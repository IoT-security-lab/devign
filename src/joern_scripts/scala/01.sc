@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/01.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/01_graph-for-funcs-dump.sc");
}
