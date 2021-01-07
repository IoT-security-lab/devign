@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/11.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/11_graph-for-funcs-dump.sc");
}
