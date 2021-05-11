# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_worker_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import CRUD_DB

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 241, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.login = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.login.setContentsMargins(10, 10, 10, 10)
        self.login.setObjectName("login")
        self.l_email = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_email.setObjectName("l_email")
        self.login.addWidget(self.l_email)
        self.email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.email.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.email.setObjectName("email")
        self.login.addWidget(self.email)
        self.l_password = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_password.setObjectName("l_password")
        self.login.addWidget(self.l_password)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password.setObjectName("password")
        self.login.addWidget(self.password)
        self.start_work = QtWidgets.QPushButton(self.centralwidget)
        self.start_work.setGeometry(QtCore.QRect(10, 580, 751, 51))
        self.start_work.setObjectName("start_work")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(280, 20, 471, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.work_log_lay = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.work_log_lay.setContentsMargins(0, 0, 0, 0)
        self.work_log_lay.setObjectName("work_log_lay")
        self.l_work = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.l_work.setObjectName("l_work")
        self.work_log_lay.addWidget(self.l_work)
        self.work_log = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.work_log.setObjectName("work_log")
        self.work_log_lay.addWidget(self.work_log)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 150, 241, 271))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.fields_for_search = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.fields_for_search.setContentsMargins(0, 0, 0, 0)
        self.fields_for_search.setObjectName("fields_for_search")
        self.name_of_work_lay = QtWidgets.QVBoxLayout()
        self.name_of_work_lay.setObjectName("name_of_work_lay")
        self.l_name_of_work = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.l_name_of_work.setObjectName("l_name_of_work")
        self.name_of_work_lay.addWidget(self.l_name_of_work)
        self.name_of_work = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.name_of_work.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.name_of_work.setObjectName("name_of_work")
        self.name_of_work_lay.addWidget(self.name_of_work)
        self.fields_for_search.addLayout(self.name_of_work_lay)
        self.city_ch = QtWidgets.QVBoxLayout()
        self.city_ch.setObjectName("city_ch")
        self.l_city = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.l_city.setObjectName("l_city")
        self.city_ch.addWidget(self.l_city)
        self.city = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.city.setEditable(True)
        self.city.setObjectName("city")
        self.city_ch.addWidget(self.city)
        self.fields_for_search.addLayout(self.city_ch)
        self.period_serch_lay = QtWidgets.QVBoxLayout()
        self.period_serch_lay.setObjectName("period_serch_lay")
        self.l_period_search = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.l_period_search.setObjectName("l_period_search")
        self.period_serch_lay.addWidget(self.l_period_search)
        self.period_search = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.period_search.setObjectName("period_search")
        self.period_serch_lay.addWidget(self.period_search)
        self.fields_for_search.addLayout(self.period_serch_lay)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 150, 471, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pos_level = QtWidgets.QVBoxLayout()
        self.pos_level.setContentsMargins(3, 3, 3, 3)
        self.pos_level.setObjectName("pos_level")
        self.l_pos_lvl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.l_pos_lvl.setObjectName("l_pos_lvl")
        self.pos_level.addWidget(self.l_pos_lvl)
        self.director = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.director.setObjectName("director")
        self.pos_level.addWidget(self.director)
        self.head_department = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.head_department.setObjectName("head_department")
        self.pos_level.addWidget(self.head_department)
        self.Senior = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.Senior.setObjectName("Senior")
        self.pos_level.addWidget(self.Senior)
        self.Middle = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.Middle.setObjectName("Middle")
        self.pos_level.addWidget(self.Middle)
        self.junior = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.junior.setObjectName("junior")
        self.pos_level.addWidget(self.junior)
        self.work_spec = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.work_spec.setObjectName("work_spec")

        self.pos_level_group = QtWidgets.QButtonGroup()
        self.pos_level_group.addButton(self.director)
        self.pos_level_group.addButton(self.head_department)
        self.pos_level_group.addButton(self.Senior)
        self.pos_level_group.addButton(self.Middle)
        self.pos_level_group.addButton(self.junior)
        self.pos_level_group.addButton(self.work_spec)

        self.pos_level_group.setExclusive(False)

        self.pos_level.addWidget(self.work_spec)
        self.variants_of_work = QtWidgets.QVBoxLayout()
        self.variants_of_work.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.variants_of_work.setContentsMargins(3, 16, 3, 16)
        self.variants_of_work.setSpacing(1)
        self.variants_of_work.setObjectName("variants_of_work")
        self.varianl_t = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.varianl_t.setObjectName("varianl_t")
        self.variants_of_work.addWidget(self.varianl_t)
        self.variants = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.variants.setObjectName("variants")
        self.variants_of_work.addWidget(self.variants)
        self.pos_level.addLayout(self.variants_of_work)
        self.horizontalLayout.addLayout(self.pos_level)
        self.type_of_work = QtWidgets.QVBoxLayout()
        self.type_of_work.setContentsMargins(3, 3, 3, 3)
        self.type_of_work.setObjectName("type_of_work")
        self.l_type_work = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.l_type_work.setObjectName("l_type_work")
        self.type_of_work.addWidget(self.l_type_work)
        self.all = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.all.setChecked(True)
        self.all.setObjectName("all")
        self.type_of_work.addWidget(self.all)
        self.full = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.full.setObjectName("full")
        self.type_of_work.addWidget(self.full)
        self.practice = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.practice.setObjectName("practice")
        self.type_of_work.addWidget(self.practice)
        self.not_full = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.not_full.setObjectName("not_full")
        self.type_of_work.addWidget(self.not_full)
        self.remote = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.remote.setObjectName("remote")
        self.type_of_work.addWidget(self.remote)
        self.project = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.project.setObjectName("project")
        self.type_of_work.addWidget(self.project)
        self.part = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.part.setObjectName("part")
        self.type_of_work.addWidget(self.part)
        self.season = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.season.setObjectName("season")
        self.type_of_work.addWidget(self.season)

        self.type_of_work_group = QtWidgets.QButtonGroup()
        self.type_of_work_group.addButton(self.all)
        self.type_of_work_group.addButton(self.full)
        self.type_of_work_group.addButton(self.practice)
        self.type_of_work_group.addButton(self.not_full)
        self.type_of_work_group.addButton(self.remote)
        self.type_of_work_group.addButton(self.project)
        self.type_of_work_group.addButton(self.part)
        self.type_of_work_group.addButton(self.season)

        self.line_3 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.type_of_work.addWidget(self.line_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 16, -1, 16)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.type_of_work.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.type_of_work)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 430, 184, 141))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.env_lvl_lay = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.env_lvl_lay.setContentsMargins(0, 0, 0, 0)
        self.env_lvl_lay.setObjectName("env_lvl_lay")
        self.l_env_lvl = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.l_env_lvl.setEnabled(True)
        self.l_env_lvl.setAutoFillBackground(False)
        self.l_env_lvl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.l_env_lvl.setObjectName("l_env_lvl")
        self.env_lvl_lay.addWidget(self.l_env_lvl)
        self.eng_lvl = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.eng_lvl.setObjectName("eng_lvl")
        self.env_lvl_lay.addWidget(self.eng_lvl)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.env_lvl_lay.addWidget(self.line)
        self.resend = QtWidgets.QCheckBox(self.verticalLayoutWidget_5)
        self.resend.setObjectName("resend")
        self.env_lvl_lay.addWidget(self.resend)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.env_lvl_lay.addWidget(self.line_4)
        self.get_same = QtWidgets.QCheckBox(self.verticalLayoutWidget_5)
        self.get_same.setObjectName("get_same")
        self.env_lvl_lay.addWidget(self.get_same)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(220, 430, 171, 141))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.cv_type_lay = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.cv_type_lay.setContentsMargins(0, 0, 0, 0)
        self.cv_type_lay.setObjectName("cv_type_lay")
        self.cv_past = QtWidgets.QRadioButton(self.verticalLayoutWidget_6)
        self.cv_past.setObjectName("cv_past")
        self.cv_type_lay.addWidget(self.cv_past)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_6)
        self.radioButton_2.setObjectName("radioButton_2")
        self.cv_type_lay.addWidget(self.radioButton_2)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_6)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.cv_type_lay.addWidget(self.line_2)
        self.l_cv_type = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.l_cv_type.setObjectName("l_cv_type")
        self.cv_type_lay.addWidget(self.l_cv_type)
        self.cv_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.cv_name.setObjectName("cv_name")
        self.cv_type_lay.addWidget(self.cv_name)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(400, 430, 351, 141))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.l_add_letter = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.l_add_letter.setObjectName("l_add_letter")
        self.verticalLayout_2.addWidget(self.l_add_letter)
        self.add_letter = QtWidgets.QTextEdit(self.verticalLayoutWidget_7)
        self.add_letter.setObjectName("add_letter")
        self.verticalLayout_2.addWidget(self.add_letter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        all_periods = CRUD_DB.get_all_periods()
        self.period_search.addItems(all_periods)

        all_variants = CRUD_DB.get_all_headings()
        self.variants.addItems(all_variants)

        all_cities = CRUD_DB.get_all_cities()
        self.city.addItems(all_cities)

        all_engLvls = CRUD_DB.get_all_engLvls()
        self.eng_lvl.addItems(all_engLvls)

        self.radioButton_2.setChecked(True)













    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.l_email.setText(_translate("MainWindow", "Email"))
        self.l_password.setText(_translate("MainWindow", "Password"))
        self.start_work.setText(_translate("MainWindow", "Начать работу"))
        self.l_work.setText(_translate("MainWindow", "Отчётность работы приложения"))
        self.l_name_of_work.setText(_translate("MainWindow", "Название должности"))
        self.l_city.setText(_translate("MainWindow", "Город поиска"))
        self.l_period_search.setText(_translate("MainWindow", "Период поиска"))
        self.l_pos_lvl.setText(_translate("MainWindow", "Уровень должности:"))
        self.director.setText(_translate("MainWindow", "Топ менеджер / директор"))
        self.head_department.setText(_translate("MainWindow", "Руководитель отдела"))
        self.Senior.setText(_translate("MainWindow", "Старший специалист"))
        self.Middle.setText(_translate("MainWindow", "Специалист"))
        self.junior.setText(_translate("MainWindow", "Специалист начального уровня"))
        self.work_spec.setText(_translate("MainWindow", "Рабочие специальности"))
        self.varianl_t.setText(_translate("MainWindow", "Рубрика"))
        self.l_type_work.setText(_translate("MainWindow", "Вид занятости:"))
        self.all.setText(_translate("MainWindow", "Все виды"))
        self.full.setText(_translate("MainWindow", "Полная занятость"))
        self.practice.setText(_translate("MainWindow", "Стажировка / практика"))
        self.not_full.setText(_translate("MainWindow", "Неполная занятость"))
        self.remote.setText(_translate("MainWindow", "Удаленная работа"))
        self.project.setText(_translate("MainWindow", "Проектная работа"))
        self.part.setText(_translate("MainWindow", "Посменная работа"))
        self.season.setText(_translate("MainWindow", "Сезонная / временная работа"))
        self.checkBox.setText(_translate("MainWindow", "Показывать вакансии агентств"))
        self.l_env_lvl.setText(_translate("MainWindow", "Уровень английского"))
        self.resend.setText(_translate("MainWindow", "Отправлять резюме повторно "))
        self.get_same.setText(_translate("MainWindow", "Получать схожие ваканси"))
        self.cv_past.setText(_translate("MainWindow", "Ранее отправленное резюме"))
        self.radioButton_2.setText(_translate("MainWindow", "Резюме созданное на сайте"))
        self.l_cv_type.setText(_translate("MainWindow", "Название резюме"))
        self.l_add_letter.setText(_translate("MainWindow", "Сопроводительное письмо"))
