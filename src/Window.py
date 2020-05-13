from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DemosList(QWidget):

    def __init__(self, demosList):
        super().__init__()
        self.demosList = demosList

        self.initWidget()

    def initWidget(self):
        self.grid = QGridLayout()

        for i, v in enumerate(self.demosList):
            self.demosList[i] = QCheckBox(v)
            self.grid.addWidget(self.demosList[i], i, 0)

        self.setLayout(self.grid)
