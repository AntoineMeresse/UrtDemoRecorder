class ConfigFile:

    def __init__(self, demosLst, gunSize, gunX, gunY, gunZ, fov):
        self.demosLst = demosLst
        self.gunSize = gunSize
        self.gunX = gunX
        self.gunY = gunY
        self.gunZ = gunZ
        self.fov = fov

        self.toString()

    def toString(self):
        print("\nDemos List : "+str(self.demosLst))
        print(str.format("Infos : \n - Gunsize : {} \n - GunX : {} \n - GunY : {} \n - GunZ : {} \n - Fov : {} ",
                         self.gunSize, self.gunX, self.gunY, self.gunZ, self.fov))
