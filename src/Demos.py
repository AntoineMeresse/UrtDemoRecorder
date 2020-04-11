class Demos():

    def __init__(self, path):
        self.path = path
        self.demosList = list()
        self.format = ".demo"

    def getInfos(self):
        print("\n=========================================================")
        print("Infos:")
        print("=========================================================")
        print("Path : " + self.path)
        print("Demos List Length : " + str(len(self.demosList)))
        print("Demos format : " + self.format)
        print("=========================================================")