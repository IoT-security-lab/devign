@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/08.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/08_graph-for-funcs-dump.sc");
}
