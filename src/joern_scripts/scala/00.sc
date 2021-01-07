@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/00.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/00_graph-for-funcs-dump.sc");
}
