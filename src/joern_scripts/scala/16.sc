@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/16.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/16_graph-for-funcs-dump.sc");
}
