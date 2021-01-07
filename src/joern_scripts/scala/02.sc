@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/02.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/02_graph-for-funcs-dump.sc");
}
