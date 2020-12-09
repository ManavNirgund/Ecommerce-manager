from random import randint
from passlib.hash import pbkdf2_sha256

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

from Database.database_update import user_insert


class SignupGUI(object):
    def __init__(self, conn, MainWindow):
        self.conn = conn
        self.type = "Customer"
        self.mainform = MainWindow
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(971, 770)
        MainWindow.setMinimumSize(QtCore.QSize(971, 770))
        MainWindow.setMaximumSize(QtCore.QSize(971, 770))
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("./Resources/Icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(self.icon)
        self.frm_Signup = QtWidgets.QFrame(MainWindow)
        self.frm_Signup.setGeometry(QtCore.QRect(0, 0, 971, 770))
        self.frm_Signup.setMinimumSize(QtCore.QSize(0, 0))
        self.frm_Signup.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frm_Signup.setStyleSheet("background: #444;")
        self.frm_Signup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_Signup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_Signup.setObjectName("frm_Signup")
        self.lbl_Depot = QtWidgets.QLabel(self.frm_Signup)
        self.lbl_Depot.setGeometry(QtCore.QRect(340, 60, 251, 91))
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
        self.txt_Pass.setGeometry(QtCore.QRect(380, 410, 241, 31))
        self.txt_Pass.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txt_Pass.setStyleSheet("border: 2px solid rgb(243, 76, 83);\n"
                                    "border-radius: 15px;\n"
                                    "padding-left: 10px;\n"
                                    "padding-bottom: 1px;\n"
                                    "color: white;\n"
                                    "font-size: 20px;")
        self.txt_Pass.setObjectName("txt_Pass")
        self.txt_Pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_SelEmail = QtWidgets.QLineEdit(self.frm_Signup)
        self.txt_SelEmail.setGeometry(QtCore.QRect(380, 270, 241, 31))
        self.txt_SelEmail.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txt_SelEmail.setStyleSheet("border: 2px solid rgb(243, 76, 83);\n"
                                        "border-radius: 15px;\n"
                                        "padding-left: 10px;\n"
                                        "padding-bottom: 1px;\n"
                                        "color: white;\n"
                                        "font-size: 20px;")
        self.txt_SelEmail.setObjectName("txt_SelEmail")
        self.lbl_Pass = QtWidgets.QLabel(self.frm_Signup)
        self.lbl_Pass.setGeometry(QtCore.QRect(230, 410, 111, 31))
        self.lbl_Pass.setStyleSheet("color: white;\n"
                                    "font-size: 20px;")
        self.lbl_Pass.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Pass.setObjectName("lbl_Pass")
        self.lbl_Email = QtWidgets.QLabel(self.frm_Signup)
        self.lbl_Email.setGeometry(QtCore.QRect(230, 270, 111, 31))
        self.lbl_Email.setStyleSheet("color: white;\n"
                                     "font-size: 20px;")
        self.lbl_Email.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Email.setObjectName("lbl_Email")
        self.lbl_Fname = QtWidgets.QLabel(self.frm_Signup)
        self.lbl_Fname.setGeometry(QtCore.QRect(220, 200, 121, 31))
        self.lbl_Fname.setStyleSheet("color: white;\n"
                                     "font-size: 20px;")
        self.lbl_Fname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Fname.setObjectName("lbl_Fname")
        self.txt_Fname = QtWidgets.QLineEdit(self.frm_Signup)
        self.txt_Fname.setGeometry(QtCore.QRect(380, 200, 241, 31))
        self.txt_Fname.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txt_Fname.setStyleSheet("border: 2px solid rgb(243, 76, 83);\n"
                                    "border-radius: 15px;\n"
                                    "padding-left: 10px;\n"
                                    "padding-bottom: 1px;\n"
                                    "color: white;\n"
                                    "font-size: 20px;")
        self.txt_Fname.setText("")
        self.txt_Fname.setObjectName("lineEdit")
        self.txt_PassConfirm = QtWidgets.QLineEdit(self.frm_Signup)
        self.txt_PassConfirm.setGeometry(QtCore.QRect(380, 480, 241, 31))
        self.txt_PassConfirm.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txt_PassConfirm.setStyleSheet("border: 2px solid rgb(243, 76, 83);\n"
                                           "border-radius: 15px;\n"
                                           "padding-left: 10px;\n"
                                           "padding-bottom: 1px;\n"
                                           "color: white;\n"
                                           "font-size: 20px;")
        self.txt_PassConfirm.setObjectName("txt_PassConfirm")
        self.txt_PassConfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lbl_PassConfirm = QtWidgets.QLabel(self.frm_Signup)
        self.lbl_PassConfirm.setGeometry(QtCore.QRect(180, 480, 161, 31))
        self.lbl_PassConfirm.setStyleSheet("color: white;\n"
                                           "font-size: 20px;")
        self.lbl_PassConfirm.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_PassConfirm.setObjectName("lbl_PassConfirm")
        self.btn_Signup = QtWidgets.QPushButton(self.frm_Signup)
        self.btn_Signup.setGeometry(QtCore.QRect(390, 580, 191, 51))
        self.btn_Signup.setStyleSheet("border: none;\n"
                                      "border-radius: 15px;\n"
                                      "background: rgb(243, 76, 83);\n"
                                      "font-size: 20px;")
        self.btn_Signup.setObjectName("btn_Signup")
        self.btn_Switch = QtWidgets.QPushButton(self.frm_Signup)
        self.btn_Switch.setGeometry(QtCore.QRect(340, 660, 291, 51))
        self.btn_Switch.setStyleSheet("border: none;\n"
                                      "border-radius: 15px;\n"
                                      "background: #222;\n"
                                      "color: white;\n"
                                      "font-size: 20px;")
        self.btn_Switch.setObjectName("btn_Switch")
        self.txt_Phone = QtWidgets.QLineEdit(self.frm_Signup)
        self.txt_Phone.setGeometry(QtCore.QRect(380, 340, 241, 31))
        self.txt_Phone.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txt_Phone.setStyleSheet("border: 2px solid rgb(243, 76, 83);\n"
                                     "border-radius: 15px;\n"
                                     "padding-left: 10px;\n"
                                     "padding-bottom: 1px;\n"
                                     "color: white;\n"
                                     "font-size: 20px;")
        self.txt_Phone.setObjectName("txt_Phone")
        self.lbl_Phone = QtWidgets.QLabel(self.frm_Signup)
        self.lbl_Phone.setGeometry(QtCore.QRect(210, 340, 131, 31))
        self.lbl_Phone.setStyleSheet("color: white;\n"
                                     "font-size: 20px;")
        self.lbl_Phone.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Phone.setObjectName("lbl_Phone")

        self.retranslateUi(MainWindow)
        self.txt_Fname.returnPressed.connect(self.txt_SelEmail.setFocus)
        self.txt_SelEmail.returnPressed.connect(self.txt_Phone.setFocus)
        self.txt_Phone.returnPressed.connect(self.txt_Pass.setFocus)
        self.txt_Pass.returnPressed.connect(self.txt_PassConfirm.setFocus)
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
        self.btn_Switch.setText(_translate("MainWindow", "Sign up as a seller"))
        self.lbl_Phone.setText(_translate("MainWindow", "Phone Number"))

    def userFunctions(self, MainWindow):
        self.btn_Signup.clicked.connect(lambda: self.signupPressed())
        self.btn_Switch.clicked.connect(lambda: self.switchPressed(MainWindow))
        #self.btn_Signup.clicked.connect(MainWindow.hide)

    def signupPressed(self):
        fullname = self.txt_Fname.text()
        email = self.txt_SelEmail.text()
        password = self.txt_Pass.text()
        phone = self.txt_Phone.text()
        confirm_password = self.txt_PassConfirm.text()
        if fullname == '' or email == '' or password == '' or confirm_password == '' or phone == '':
            pass
        elif password != confirm_password:
            self.createMessageBox("Password Mismatch", "Password and Confirm password does not match")
        else:
            user = self.signupUser(fullname, email, password, phone)
            if user != -1:
                self.mainformOpen(user)

    def signupUser(self, user_name, email, password, phone):
        user_id = randint(100000000, 999999999)
        password = pbkdf2_sha256.hash(password)
        user_info = (user_id, user_name, email, password, phone, self.type)
        result = user_insert(self.conn, user_info)
        if result == -1:
            self.createMessageBox("Error Occured", "Signup unsuccessful.\nPlease try again!")
            return result
        return result[0]

    def mainformOpen(self, user):
        pass

    def switchPressed(self, MainWindow):
        if self.type == 'Customer':
            self.type = 'Seller'
            MainWindow.setWindowTitle("Seller Signup")
            self.btn_Switch.setText("Sign up as a customer")
        else:
            self.type = 'Customer'
            MainWindow.setWindowTitle("Customer Signup")
            self.btn_Switch.setText("Sign up as a seller")

    def createMessageBox(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setWindowIcon(self.icon)
        msg.setText(message)
        msg.exec()
