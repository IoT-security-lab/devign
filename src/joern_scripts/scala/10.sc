@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/10.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/10_graph-for-funcs-dump.sc");
}
