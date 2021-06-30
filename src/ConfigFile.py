import os

from src.settings import Settings


class ConfigFile:

    def __init__(self, urtpath, dirpath, demosLst, gunSize, gunX, gunY, gunZ, fov, framerate, toBeRecord, hideHUD ,settings : Settings):
        self.urtpath = urtpath
        self.dirpath = dirpath
        self.demosLst = demosLst
        self.gunSize = gunSize
        self.gunX = gunX
        self.gunY = gunY
        self.gunZ = gunZ
        self.fov = fov
        self.framerate = framerate
        self.toberecord = toBeRecord
        self.hideHUD = hideHUD
        self.settings = settings

        self.createConfigFile()
        self.execConfigFile()

    def createConfigFile(self):
        """
        Function to create the config file (.cfg)
        :param path: a path
        """
        filepath = self.dirpath + os.sep + "q3ut4" + os.sep + "demorecorder.cfg"
        with open(filepath, "w+") as fl:
            if (self.settings.getCustomSetttings() != ""):
                fl.write(self.settings.getCustomSetttings()+"\n")
            if self.hideHUD:
                fl.write("{}\n".format(self.settings.getHideHud()))
            for i in range(0, len(self.demosLst)):
                demo = self.demosLst[i]
                line = str.format('seta demo{} "set nextdemo vstr demo{}; demo {}; {}',
                                  i, i+1, demo, self.getParams())
                if self.toberecord:
                    line += str.format('; video {}"\n', demo.split(".")[0])
                else:
                    line += '"\n'
                fl.write(line)
            fl.write(str.format('seta demo{} "demo {}; {} quit"', len(self.demosLst), self.demosLst[0], self.settings.getShowHud()))

    def getParams(self):
        return(str.format("cg_gunsize {}; cg_gunx {}; cg_guny {}; cg_gunz {}; cg_demofov {}; cl_aviFrameRate {}",
               self.gunSize, self.gunX, self.gunY, self.gunZ, self.fov, self.framerate))

    def execConfigFile(self):
        executable = self.urtpath.split(os.sep)[-1]
        cmd = str.format("cd /d {} && {} + exec demorecorder.cfg + vstr demo0", self.dirpath, executable)
        #cmd = str.format("{}/{} + exec demorecorder.cfg + vstr demo0", self.dirpath, executable)
        print(cmd)
        os.system(cmd)

    def toString(self):
        """
        Function to display informations of this object
        """
        print("\nDemos List : "+str(self.demosLst))
        print("Path : " + self.path)
        print(str.format("Infos : \n - Gunsize : {} \n - GunX : {} \n - GunY : {} \n - GunZ : {} \n - Fov : {} ",
                         self.gunSize, self.gunX, self.gunY, self.gunZ, self.fov))
