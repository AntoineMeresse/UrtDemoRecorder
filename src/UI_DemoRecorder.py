from PyQt5.QtWidgets import QMainWindow, QScrollArea, QToolBar, QPushButton, QSpinBox
from PyQt5 import QtCore
from src.Demos import Demos
from src.DemosList import DemosList


class DemoRecorder(QMainWindow):

    def __init__(self, path, fmt):
        super().__init__()
        self.setWindowTitle("Urban Terror DemoRecorder")
        self.setGeometry(0, 0, 800, 500)

        # Datas
        d = Demos(path)
        d.changeFormat(fmt)
        self.demosLst = DemosList(d.demosList)

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

        # Button
        self.toolbar2 = QToolBar("Buttons")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar2)

        self.initSelectAllButtons()
        self.initRecordButton()

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

    def initRecordButton(self):
        self.record = QPushButton()
        self.record.setText("Record")
        self.record.clicked.connect(self.demosLst.getDemosChecked)  # Change Function
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

    def void(self):
        print("Print void")

