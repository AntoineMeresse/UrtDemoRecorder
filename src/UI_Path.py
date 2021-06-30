from PyQt5.QtWidgets import *
from src.UI_DemoRecorder import DemoRecorder
from src.settings import Settings


class Path(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Urban Terror DemoRecorder")
        self.setGeometry(0, 0, 500, 200)

        self.settings = Settings()

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
        path_tmp = self.settings.getPath()
        if path_tmp == "":
            self.game.setText("---> Path of UrbanTerror Executable (Put your own)")
        else:
            self.path = path_tmp
            self.game.setText(path_tmp)
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
        if self.settings.getDemoType() == '.urtdemo':
            self.combo.addItem(".urtdemo")
            self.combo.addItem(".dm_68")
        else:
            self.combo.addItem(".dm_68")
            self.combo.addItem(".urtdemo")
        self.layout.addWidget(self.combo)

    def initSubmitButton(self):
        self.submit = QPushButton()
        self.submit.setText("Next")
        self.submit.clicked.connect(self.demoWindow)

        self.layout.addWidget(self.submit)

    def updateSettings(self):
        self.settings.savePath(self.path)
        self.settings.saveDemoFormat(self.combo.currentText())
        self.settings.writeInJsonFile()

    def demoWindow(self):
        if self.path != "":
            self.updateSettings()
            self.dr = DemoRecorder(self.path, self.combo.currentText(), self.settings)
            self.dr.show()
            self.close()
        else:
            msg = QMessageBox()
            msg.setText("Urban terror path is empty")
            msg.exec_()
