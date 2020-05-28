from PyQt5.QtWidgets import *
from src.UI_DemoRecorder import DemoRecorder


class Path(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Urban Terror DemoRecorder")
        self.setGeometry(0, 0, 500, 200)

        self.path = ""
        self.format = ""

        # Path
        self.layout = QVBoxLayout()

        self.initPath()
        self.initDemosFormat()
        self.initSubmitButton()

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def initPath(self):
        self.game = QLineEdit(self)
        self.game.setText("---> Path of UrbanTerror Executable (Put your own)")
        self.gameB = QPushButton()
        self.gameB.setText("Change path")
        self.gameB.clicked.connect(self.gamePath)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.game)
        layout2.addWidget(self.gameB)

        self.layout.addLayout(layout2)

    def gamePath(self):
        tmp = str(QFileDialog.getOpenFileName(self, "Open executable", "", "Executable (*.exe)"))
        self.path = tmp.split("'")[1]
        self.game.setText(self.path)

    def initDemosFormat(self):
        self.combo = QComboBox(self)
        self.combo.addItem(".urtdemo")
        self.combo.addItem(".dm_68")

        self.layout.addWidget(self.combo)

    def initSubmitButton(self):
        self.submit = QPushButton()
        self.submit.setText("Next")
        self.submit.clicked.connect(self.demoWindow)

        self.layout.addWidget(self.submit)

    def demoWindow(self):
        if self.path != "":
            self.dr = DemoRecorder(self.path,self.combo.currentText())
            self.dr.show()
            self.close()
        else:
            msg = QMessageBox()
            msg.setText("Urban terror path is empty")
            msg.exec_()
