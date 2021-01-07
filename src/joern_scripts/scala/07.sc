@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/07.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/07_graph-for-funcs-dump.sc");
}
