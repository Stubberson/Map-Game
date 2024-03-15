import sys
from PyQt6 import QtWidgets, QtGui, QtCore
import main_widget


def main():
    app = QtWidgets.QApplication(sys.argv)
    widget = main_widget.MainWidget()
    widget.show()
    sys.exit(app.exec())


main()
