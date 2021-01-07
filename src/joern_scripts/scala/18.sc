@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/18.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/18_graph-for-funcs-dump.sc");
}
