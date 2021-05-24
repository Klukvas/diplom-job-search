# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from Models import RememeredData
class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(321, 194)
        Login.setMinimumSize(QtCore.QSize(321, 194))
        Login.setMaximumSize(QtCore.QSize(321, 194))
        Login.setStyleSheet("font-size: 12px")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setStyleSheet("background-color: black;\n"
"color: white;\n"
"QLablel{\n"
"    background-color: rgb(255, 255, 255);\n"
"};\n"
"QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 172))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.l_email = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_email.setObjectName("l_email")
        self.verticalLayout.addWidget(self.l_email)
        self.log_email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.log_email.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 158, 2);\n"
"color: rgb(0, 0, 0)")
        self.log_email.setObjectName("log_email")
        self.verticalLayout.addWidget(self.log_email)
        self.l_pass = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_pass.setObjectName("l_pass")
        self.verticalLayout.addWidget(self.l_pass)
        self.log_pass = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.log_pass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 158, 2);\n"
"color: rgb(0, 0, 0)")
        self.log_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.log_pass.setObjectName("log_pass")
        self.verticalLayout.addWidget(self.log_pass)
        self.remember = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.remember.setObjectName("remember")
        self.verticalLayout.addWidget(self.remember)
        self.login = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.login.setStyleSheet("background-color: rgb(255, 158, 2);\n"
"margin-top:4px;\n"
"padding:2px 2px 2px 2px;\n"
"border: 1px solid rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0)")
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.go_login_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.go_login_2.setStyleSheet("background-color: rgb(255, 158, 2);\n"
"margin-top:4px;\n"
"padding:2px 2px 2px 2px;\n"
"border: 1px solid rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0)")
        self.go_login_2.setObjectName("go_login_2")
        self.verticalLayout.addWidget(self.go_login_2)
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        rememeredData = RememeredData.get_rememeredData()
        if len(rememeredData):
            self.log_email.setText(rememeredData[0])
            self.log_pass.setText(rememeredData[1])
            self.remember.setChecked(True)
    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.l_email.setText(_translate("Login", "Имейл"))
        self.l_pass.setText(_translate("Login", "Пароль"))
        self.remember.setText(_translate("Login", "Запомнить меня"))
        self.login.setText(_translate("Login", "Войти"))
        self.go_login_2.setText(_translate("Login", "Регистрация"))
        self.go_login_2.setShortcut(_translate("Login", "Ctrl+R"))
