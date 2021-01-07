@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/19outof20_500_cpg.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/19_graph-for-funcs-dump.sc");
}
