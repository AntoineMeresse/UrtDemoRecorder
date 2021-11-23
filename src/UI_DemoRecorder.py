from PyQt5.QtWidgets import QCheckBox, QMainWindow, QScrollArea, QToolBar, QPushButton, QSpinBox
from PyQt5 import QtCore
from src.Demos import Demos
from src.DemosList import DemosList
from src.ConfigFile import ConfigFile
from src.style import checkbox_style

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
        # Gun
        self.toolbar = QToolBar("Gun Properties")
        self.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolbar)

        self.initGunSize()
        self.initGunX()
        self.initGunY()
        self.initGunZ()
        self.initFov()
        self.initFrameRate()
        self.initHideHud()

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

    def initGunSize(self):
        self.guns = QSpinBox(self)
        self.guns.setMinimum(0)
        self.guns.setMaximum(1)
        self.guns.setValue(0)
        self.guns.setPrefix(" Gun Size : ")
        self.toolbar.addWidget(self.guns)

    def initGunX(self):
        self.gunx = QSpinBox(self)
        self.gunx.setMinimum(0)
        self.gunx.setValue(0)
        self.gunx.setPrefix(" Gun X : ")
        self.toolbar.addWidget(self.gunx)
        
    def initGunY(self):
        self.guny = QSpinBox(self)
        self.guny.setMinimum(0)
        self.guny.setValue(0)
        self.guny.setPrefix(" Gun Y : ")
        self.toolbar.addWidget(self.guny)
        
    def initGunZ(self):
        self.gunz = QSpinBox(self)
        self.gunz.setMinimum(0)
        self.gunz.setValue(0)
        self.gunz.setPrefix(" Gun Z : ")
        self.toolbar.addWidget(self.gunz)

    def initFov(self):
        self.fov = QSpinBox(self)
        self.fov.setMinimum(50)
        self.fov.setMaximum(150)
        self.fov.setValue(110)
        self.fov.setPrefix(" DemoFov : ")
        self.toolbar.addWidget(self.fov)

    def initFrameRate(self):
        self.framerate = QSpinBox(self)
        self.framerate.setMinimum(0)
        self.framerate.setMaximum(250)
        self.framerate.setValue(25)
        self.framerate.setPrefix(" FrameRate : ")
        self.toolbar.addWidget(self.framerate)

    def initHideHud(self):
        self.hud = QCheckBox()
        self.hud.setText("Hide Hud")
        self.hud.setStyleSheet(checkbox_style)
        self.toolbar.addWidget(self.hud)

    def initNoParams(self):
        self.a_override = QCheckBox()
        self.a_override.setText("Avoid Override")
        self.a_override.setStyleSheet(checkbox_style)
        self.toolbar.addWidget(self.a_override)

    def isHudChecked(self):
        return True if self.hud.checkState() else False

    def isAvoidOverrideChecked(self):
        return True if self.a_override.checkState() else False

    def recordAction(self):
        ConfigFile(self.demos.urban, self.demos.path, self.demosLst.getDemosChecked(), self.guns.cleanText(), self.gunx.cleanText(),
                   self.guny.cleanText(), self.gunz.cleanText(), self.fov.cleanText(), self.framerate.cleanText(), True, self.isHudChecked(), self.settings)

    def playAction(self):
        ConfigFile(self.demos.urban, self.demos.path, self.demosLst.getDemosChecked(), self.guns.cleanText(), self.gunx.cleanText(),
                   self.guny.cleanText(), self.gunz.cleanText(), self.fov.cleanText(), self.framerate.cleanText(), False, self.isHudChecked(), self.settings)

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

