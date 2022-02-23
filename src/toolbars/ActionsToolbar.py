from PyQt5.QtWidgets import *
from src.toolbars.style import checkbox_style

class ActionsToolbar(QToolBar):

    def __init__(self, demosLst, recordFunction, playFunction) -> None:
        super().__init__("Actions Toolbar")
        self.demosLst = demosLst
        self.recordAction = recordFunction
        self.playAction = playFunction

        self.initSelectAllButtons()
        self.initRecordButton()
        self.initPlayDemosButton()

    def initRecordButton(self):
        self.record = QPushButton()
        self.record.setText("Record")
        self.record.clicked.connect(self.recordAction)  # Change Function
        self.addWidget(self.record)

    def initSelectAllButtons(self):
        self.unselectall = QPushButton()
        self.unselectall.setText("Unselect All")
        self.unselectall.clicked.connect(self.demosLst.unselectAll)
        self.addWidget(self.unselectall)

        self.selectall = QPushButton()
        self.selectall.setText("Select All")
        self.selectall.clicked.connect(self.demosLst.selectAll)
        self.addWidget(self.selectall)

    def initPlayDemosButton(self):
        self.play = QPushButton()
        self.play.setText("Play Demo(s)")
        self.play.clicked.connect(self.playAction)
        self.addWidget(self.play)