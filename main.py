from PyQt5.QtWidgets import *
from src.UI_Path import Path
from src.UI_DemoRecorder import DemoRecorder
import sys


def main(args):
    app = QApplication(args)
    #window = DemoRecorder("C:/Logiciels/UrbanTerror43/Quake3-UrT.exe", ".urtdemo")
    window = Path()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main(sys.argv)