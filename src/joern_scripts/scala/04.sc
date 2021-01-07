@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/04.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/04_graph-for-funcs-dump.sc");
}
