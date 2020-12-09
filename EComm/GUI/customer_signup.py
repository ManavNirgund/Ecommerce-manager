from random import randint
from passlib.hash import pbkdf2_sha256

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

from GUI.seller_signup import SellerSignupGUI
from Database.database_update import user_insert


class CustomerSignupGUI(object):
    def __init__(self, conn, MainWindow):
        self.conn = conn
        self.mainform = MainWindow
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 771)
        MainWindow.setMinimumSize(QtCore.QSize(730, 771))
        MainWindow.setMaximumSize(QtCore.QSize(771, 771))
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("./Resources/Icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(self.icon)
        MainWindow.setStyleSheet("background: white;")
        self.frm_Signup = QtWidgets.QFrame(MainWindow)
        self.frm_Signup.setGeometry(QtCore.QRect(0, 0, 731, 771))
        self.frm_Signup.setStyleSheet("background: #444")
        self.frm_Signup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_Signup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_Signup.setObjectName("frm_Signup")
        self.lbl_Depot = QtWidgets.QLabel(self.frm_Signup)
        self.lbl_Depot.setGeometry(QtCore.QRect(200, 50, 311, 111))
        self.lbl_Depot.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_Depot.setStyleSheet("font-family: Calibri Light;\n"
                                     "font-size: 50px;\n"
                                     "font-weight: bold;")
        self.lbl_Depot.setText("")
        self.lbl_Depot.setPixmap(QtGui.QPixmap("./Resources/Icons/depot.png"))
        self.lbl_Depot.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Depot.setObjectName("lbl_Depot")
        self.lbl_Depot.setScaledContents(True)
        self.txt_Pass = QtWidgets.QLineEdit(self.frm_Signup)
        self.txt_Pass.setGeometry(QtCore.QRect(270, 390, 241, 31))
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
        self.txt_SelEmail = QtWidgets.QLineEdit(self.frm_Signup)
        self.txt_SelEmail.setGeometry(QtCore.QRect(270, 310, 241, 31))
        self.txt_SelEmail.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txt_SelEmail.setStyleSheet("border: 2px solid rgb(243, 76, 83);\n"
                                        "border-radius: 15px;\n"
                                        "padding-left: 10px;\n"
                                        "padding-bottom: 1px;\n"
                                        "color: white;\n"
                                        "font-size: 20px;")
        self.txt_SelEmail.setClearButtonEnabled(True)
        self.txt_SelEmail.setObjectName("txt_SelEmail")
        self.lbl_Pass = QtWidgets.QLabel(self.frm_Signup)
        self.lbl_Pass.setGeometry(QtCore.QRect(120, 390, 111, 31))
        self.lbl_Pass.setStyleSheet("color: white;\n"
                                    "font-size: 20px;")
        self.lbl_Pass.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_Pass.setObjectName("lbl_Pass")
        self.lbl_Email = QtWidgets.QLabel(self.frm_Signup)
        self.lbl_Email.setGeometry(QtCore.QRect(120, 310, 111, 31))
        self.lbl_Email.setStyleSheet("color: white;\n"
                                     "font-size: 20px;")
        self.lbl_Email.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_Email.setObjectName("lbl_Email")
        self.lbl_Fname = QtWidgets.QLabel(self.frm_Signup)
        self.lbl_Fname.setGeometry(QtCore.QRect(110, 230, 121, 31))
        self.lbl_Fname.setStyleSheet("color: white;\n"
                                     "font-size: 20px;")
        self.lbl_Fname.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_Fname.setObjectName("lbl_Fname")
        self.txt_Fname = QtWidgets.QLineEdit(self.frm_Signup)
        self.txt_Fname.setGeometry(QtCore.QRect(270, 230, 241, 31))
        self.txt_Fname.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txt_Fname.setStyleSheet("border: 2px solid rgb(243, 76, 83);\n"
                                     "border-radius: 15px;\n"
                                     "padding-left: 10px;\n"
                                     "padding-bottom: 1px;\n"
                                     "color: white;\n"
                                     "font-size: 20px;")
        self.txt_Fname.setText("")
        self.txt_Fname.setClearButtonEnabled(True)
        self.txt_Fname.setObjectName("lineEdit")
        self.txt_PassConfirm = QtWidgets.QLineEdit(self.frm_Signup)
        self.txt_PassConfirm.setGeometry(QtCore.QRect(270, 470, 241, 31))
        self.txt_PassConfirm.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txt_PassConfirm.setStyleSheet("border: 2px solid rgb(243, 76, 83);\n"
                                           "border-radius: 15px;\n"
                                           "padding-left: 10px;\n"
                                           "padding-bottom: 1px;\n"
                                           "color: white;\n"
                                           "font-size: 20px;")
        self.txt_PassConfirm.setClearButtonEnabled(True)
        self.txt_PassConfirm.setObjectName("txt_PassConfirm")
        self.txt_PassConfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lbl_PassConfirm = QtWidgets.QLabel(self.frm_Signup)
        self.lbl_PassConfirm.setGeometry(QtCore.QRect(70, 470, 161, 31))
        self.lbl_PassConfirm.setStyleSheet("color: white;\n"
                                           "font-size: 20px;")
        self.lbl_PassConfirm.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_PassConfirm.setObjectName("lbl_PassConfirm")
        self.btn_Signup = QtWidgets.QPushButton(self.frm_Signup)
        self.btn_Signup.setGeometry(QtCore.QRect(280, 580, 191, 51))
        self.btn_Signup.setStyleSheet("border: none;\n"
                                      "border-radius: 15px;\n"
                                      "background: rgb(243, 76, 83);\n"
                                      "font-size: 20px;")
        self.btn_Signup.setObjectName("btn_Signup")
        self.btn_Seller = QtWidgets.QPushButton(self.frm_Signup)
        self.btn_Seller.setGeometry(QtCore.QRect(230, 660, 291, 51))
        self.btn_Seller.setStyleSheet("border: none;\n"
                                      "border-radius: 15px;\n"
                                      "background: #222;\n"
                                      "color: white;\n"
                                      "font-size: 20px;\n"
                                      "")
        self.btn_Seller.setObjectName("btn_Seller")

        self.retranslateUi(MainWindow)
        self.txt_Pass.returnPressed.connect(self.txt_PassConfirm.setFocus)
        self.txt_PassConfirm.returnPressed.connect(self.btn_Signup.setFocus)
        self.txt_SelEmail.returnPressed.connect(self.txt_Pass.setFocus)
        self.txt_Fname.returnPressed.connect(self.txt_SelEmail.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.userFunctions(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Customer Signup"))
        self.lbl_Pass.setText(_translate("MainWindow", "Password"))
        self.lbl_Email.setText(_translate("MainWindow", "E-Mail"))
        self.lbl_Fname.setText(_translate("MainWindow", "Full Name"))
        self.lbl_PassConfirm.setText(_translate("MainWindow", "Confirm Password"))
        self.btn_Signup.setText(_translate("MainWindow", "Signup"))
        self.btn_Seller.setText(_translate("MainWindow", "Sign up as a seller"))

    def userFunctions(self, MainWindow):
        self.btn_Signup.clicked.connect(lambda: self.signupPressed())
        self.btn_Seller.clicked.connect(lambda: self.sellerSignup())
        # self.btn_Signup.clicked.connect(MainWindow.hide)
        # self.btn_Seller.clicked.connect(MainWindow.hide)

    def signupPressed(self):
        fullname = self.txt_Fname.text()
        email = self.txt_SelEmail.text()
        password = self.txt_Pass.text()
        confirm_password = self.txt_PassConfirm.text()
        if fullname == '' or email == '' or password == '' or confirm_password == '':
            pass
        elif password != confirm_password:
            self.createMessageBox("Password Mismatch", "Password and Confirm password does not match")
        else:
            user = self.signupUser(fullname, email, password)
            if user != -1:
                self.customerFormOpen(user)

    def signupUser(self, user_name, email, password):
        user_id = randint(100000000, 999999999)
        password = pbkdf2_sha256.hash(password)
        user_info = (user_id, user_name, email, password, '', 'Customer')
        result = user_insert(self.conn, user_info)
        if result == -1:
            self.createMessageBox("Error Occured", "Signup unsuccessful.\nPlease try again!")
            return result
        return result[0]

    def customerFormOpen(self, user):
        pass

    def sellerSignup(self):
        self.mainform = QtWidgets.QMainWindow()
        SellerSignupGUI(self.conn, self.mainform)
        self.mainform.show()

    def createMessageBox(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setWindowIcon(self.icon)
        msg.setText(message)
        msg.exec()
