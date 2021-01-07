@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/03.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/03_graph-for-funcs-dump.sc");
}
