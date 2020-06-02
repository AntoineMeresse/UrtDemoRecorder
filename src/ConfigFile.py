import os


class ConfigFile:

    def __init__(self, urtpath, dirpath, demosLst, gunSize, gunX, gunY, gunZ, fov):
        self.urtpath = urtpath
        self.dirpath = dirpath
        self.demosLst = demosLst
        self.gunSize = gunSize
        self.gunX = gunX
        self.gunY = gunY
        self.gunZ = gunZ
        self.fov = fov

        self.createConfigFile()
        self.execConfigFile()

    def createConfigFile(self):
        """
        Function to create the config file (.cfg)
        :param path: a path
        """
        filepath = self.dirpath + os.sep + "q3ut4" + os.sep + "demorecorder.cfg"
        with open(filepath, "w+") as fl:
            for i in range(0, len(self.demosLst)):
                demosName = self.demosLst[i].split(".")[0]
                line = str.format('seta demo{} "set nextdemo vstr demo{}; demo {}; {} ; video {}"\n',
                                  i, i+1, demosName, self.getParams(), demosName)
                fl.write(line)
            fl.write(str.format('seta demo{} "demo {}; quit"', len(self.demosLst), self.demosLst[0]))

    def getParams(self):
        return(str.format("cg_gunsize {}; cg_gunx {}; cg_guny {}; cg_gunz {}; cg_demofov {}",
               self.gunSize, self.gunX, self.gunY, self.gunZ, self.fov))

    def execConfigFile(self):
        executable = self.urtpath.split(os.sep)[-1]
        cmd = str.format("cd {} && {} + exec demorecorder.cfg + vstr demo0",self.dirpath,executable)
        os.system(cmd)

    def toString(self):
        """
        Function to display informations of this object
        """
        print("\nDemos List : "+str(self.demosLst))
        print("Path : " + self.path)
        print(str.format("Infos : \n - Gunsize : {} \n - GunX : {} \n - GunY : {} \n - GunZ : {} \n - Fov : {} ",
                         self.gunSize, self.gunX, self.gunY, self.gunZ, self.fov))
