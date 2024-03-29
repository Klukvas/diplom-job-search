# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore,QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 288)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(341, 288))
        MainWindow.setMaximumSize(QtCore.QSize(341, 288))
        MainWindow.setStyleSheet("font-size: 11px")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 301, 270))
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
        self.l_pass_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_pass_2.setObjectName("l_pass_2")
        self.verticalLayout.addWidget(self.l_pass_2)
        self.log_pass_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.log_pass_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 158, 2);\n"
"color: rgb(0, 0, 0)")
        self.log_pass_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.log_pass_2.setObjectName("log_pass_2")
        self.verticalLayout.addWidget(self.log_pass_2)
        self.l_email_confirm = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_email_confirm.setObjectName("l_email_confirm")
        self.verticalLayout.addWidget(self.l_email_confirm)
        self.email_confirm = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.email_confirm.setEnabled(False)
        self.email_confirm.setStyleSheet("background-color: gray;\n"
"border: 2px solid rgb(255, 158, 2);\n"
"color: rgb(0, 0, 0)")
        self.email_confirm.setReadOnly(False)
        self.email_confirm.setObjectName("email_confirm")
        self.verticalLayout.addWidget(self.email_confirm)
        self.login = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.login.setStyleSheet("background-color: rgb(255, 158, 2);\n"
"margin-top:4px;\n"
"padding:2px 2px 2px 2px;\n"
"border: 1px solid rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0)")
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.go_login = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.go_login.setStyleSheet("background-color: rgb(255, 158, 2);\n"
"margin-top:4px;\n"
"padding:2px 2px 2px 2px;\n"
"border: 1px solid rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0)")
        self.go_login.setObjectName("go_login")
        self.verticalLayout.addWidget(self.go_login)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.l_email.setText(_translate("MainWindow", "Имейл"))
        self.l_pass.setText(_translate("MainWindow", "Пароль"))
        self.l_pass_2.setText(_translate("MainWindow", "Пароль"))
        self.l_email_confirm.setText(_translate("MainWindow", "Подтверждение почты"))
        self.login.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.go_login.setText(_translate("MainWindow", "Вход в аккаунт"))
        self.go_login.setShortcut(_translate("MainWindow", "Ctrl+R"))
