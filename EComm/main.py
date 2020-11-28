# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets, uic


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win1 = uic.loadUi("login.ui")
    win2 = uic.loadUi("cussignup.ui")
    win3 = uic.loadUi("selsignup.ui")
    win4 = uic.loadUi("wrongcred.ui")

    win1.show()
    win2.show()
    win3.show()
    win4.show()

    app.exec()
