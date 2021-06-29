import os, json

demorecorder="""{
    "path" : "",
    "demotype" : ".urtdemo"
}
"""

class Settings:

    def __init__(self):
        self.settingFileName = 'demorecorder.json'
        self.initSettingFileIfItDoesntExist()
        self.settings = None
        self.hasChanged = False

        self.readJsonFile()

    def initSettingFileIfItDoesntExist(self):
        if not os.path.exists(self.settingFileName):
            with open(self.settingFileName, 'w') as f:
                f.write(demorecorder)

    def readJsonFile(self):
        with open(self.settingFileName, 'r') as f:
            self.settings = json.load(f)
            print(self.settings)

    def writeInJsonFile(self):
        if self.hasChanged:
            with open(self.settingFileName, 'w') as f:
                json.dump(self.settings, f)

    def getPath(self):
        return self.settings['path']

    def getDemoType(self):
        return self.settings['demotype']

    def savePath(self, path):
        if self.getPath() != path:
            self.settings['path'] = path
            self.hasChanged = True

    def saveDemoFormat(self, demotype):
        if self.getDemoType() != demotype:
            self.settings['demotype'] = demotype
            self.hasChanged = True

