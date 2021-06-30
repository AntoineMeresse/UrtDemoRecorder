import os, json

demorecorder="""{
    "path" : "",
    "demotype" : ".urtdemo",
    "hideHUD": "cg_msgtime 0; cg_chattime 0; cg_draw2d 0; cl_drawangle 0;",
    "showHUD": "cg_msgtime 6000; cg_chattime 5000; cg_draw2d 1;", 
    "customSettings": ""
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

    def writeInJsonFile(self):
        if self.hasChanged:
            with open(self.settingFileName, 'w') as f:
                json.dump(self.settings, f, indent=4)

    def getPath(self):
        return self.settings['path']

    def getDemoType(self):
        return self.settings['demotype']

    def getHideHud(self):
        return self.settings['hideHUD']

    def getShowHud(self):
        return self.settings['showHUD']

    def getCustomSetttings(self):
        return self.settings['customSettings']

    def savePath(self, path):
        if self.getPath() != path:
            self.settings['path'] = path
            self.hasChanged = True

    def saveDemoFormat(self, demotype):
        if self.getDemoType() != demotype:
            self.settings['demotype'] = demotype
            self.hasChanged = True

