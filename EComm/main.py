# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets, uic


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win1 = uic.loadUi("mainwindow.ui")
    win2 = uic.loadUi("cuslogin.ui")
    win3 = uic.loadUi("sellogin.ui")

    win1.show()
    win2.show()
    win3.show()

    app.exec()
