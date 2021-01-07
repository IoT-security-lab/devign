@main def exec() = {
        var path = System.getProperty("user.dir");
        print(path);
        importCpg("/home/kb/hd/datasets/devign/qemu.cpg");
        cpg.runScript("graph-for-funcs-dump.sc");
}
