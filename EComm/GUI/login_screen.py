from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

from GUI.customer_signup import CustomerSignupGUI
from Database.database_queries import verify_user
from Database.database_update import user_insert


class LoginScreenGUI(object):
    def __init__(self, conn, MainWindow):
        self.conn = conn
        self.mainform = MainWindow
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 561)
        MainWindow.setMinimumSize(QtCore.QSize(401, 561))
        MainWindow.setMaximumSize(QtCore.QSize(401, 561))
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("./Resources/Icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(self.icon)
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 561))
        self.frame.setStyleSheet("background: #444;\n"
                                 "color: white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_Depot = QtWidgets.QLabel(self.frame)
        self.lbl_Depot.setGeometry(QtCore.QRect(50, 30, 280, 100))
        self.lbl_Depot.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_Depot.setStyleSheet("font-family: Calibri Light;\n"
                                     "font-size: 50px;\n"
                                     "font-weight: bold;")
        self.lbl_Depot.setText("")
        self.lbl_Depot.setPixmap(QtGui.QPixmap("./Resources/Icons/depot.png"))
        self.lbl_Depot.setScaledContents(True)
        self.lbl_Depot.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Depot.setObjectName("lbl_Depot")
        self.txt_Pass = QtWidgets.QLineEdit(self.frame)
        self.txt_Pass.setGeometry(QtCore.QRect(130, 230, 241, 31))
        self.txt_Pass.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txt_Pass.setStyleSheet("border: 2px solid rgb(243, 76, 83);\n"
                                    "border-radius: 15px;\n"
                                    "padding-left: 10px;\n"
                                    "padding-bottom: 1px;\n"
                                    "color: white;\n"
                                    "font-size: 20px;")
        self.txt_Pass.setClearButtonEnabled(True)
        self.txt_Pass.setObjectName("txt_Pass")
        self.txt_Pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_Email = QtWidgets.QLineEdit(self.frame)
        self.txt_Email.setGeometry(QtCore.QRect(130, 160, 241, 31))
        self.txt_Email.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txt_Email.setStyleSheet("border: 2px solid rgb(243, 76, 83);\n"
                                     "border-radius: 15px;\n"
                                     "padding-left: 10px;\n"
                                     "padding-bottom: 1px;\n"
                                     "color: white;\n"
                                     "font-size: 20px;")
        self.txt_Email.setClearButtonEnabled(True)
        self.txt_Email.setObjectName("txt_Email")
        self.lbl_Pass = QtWidgets.QLabel(self.frame)
        self.lbl_Pass.setGeometry(QtCore.QRect(10, 230, 101, 31))
        self.lbl_Pass.setStyleSheet("color: white;\n"
                                    "font-size: 20px;")
        self.lbl_Pass.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_Pass.setObjectName("lbl_Pass")
        self.lbl_Email = QtWidgets.QLabel(self.frame)
        self.lbl_Email.setGeometry(QtCore.QRect(40, 160, 71, 31))
        self.lbl_Email.setStyleSheet("color: white;\n"
                                     "font-size: 20px;")
        self.lbl_Email.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_Email.setObjectName("lbl_Email")
        self.lbl_Alt = QtWidgets.QLabel(self.frame)
        self.lbl_Alt.setGeometry(QtCore.QRect(100, 390, 211, 61))
        self.lbl_Alt.setStyleSheet("color: white;\n"
                                   "font-size: 15px;")
        self.lbl_Alt.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Alt.setObjectName("lbl_Alt")
        self.btn_Signup = QtWidgets.QPushButton(self.frame)
        self.btn_Signup.setGeometry(QtCore.QRect(110, 460, 181, 51))
        self.btn_Signup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Signup.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_Signup.setStyleSheet("border: none;\n"
                                      "border-radius: 15px;\n"
                                      "background: #222;\n"
                                      "color: white;\n"
                                      "font-size: 25px;")
        self.btn_Signup.setObjectName("btn_Signup")
        self.btn_Login = QtWidgets.QPushButton(self.frame)
        self.btn_Login.setGeometry(QtCore.QRect(110, 330, 181, 51))
        self.btn_Login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Login.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_Login.setStyleSheet("background: 2px solid rgb(243, 76, 83);\n"
                                     "border-radius: 15px;\n"
                                     "font-size: 25px;")
        self.btn_Login.setCheckable(True)
        self.btn_Login.setObjectName("btn_Login")

        self.retranslateUi(MainWindow)
        self.txt_Email.returnPressed.connect(self.txt_Pass.setFocus)
        self.txt_Pass.returnPressed.connect(self.btn_Login.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.userFunctions(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.lbl_Pass.setText(_translate("MainWindow", "Password"))
        self.lbl_Email.setText(_translate("MainWindow", "E-Mail"))
        self.lbl_Alt.setText(_translate("MainWindow", "Don\'t have an account already?\n"
                                                      "Sign up over here!!!"))
        self.btn_Signup.setText(_translate("MainWindow", "Sign up"))
        self.btn_Login.setText(_translate("MainWindow", "Login"))

    def userFunctions(self, MainWindow):
        self.btn_Login.clicked.connect(lambda: self.loginPressed())
        self.btn_Signup.clicked.connect(lambda: self.openSignupForm())
        self.btn_Signup.clicked.connect(MainWindow.hide)

    def loginPressed(self):
        email = self.txt_Email.text()
        password = self.txt_Pass.text()
        if email != '' and password != '':
            result = verify_user(self.conn, email, password)
            if result == "Incorrect Password":
                self.createMessageBox("Invalid Password", "Please try again")
            elif result == "No Record Found":
                self.createMessageBox("Invalid User", "No User Found.\nEmail is not registered.")
            else:
                self.openMainForm(result)

    def openMainForm(self, result):
        print(result)
        self.mainform = QtWidgets.QMainWindow()
        if result[-1] == 'Customer':
            CustomerMainformGUI(self.conn, self.mainform, result[0])
        elif result[-1] == 'Seller':
            SellerMainformGUI(self.conn, self.mainform, result[0])
        self.mainform.show()

    def openSignupForm(self):
        self.mainform = QtWidgets.QMainWindow()
        CustomerSignupGUI(self.conn, self.mainform)
        self.mainform.show()

    def createMessageBox(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setWindowIcon(self.icon)
        msg.setText(message)
        msg.exec_()
