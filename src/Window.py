from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DemosList(QWidget):

    def __init__(self, demosList):
        super().__init__()
        self.demosList = demosList
        self.lstCpy = demosList.copy()

        self.initWidget()
        self.demosChecked = list()

    def initWidget(self):
        self.grid = QGridLayout()

        for i, v in enumerate(self.demosList):
            self.demosList[i] = QCheckBox(v)
            self.grid.addWidget(self.demosList[i], i, 0)

        self.setLayout(self.grid)

    def getDemosChecked(self):
        for i, v in enumerate(self.demosList):
            if v.checkState():
                self.demosChecked.append(self.lstCpy[i])
        print(self.demosChecked)
