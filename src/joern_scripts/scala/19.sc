@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/19.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/19_graph-for-funcs-dump.sc");
}
