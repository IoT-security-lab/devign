@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/14.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/14_graph-for-funcs-dump.sc");
}
