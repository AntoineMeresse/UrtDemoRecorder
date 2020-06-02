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
            fl.write(filepath)

    def toString(self):
        """
        Function to display information of this object
        """
        print("\nDemos List : "+str(self.demosLst))
        print("Path : " + self.path)
        print(str.format("Infos : \n - Gunsize : {} \n - GunX : {} \n - GunY : {} \n - GunZ : {} \n - Fov : {} ",
                         self.gunSize, self.gunX, self.gunY, self.gunZ, self.fov))
