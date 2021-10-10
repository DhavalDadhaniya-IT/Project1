import sys
from PyQt5 import QtGui
from os import environ
from PyQt5.QtWidgets import QApplication
from view import GUI
# Client code

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = GUI()
    view.show()
    sys.exit(pycalc.exec_())
   # sys.exit(pycalc.exec_())
if __name__ == '__main__':
    suppress_qt_warnings()
    main()