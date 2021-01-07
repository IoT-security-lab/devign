@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/05.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/05_graph-for-funcs-dump.sc");
}
