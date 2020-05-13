from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea, QToolBar, QPushButton, QLineEdit, QSpinBox, QAction, QFileDialog
from PyQt5 import QtCore
from src.Demos import Demos
from src.Window import DemosList
import sys

class DemoRecorder(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Urban Terror DemoRecorder")
        self.setGeometry(0, 0, 800, 500)

        self.path = ""

        # Datas
        d = Demos("C:\\Logiciels\\UrbanTerror43")
        demosLst = DemosList(d.demosList)

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

        # Path
        self.toolbarPath = QToolBar("Paths")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbarPath)

        self.initPath()

        self.initRecordButton()

        #######################################################
        # Scroll Area
        self.sArea = QScrollArea()
        self.sArea.setWidget(demosLst)

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
        self.record.clicked.connect(self.void) # Change Function
        self.toolbar.addWidget(self.record)

    def initPath(self):
        self.game = QLineEdit(self)
        self.game.setText("Path of UrbanTerror")
        self.gameB = QPushButton()
        self.gameB.setText("Change path")
        self.gameB.clicked.connect(self.gamePath)
        self.toolbarPath.addWidget(self.game)
        self.toolbarPath.addWidget(self.gameB)

    def gamePath(self):
        tmp = str(QFileDialog.getOpenFileName(self))
        self.path = tmp.split("'")[1]
        self.game.setText(self.path)


    def void(self):
        print("Print void")


def main(args):
    """
    d = Demos("C:\\Logiciels\\UrbanTerror43")

    app = QApplication(args)
    win = QMainWindow()
    dList = DemosList(d.demosList)
    scr = QScrollArea()

    win.setGeometry(0, 0, 200, 200)
    scr.setWidget(dList)
    win.setCentralWidget(scr)

    win.show()
    app.exec_()
    """
    app = QApplication(args)
    dRec = DemoRecorder()
    dRec.show()
    app.exec_()

if __name__ == "__main__":
    main(sys.argv)
