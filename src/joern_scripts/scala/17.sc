@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/17outof20_500_cpg.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/17_graph-for-funcs-dump.sc");
}
