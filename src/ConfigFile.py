import os


class ConfigFile:

    def __init__(self, path, demosLst, gunSize, gunX, gunY, gunZ, fov):
        self.path = path
        self.demosLst = demosLst
        self.gunSize = gunSize
        self.gunX = gunX
        self.gunY = gunY
        self.gunZ = gunZ
        self.fov = fov

        self.toString()
        self.createConfigFile()

    def createConfigFile(self):
        """
        Function to create the config file (.cfg)
        :param path: a path
        """
        filepath = self.path + os.sep + "q3ut4" + os.sep + "demorecorder.cfg"
        with open(filepath, "w+") as fl:
            for i in range(0, len(self.demosLst)):
                demosName = self.demosLst[i]
                line = str.format('seta demo{} "set nextdemo vstr demo{}; demo {}; {} ; video {}"\n',
                                  i, i+1, demosName, self.getParams(), demosName)
                fl.write(line)
            # Last demos, start then close urt. (To test without demo)
            fl.write(str.format('seta demo{} "demo {}; quit"', len(self.demosLst), self.demosLst[0]))

    def getParams(self):
        return(str.format("cg_gunsize {}; cg_gunx {}; cg_guny {}; cg_gunz {}; cg_demofov {}",
               self.gunSize, self.gunX, self.gunY, self.gunZ, self.fov))

    def toString(self):
        """
        Function to display informations of this object
        """
        print("\nDemos List : "+str(self.demosLst))
        print("Path : " + self.path)
        print(str.format("Infos : \n - Gunsize : {} \n - GunX : {} \n - GunY : {} \n - GunZ : {} \n - Fov : {} ",
                         self.gunSize, self.gunX, self.gunY, self.gunZ, self.fov))
