# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\customerwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class CustomerGUI(object):

    def __init__(self, conn, MainWindow):
        self.conn = conn
        self.mainform = MainWindow
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 949)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1122, 949))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Resources/Icons/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -3, 1601, 951))
        self.frame.setStyleSheet("background: #333")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frm_NavBar = QtWidgets.QFrame(self.frame)
        self.frm_NavBar.setGeometry(QtCore.QRect(12, 10, 1581, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_NavBar.sizePolicy().hasHeightForWidth())
        self.frm_NavBar.setSizePolicy(sizePolicy)
        self.frm_NavBar.setMinimumSize(QtCore.QSize(586, 0))
        self.frm_NavBar.setMaximumSize(QtCore.QSize(1865, 51))
        self.frm_NavBar.setStyleSheet("background: rgb(243, 76, 83);\n"
"")
        self.frm_NavBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_NavBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_NavBar.setObjectName("frm_NavBar")
        self.frame_7 = QtWidgets.QFrame(self.frm_NavBar)
        self.frame_7.setGeometry(QtCore.QRect(470, 5, 671, 41))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit.setGeometry(QtCore.QRect(80, 0, 591, 41))
        self.lineEdit.setStyleSheet("border-radius: 10px;\n"
"padding-left: 10px;\n"
"background: rgb(200, 200, 200);\n"
"color: #444;\n"
"font-size: 18px;\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.frame_7)
        self.comboBox.setGeometry(QtCore.QRect(7, 0, 81, 41))
        self.comboBox.setStyleSheet("border-radius: 10px;\n"
"padding-left: 10px;\n"
"background: rgb(200, 200, 200);\n"
"color: #444;\n"
"font-size: 18px;\n"
"")
        self.comboBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(640, 10, 21, 21))
        self.label_4.setStyleSheet("background: #c8c8c8;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(".\\../Resources/Icons/Search.png"))
        self.label_4.setObjectName("label_4")
        self.frame_9 = QtWidgets.QFrame(self.frm_NavBar)
        self.frame_9.setGeometry(QtCore.QRect(1150, 0, 120, 50))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_8 = QtWidgets.QFrame(self.frame_9)
        self.frame_8.setGeometry(QtCore.QRect(20, 30, 100, 3))
        self.frame_8.setStyleSheet("background: rgb(243, 76, 83);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_22.setGeometry(QtCore.QRect(13, 21, 93, 28))
        self.pushButton_22.setStyleSheet("border: none;\n"
" background: rgb(243, 76, 83);\n"
" color: #333;\n"
" font-size: 20px;")
        self.pushButton_22.setObjectName("pushButton_22")
        self.label = QtWidgets.QLabel(self.frame_9)
        self.label.setGeometry(QtCore.QRect(50, 5, 21, 25))
        self.label.setStyleSheet("background: rgb(243, 76, 83);\n"
" ")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\../Resources/Icons/Accounts.png"))
        self.label.setObjectName("label")
        self.frame_10 = QtWidgets.QFrame(self.frm_NavBar)
        self.frame_10.setGeometry(QtCore.QRect(1290, 0, 120, 50))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setGeometry(QtCore.QRect(20, 30, 100, 3))
        self.frame_11.setStyleSheet("background: rgb(243, 76, 83);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_23.setGeometry(QtCore.QRect(13, 18, 93, 31))
        self.pushButton_23.setStyleSheet("border: none;\n"
" background: rgb(243, 76, 83);\n"
" color: #333;\n"
" font-size: 20px;")
        self.pushButton_23.setObjectName("pushButton_23")
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        self.label_2.setGeometry(QtCore.QRect(50, 5, 21, 21))
        self.label_2.setStyleSheet("background: rgb(243, 76, 83);\n"
" ")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(".\\../Resources/Icons/Cart.png"))
        self.label_2.setObjectName("label_2")
        self.frame_12 = QtWidgets.QFrame(self.frm_NavBar)
        self.frame_12.setGeometry(QtCore.QRect(1430, 0, 120, 50))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setGeometry(QtCore.QRect(20, 30, 100, 3))
        self.frame_13.setStyleSheet("background: rgb(243, 76, 83);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_24.setGeometry(QtCore.QRect(13, 21, 93, 28))
        self.pushButton_24.setStyleSheet("border: none;\n"
" background: rgb(243, 76, 83);\n"
" color: #333;\n"
" font-size: 20px;")
        self.pushButton_24.setObjectName("pushButton_24")
        self.label_3 = QtWidgets.QLabel(self.frame_12)
        self.label_3.setGeometry(QtCore.QRect(50, 5, 21, 25))
        self.label_3.setStyleSheet("background: rgb(243, 76, 83);\n"
" ")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(".\\../Resources/Icons/Wishlist.png"))
        self.label_3.setObjectName("label_3")
        self.frm__StoreView = QtWidgets.QFrame(self.frame)
        self.frm__StoreView.setGeometry(QtCore.QRect(12, 60, 1581, 891))
        self.frm__StoreView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frm__StoreView.setStyleSheet("")
        self.frm__StoreView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm__StoreView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm__StoreView.setObjectName("frm__StoreView")
        self.frm_ProductPreview = QtWidgets.QFrame(self.frm__StoreView)
        self.frm_ProductPreview.setGeometry(QtCore.QRect(1, 1, 881, 881))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_ProductPreview.sizePolicy().hasHeightForWidth())
        self.frm_ProductPreview.setSizePolicy(sizePolicy)
        self.frm_ProductPreview.setMinimumSize(QtCore.QSize(0, 0))
        self.frm_ProductPreview.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frm_ProductPreview.setStyleSheet("background: #444;\n"
"")
        self.frm_ProductPreview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_ProductPreview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_ProductPreview.setObjectName("frm_ProductPreview")
        self.listWidget = QtWidgets.QListWidget(self.frm_ProductPreview)
        self.listWidget.setGeometry(QtCore.QRect(12, 12, 861, 861))
#************************************************************************************************************
        self.listWidget.setStyleSheet("color: rgb(200, 200, 200);\n"                                        #
        "font-size: 20px;\n")                                                                               #
        self.listWidget.setObjectName("listWidget")                                                         #
        self.listWidget.addItem("Search for 'addItem' and look down that's one of the solutions I guess 🤷‍")#
        self.listWidget.addItem("Or use a plain ol' scroll area")                                           #
        self.listWidget.addItem("Or use a table view like you said you did in OOPs")                        #
#************************************************************************************************************

        #******************************************************************
        self.frm_Product = QtWidgets.QFrame(self.listWidget)              #
        #******************************************************************
        self.frm_Product.setGeometry(QtCore.QRect(20, 210, 561, 190))
        self.frm_Product.setStyleSheet("")
        self.frm_Product.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_Product.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_Product.setObjectName("frm_Product")
        self.btn_ProductCost = QtWidgets.QPushButton(self.frm_Product)
        self.btn_ProductCost.setGeometry(QtCore.QRect(190, 60, 371, 47))
        self.btn_ProductCost.setStyleSheet("border: none;\n"
"background: #444;\n"
"text-align: left;\n"
"color: rgb(200, 200, 200);\n"
"font-size: 25px;\n"
"")
        self.btn_ProductCost.setObjectName("btn_ProductCost")
        self.btn_ProductName = QtWidgets.QPushButton(self.frm_Product)
        self.btn_ProductName.setGeometry(QtCore.QRect(190, 0, 371, 47))
        self.btn_ProductName.setStyleSheet("border: none;\n"
"background: #444;\n"
"text-align: left;\n"
"color: rgb(200, 200, 200);\n"
"font-size: 25px;\n"
"")
        self.btn_ProductName.setFlat(True)
        self.btn_ProductName.setObjectName("btn_ProductName")
        self.btn_Seller = QtWidgets.QPushButton(self.frm_Product)
        self.btn_Seller.setGeometry(QtCore.QRect(190, 120, 371, 47))
        self.btn_Seller.setStyleSheet("border: none;\n"
"background: #444;\n"
"text-align: left;\n"
"color: rgb(200, 200, 200);\n"
"font-size: 25px;\n"
"")
        self.btn_Seller.setObjectName("btn_Seller")
        self.btn_Image = QtWidgets.QPushButton(self.frm_Product)
        self.btn_Image.setGeometry(QtCore.QRect(0, 0, 171, 171))
        self.btn_Image.setText("")
        self.btn_Image.setObjectName("btn_Image")
        self.frm_Divider = QtWidgets.QFrame(self.frm_Product)
        self.frm_Divider.setGeometry(QtCore.QRect(50, 180, 500, 2))
        self.frm_Divider.setStyleSheet("background: rgb(243, 76, 83);")
        self.frm_Divider.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_Divider.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_Divider.setObjectName("frm_Divider")
        self.frm_ProductDescription = QtWidgets.QFrame(self.frm__StoreView)
        self.frm_ProductDescription.setGeometry(QtCore.QRect(895, 0, 681, 881))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_ProductDescription.sizePolicy().hasHeightForWidth())
        self.frm_ProductDescription.setSizePolicy(sizePolicy)
        self.frm_ProductDescription.setStyleSheet("background: #444;\n"
"")
        self.frm_ProductDescription.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_ProductDescription.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_ProductDescription.setObjectName("frm_ProductDescription")
        self.frm__StoreView.raise_()
        self.frm_NavBar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "depot"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search"))
        self.comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cloths"))
        self.pushButton_22.setText(_translate("MainWindow", "Accounts"))
        self.pushButton_23.setText(_translate("MainWindow", "Cart"))
        self.pushButton_24.setText(_translate("MainWindow", "Wishlist"))
        self.btn_ProductCost.setText(_translate("MainWindow", "Product Cost"))
        self.btn_ProductName.setText(_translate("MainWindow", "Product Name"))
        self.btn_Seller.setText(_translate("MainWindow", "Seller"))
