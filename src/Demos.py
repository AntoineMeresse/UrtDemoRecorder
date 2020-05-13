from os import listdir
from os.path import isdir, sep

class Demos:

    def __init__(self, path):
        self.path = path
        self.pathQ3UT4 = path+sep+"q3ut4"
        self.pathDemos = self.pathQ3UT4+sep+"demos"
        self.demosList = list()
        self.format = ".dm_68"
        self.initDemosList()

    def changeFormat(self, format):
        if format in [".demo", ".dm_68"]:
            self.format = format

    def initDemosList(self):
        self.demosList = list()
        if isdir(self.pathDemos):
            for elem in listdir(self.pathDemos):
                if self.format in elem:
                    self.demosList.append(elem)

    def getInfos(self):
        print("\n=========================================================")
        print("Infos:")
        print("=========================================================")
        print("Path : " + self.path)
        print("Demos List Length : " + str(len(self.demosList)))
        print("Demos format : " + self.format)
        print("=========================================================")