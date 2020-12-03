import sys
from PyQt5 import QtWidgets, QtGui, QtCore, uic
#from login_screen import Ui_Dialog


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


def showCustomerWindow():
    win = uic.loadUi("customerwindow.ui")
    win.show()
    return win


'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = showCustomerWindow()
    if window.exec():
        #d.exec_()
        app.exec()'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = showCustomerWindow()
    window.show()
    app.exec()

'''class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()'''

