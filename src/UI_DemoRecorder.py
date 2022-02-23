from PyQt5.QtWidgets import QCheckBox, QMainWindow, QScrollArea, QToolBar, QPushButton, QSpinBox
from PyQt5 import QtCore
from src.Demos import Demos
from src.DemosList import DemosList
from src.ConfigFile import ConfigFile
# from toolbars.style import checkbox_style
from src.toolbars.SettingsToolbar import SettingsToolbar

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
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.settingsToolbar)

        # Button
        self.toolbar2 = QToolBar("Buttons")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar2)

        self.initSelectAllButtons()
        self.initRecordButton()
        self.initPlayDemosButton()

        #######################################################
        # Scroll Area
        self.sArea = QScrollArea()
        self.sArea.setWidget(self.demosLst)

        #######################################################
        # Main
        self.setCentralWidget(self.sArea)


    def recordAction(self):
        ConfigFile(self.demos.urban, self.demos.path, self.demosLst.getDemosChecked(), self.settingsToolbar.getGunSize(), self.settingsToolbar.getGunx(),
                   self.settingsToolbar.getGuny(), self.settingsToolbar.getGunz(), self.settingsToolbar.getFov(), self.settingsToolbar.getFramerate(), True, self.settingsToolbar.isHudChecked(), self.settings,
                   self.settingsToolbar.isAvoidOverrideChecked(), self.settingsToolbar.isVideoPipeChecked())

    def playAction(self):
        ConfigFile(self.demos.urban, self.demos.path, self.demosLst.getDemosChecked(), self.settingsToolbar.getGunSize(), self.settingsToolbar.getGunx(),
                   self.settingsToolbar.getGuny(), self.settingsToolbar.getGunz(), self.settingsToolbar.getFov(), self.settingsToolbar.getFramerate(), False, self.settingsToolbar.isHudChecked(), self.settings,
                   self.settingsToolbar.isAvoidOverrideChecked(), False)

    def initRecordButton(self):
        self.record = QPushButton()
        self.record.setText("Record")
        self.record.clicked.connect(self.recordAction)  # Change Function
        self.toolbar2.addWidget(self.record)

    def initSelectAllButtons(self):
        self.unselectall = QPushButton()
        self.unselectall.setText("Unselect All")
        self.unselectall.clicked.connect(self.demosLst.unselectAll)
        self.toolbar2.addWidget(self.unselectall)

        self.selectall = QPushButton()
        self.selectall.setText("Select All")
        self.selectall.clicked.connect(self.demosLst.selectAll)
        self.toolbar2.addWidget(self.selectall)

    def initPlayDemosButton(self):
        self.play = QPushButton()
        self.play.setText("Play Demo(s)")
        self.play.clicked.connect(self.playAction)
        self.toolbar2.addWidget(self.play)

    def void(self):
        print("Print void")

