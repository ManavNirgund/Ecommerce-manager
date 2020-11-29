import sys
from PyQt5 import QtWidgets, uic


def showLogin():
    win = uic.loadUi("login_screen.ui")
    win.show()
    return win


def showSellerSignup():
    win = uic.loadUi("seller_signup.ui")
    win.show()
    return win


def showCustomerSignup():
    win = uic.loadUi("customer_signup.ui")
    win.show()
    return win


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = showLogin()
    if window.exec():
        app.exec()