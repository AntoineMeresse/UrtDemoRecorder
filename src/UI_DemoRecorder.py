from PyQt5.QtWidgets import QCheckBox, QMainWindow, QScrollArea, QToolBar, QPushButton, QSpinBox
from PyQt5 import QtCore
from src.Demos import Demos
from src.DemosList import DemosList
from src.ConfigFile import ConfigFile
from src.toolbars.SettingsToolbar import SettingsToolbar
from src.toolbars.ActionsToolbar import ActionsToolbar

class DemoRecorder(QMainWindow):

    def __init__(self, path, fmt, settings):
        super().__init__()
        self.setWindowTitle("Urban Terror DemoRecorder")
        self.setGeometry(0, 0, 800, 500)
        self.settings = settings

        # Datas
        self.demos = Demos(path)
        self.demos.changeFormat(fmt)
        self.demosLst = DemosList(self.demos.demosList)

        #######################################################
        # ToolBar
        self.settingsToolbar : SettingsToolbar = SettingsToolbar()
        self.actionsToolbar : ActionsToolbar = ActionsToolbar(self.demosLst, self.recordAction, self.playAction)
        
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.settingsToolbar)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.actionsToolbar)

        #######################################################
        # Scroll Area (Main Element)
        self.sArea = QScrollArea()
        self.sArea.setWidget(self.demosLst)

        self.setCentralWidget(self.sArea)


    def recordAction(self):
        ConfigFile(self.demos.urban, self.demos.path, self.demosLst.getDemosChecked(), self.settingsToolbar.getGunSize(), self.settingsToolbar.getGunx(),
                   self.settingsToolbar.getGuny(), self.settingsToolbar.getGunz(), self.settingsToolbar.getFov(), self.settingsToolbar.getFramerate(), True, self.settingsToolbar.isHudChecked(), self.settings,
                   self.settingsToolbar.isAvoidOverrideChecked(), self.settingsToolbar.isVideoPipeChecked())

    def playAction(self):
        ConfigFile(self.demos.urban, self.demos.path, self.demosLst.getDemosChecked(), self.settingsToolbar.getGunSize(), self.settingsToolbar.getGunx(),
                   self.settingsToolbar.getGuny(), self.settingsToolbar.getGunz(), self.settingsToolbar.getFov(), self.settingsToolbar.getFramerate(), False, self.settingsToolbar.isHudChecked(), self.settings,
                   self.settingsToolbar.isAvoidOverrideChecked(), False)
