@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/09.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/09_graph-for-funcs-dump.sc");
}
