import json
import math
import re
import subprocess
import pty
import os.path
import os
import sys
import time
from .cpg_client_wrapper import CPGClientWrapper
#from ..data import datamanager as data


def funcs_to_graphs(funcs_path):
    client = CPGClientWrapper()
    # query the cpg for the dataset
    print(f"Creating CPG.")
    graphs_string = client(funcs_path)
    # removes unnecessary namespace for object references
    graphs_string = re.sub(r"io\.shiftleft\.codepropertygraph\.generated\.", '', graphs_string)
    graphs_json = json.loads(graphs_string)

    return graphs_json["functions"]


def graph_indexing(graph):
    idx = int(graph["file"].split(".c")[0].split("/")[-1])  # remove path from graph
    del graph["file"]
    return idx, {"functions": [graph]}


def joern_parse(joern_path, input_path, output_path, file_name):
    out_file = file_name + ".bin"
    if os.path.exists(output_path+out_file):
        print(f"File {out_file} already exists. Skipping cpg creation.")
    else:
        joern_parse_call = subprocess.run(["./" + joern_path + "joern-parse", input_path, "--out", output_path + out_file],
                                      stdout=subprocess.PIPE, text=True, check=True)
        # print(str(joern_parse_call))
    return out_file


def joern_create(bash_path, cpg_files, parallel=True, jobs=2):
    json_files = []
    num_files = len(cpg_files)
    if num_files < jobs:
        print("[Warning] The number of CPF files is greater than jobs number.")
    for cpg in range(math.ceil(num_files/jobs)):
        process = []
        left = len(cpg_files)
        loops = jobs if jobs < left else left
        for p in range(loops):
            this = cpg_files.pop()
            filtered = re.search(r'^\d+', this)
            bash_script = f"{bash_path}{filtered.group(0)}.bash"
            if not os.path.exists(bash_script):
                print(f"[Error] path {bash_script} does not exists for cpg {this}. Exit.")
                sys.exit(-1)
            print(f"Executing: {bash_script}.")
            process.append(subprocess.Popen(f"{bash_script} &", shell=True, stdout=subprocess.PIPE))
        exit_codes = [p.wait() for p in process]  # wait for all jobs to finish
        for p in process:
            output = p.stdout.readlines()[-1].decode()
            if ".json" in output:
                output = output.replace('\n', '')
                json_files.append(output)
    if len(json_files) == num_files:
        return json_files
    else:
        print(f"[Error] Some CPG/Json files were not process successfully, missing {num_files-len(json_files)} files.")
        sys.exit(-1)






# def joern_create(joern_path, in_path, out_path, cpg_files):
#     joern_process = subprocess.Popen(["./" + joern_path + "joern"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#     time.sleep(10)
#     json_files = []
#     for cpg_file in cpg_files:
#         json_file_name = f"{cpg_file.split('.')[0]}.json"
#         json_files.append(json_file_name)
#
#         print(in_path+cpg_file)
#         if os.path.exists(in_path+cpg_file):
#             json_out = f"{os.path.abspath(out_path)}/{json_file_name}"
#             import_cpg_cmd = f"importCpg(\"{os.path.abspath(in_path)}/{cpg_file}\")\r".encode()
#             script_path = f"{os.path.dirname(os.path.abspath(joern_path))}/graph-for-funcs-dump.sc"
#             run_script_cmd = f"cpg.runScript('{script_path}')".encode()
#             # os.rename(joern_path + "graph-for-funcs.json", json_out)
#             # run_script_cmd = f"cpg.runScript('{script_path}').toString() |> \"{json_out}\"\r".encode()
#             print(f"Running in Joern: {import_cpg_cmd.decode()}")
#             joern_process.stdin.write(import_cpg_cmd)
#             joern_process.communicate(timeout=100)
#             # print(joern_process.stdout.readline().decode())
#             # print(f"Running in Joern: {run_script_cmd.decode()}")
#             # joern_process.stdin.write(run_script_cmd)
#             # # print(joern_process.stdout.readline().decode())
#             # joern_process.stdin.write("delete\r".encode())
#             # print(joern_process.stdout.readline().decode())
#     try:
#         outs, errs = joern_process.communicate(timeout=100)
#     except subprocess.TimeoutExpired:
#         print("Time expired. Killing Joern.")
#         joern_process.kill()
#         outs, errs = joern_process.communicate()
#     if outs is not None:
#         print(f"Outs: {outs.decode()}")
#     if errs is not None:
#         print(f"Errs: {errs.decode()}")
#     return json_files


def json_process(in_path, json_file):
    if os.path.exists(in_path+json_file):
        with open(in_path+json_file) as jf:
            cpg_string = jf.read()
            cpg_string = re.sub(r"io\.shiftleft\.codepropertygraph\.generated\.", '', cpg_string) # rename 'function' section in json pdg
            cpg_json = json.loads(cpg_string)
            container = []
            for graph in cpg_json["functions"]:
                container.append(graph)
            return container
    return None

'''
def generate(dataset, funcs_path):
    dataset_size = len(dataset)
    print("Size: ", dataset_size)
    graphs = funcs_to_graphs(funcs_path[2:])
    print(f"Processing CPG.")
    container = [graph_indexing(graph) for graph in graphs["functions"] if graph["file"] != "N/A"]
    graph_dataset = data.create_with_index(container, ["Index", "cpg"])
    print(f"Dataset processed.")

    return data.inner_join_by_index(dataset, graph_dataset)
'''

# client = CPGClientWrapper()
# client.create_cpg("../../data/joern/")
# joern_parse("../../joern/joern-cli/", "../../data/joern/", "../../joern/joern-cli/", "gen_test")
# print(funcs_to_graphs("/data/joern/"))
"""
while True:
    raw = input("query: ")
    response = client.query(raw)
    print(response)
"""