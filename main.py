# -*- coding: utf-8 -*-
"""
    This module is intended to join all the pipeline in separated tasks
    to be executed individually or in a flow by using command-line options

    Example:
    Dataset embedding and processing:
        $ python taskflows.py -e -pS
"""

import argparse
import gc
import os
import shutil
from argparse import ArgumentParser
from gensim.models.word2vec import Word2Vec
import configs
import src.data as data
import src.prepare as prepare  # need torch
import src.process as process  # need torch
import src.utils.functions.cpg as cpg  # need torch

PATHS = configs.Paths()
FILES = configs.Files()
DEVICE = FILES.get_device()


def select(dataset, project):
    """
    Filter the original dataset for faster processing time. Not needed in original Devign model.
    """
    result = dataset.loc[dataset['project'] == project]  # choosing only 'FFmpeg' project
    # len_filter = result.func.str.len() < 1200   # filter to select functions with length less than 1200 chars
    # result = result.loc[len_filter] # apply filter
    # result = result.head(200)   # obtain only top 200 results 
    return result


def create_task():
    ffmpeg_proj = "FFmpeg"
    qemu_proj = "qemu"
    context = configs.Create()
    raw = data.read(PATHS.raw, FILES.raw)  # read original dataset published by the authors (qemu and ffmpeg)
    ffmpeg_data = data.apply_filter(raw, ffmpeg_proj, select)  # run select function on whole dataset
    ffmpeg_data = data.clean(ffmpeg_data)  # remove duplicates in the dataset after applying the filter
    data.drop(ffmpeg_data, ["commit_id", "project"])  # ignored data for each function
    slices = data.slice_frame(ffmpeg_data, context.slice_size)  # get # of `slice_size` functions at the time
    slices = [(s, slice.apply(lambda x: x)) for s, slice in slices]  # not sure what this lambda function does
    total_slices = len(slices)
    cpg_files = []  # list for all cpg generated
    # Create CPG binary files
    index = 0

    # for s, slice in slices:
    #     i = 0
    #     # s = slices[i][0]
    #     # slice = slices[i][1]
    #     file_name = f"{ffmpeg_proj}_{i}-{total_slices}_{context.slice_size}each"
    #     # print(file_name)
    #     data.to_files(slice, PATHS.temp, file_name)  # write files selected to disk
    #     cpg_file = prepare.joern_parse(context.joern_cli_dir, PATHS.temp, PATHS.cpg,
    #                                    f"{s+1}outof{total_slices}_{context.slice_size}_{FILES.cpg}")  # generate cpg file calling joern-parse
    #     cpg_files.append(cpg_file)  # add cpg file path
    #     print(f"Dataset {s} to cpg.")
    #     shutil.rmtree(PATHS.temp)  # delete files in disk
    #     i += 1

    # Create CPG with graphs json files
    # json_files = prepare.joern_create(context.joern_cli_dir, PATHS.cpg, PATHS.cpg,
    #                                   cpg_files)  # run joern script 'graph-for-funcs.sc'
    cpg_files = os.listdir(PATHS.cpg)
    print(cpg_files)
    json_files = prepare.joern_create(PATHS.bash, cpg_files)
    for (s, slice), json_file in zip(slices, json_files):
        graphs = prepare.json_process(PATHS.json, json_file)  # rename the function section and return a 'container'
        if graphs is None:
            print(f"Dataset chunk {s} not processed.")
            continue
        dataset = data.create_with_index(graphs, ["Index", "cpg"])
        dataset = data.inner_join_by_index(slice, dataset)
        print(f"Writing cpg dataset chunk {s} to: {PATHS.cpg_pickle}.")
        data.write(dataset, PATHS.cpg_pickle, f"{s}_{FILES.cpg}.pkl")
        del dataset
        gc.collect()


def embed_task():
    context = configs.Embed()
    # Tokenize source code into tokens
    dataset_files = data.get_directory_files(PATHS.cpg)
    w2vmodel = Word2Vec(**context.w2v_args)
    w2v_init = True
    for pkl_file in dataset_files:
        file_name = pkl_file.split(".")[0]
        cpg_dataset = data.load(PATHS.cpg, pkl_file)
        tokens_dataset = data.tokenize(cpg_dataset)
        data.write(tokens_dataset, PATHS.tokens, f"{file_name}_{FILES.tokens}")
        # word2vec used to learn the initial embedding of each token
        w2vmodel.build_vocab(sentences=tokens_dataset.tokens, update=not w2v_init)
        w2vmodel.train(tokens_dataset.tokens, total_examples=w2vmodel.corpus_count, epochs=1)
        if w2v_init:
            w2v_init = False
        # Embed cpg to node representation and pass to graph data structure
        cpg_dataset["nodes"] = cpg_dataset.apply(lambda row: cpg.parse_to_nodes(row.cpg, context.nodes_dim), axis=1)
        # remove rows with no nodes
        cpg_dataset = cpg_dataset.loc[cpg_dataset.nodes.map(len) > 0]
        cpg_dataset["input"] = cpg_dataset.apply(
            lambda row: prepare.nodes_to_input(row.nodes, row.target, context.nodes_dim,
                                               w2vmodel.wv, context.edge_type), axis=1)
        data.drop(cpg_dataset, ["nodes"])
        print(f"Saving input dataset {file_name} with size {len(cpg_dataset)}.")
        data.write(cpg_dataset[["input", "target"]], PATHS.input, f"{file_name}_{FILES.input}")
        del cpg_dataset
        gc.collect()
    model_file = f"{PATHS.w2v}{FILES.w2v}";
    print(f"Saving w2vmodel to {model_file}")
    w2vmodel.save(model_file)
    return


def process_task(stopping):
    context = configs.Process()
    devign = configs.Devign()
    model_path = PATHS.model + FILES.model
    model = process.Devign(path=model_path, device=DEVICE, model=devign.model, learning_rate=devign.learning_rate,
                           weight_decay=devign.weight_decay,
                           loss_lambda=devign.loss_lambda)
    train = process.Train(model, context.epochs)
    input_dataset = data.loads(PATHS.input)
    # split the dataset and pass to DataLoader with batch size
    train_loader, val_loader, test_loader = list(
        map(lambda x: x.get_loader(context.batch_size, shuffle=context.shuffle),
            data.train_val_test_split(input_dataset, shuffle=context.shuffle)))
    train_loader_step = process.LoaderStep("Train", train_loader, DEVICE)
    val_loader_step = process.LoaderStep("Validation", val_loader, DEVICE)
    test_loader_step = process.LoaderStep("Test", test_loader, DEVICE)

    if stopping:
        early_stopping = process.EarlyStopping(model, patience=context.patience)
        train(train_loader_step, val_loader_step, early_stopping)
        model.load()
    else:
        train(train_loader_step, val_loader_step)
        model.save()

    process.predict(model, test_loader_step)


def main():
    """
    main function that executes tasks based on command-line options
    """
    parser: ArgumentParser = argparse.ArgumentParser()
    # parser.add_argument('-p', '--prepare', help='Prepare task', required=False)
    parser.add_argument('-c', '--create', action='store_true')
    parser.add_argument('-e', '--embed', action='store_true')
    parser.add_argument('-p', '--process', action='store_true')
    parser.add_argument('-pS', '--process_stopping', action='store_true')

    args = parser.parse_args()

    if args.create:
        create_task()
    if args.embed:
        embed_task()
    if args.process:
        process_task(False)
    if args.process_stopping:
        process_task(True)


if __name__ == "__main__":
    main()
