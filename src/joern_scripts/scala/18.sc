@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("data/cpg/18outof20_500_cpg.bin");
        cpg.runScript(path + "/src/joern_scripts/scala/18_graph-for-funcs-dump.sc");
}
