@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/06.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/06_graph-for-funcs-dump.sc");
}
