from PyQt5.QtWidgets import *
from src.UI_Path import Path
import sys

def main(args):
    app = QApplication(args)
    window = Path()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main(sys.argv)