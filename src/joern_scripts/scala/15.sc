@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/15.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/15_graph-for-funcs-dump.sc");
}
