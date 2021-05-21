import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from ui_components.gui_v2 import Ui_MainWindow
from ui_components.login import Ui_Login
from ui_components.register import Ui_register

import CRUD_DB
from datetime import date, timedelta
from re import fullmatch, search
from worker_v2 import Worker

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from connector import *
from random import randint
from json import loads
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.window.work_log.setReadOnly(True)
        self.window.start_work.clicked.connect(self.start_work)
        self.type_of_work = {'all': 0, 'full': 1, 'practice': 4, 'not_full': 2, 'remote': 3, 'project': 5, 'part': 7, 'season': 6 }
        self.profLevelIDs = {'director': 6, 'head_department': 5, 'Senior': 4, 'Middle': 3, 'junior': 2, 'work_spec':1}
        self.eng_lvl = {'родной': 8, 'свободно': 7, 'продвинутый': 6, 'выше среднего': 5, 'средний': 4, 'ниже среднего': 3, 'базовый': 2, 'не владею': 1}
        self.parentId = {
            "HR специалисты - Бизнес-тренеры": 3,
            "IT": 1,
            "Автобизнес - Сервисное обслуживание": 33,
            "Административный персонал - Водители - Курьеры": 11,
            "Банки - Инвестиции - Лизинг": 18,
            "Бухгалтерия - Налоги - Финансы предприятия": 6,
            "Гостиницы - Рестораны - Кафе": 8,
            "Государственные учреждения - Местное самоуправление": 34, 
            "Дизайн - Графика - Фото": 15,
            "Закупки - Снабжение": 31,
            "Консалтинг - Аналитика - Аудит": 14,
            "Культура - Шоу-бизнес - Развлечения": 21,
            "Логистика - Таможня - Склад": 5,
            "Маркетинг - Реклама - PR": 24,
            "Медиа - Издательское дело": 22,
            "Медицина - Фармацевтика - Здравоохранение": 9,
            "Морские специальности": 25,
            "Наука - Образование - Перевод": 10,
            "Недвижимость": 28, 
            "Некоммерческие - Общественные организации": 13,
            "Охрана - Безопасность - Силовые структуры": 4,
            "Продажи - Клиент-менеджмент": 17,
            "Производство - Инженеры - Технологи": 32,
            "Рабочие специальности - Персонал для дома": 20,
            "Сельское хозяйство - Агробизнес - Лесное хозяйство": 26,
            "Спорт - Красота - Оздоровление": 7,
            "Страхование": 19,
            "Строительство - Архитектура": 27,
            "Студенты - Начало карьеры - Без опыта": 30,
            "Телекоммуникации - Связь": 2,
            "Топ-менеджмент - Директора": 12, 
            "Торговля": 16,
            "Туризм - Путешествия": 23,
            "Юристы, адвокаты, нотариусы": 29
        }
        self.all_ids = []
        self.synchronized_vacans()
    def synchronized_vacans(self):
        vacans = CRUD_DB.get_unsynchronized_vacans()
        if len(vacans):
            id = CRUD_DB.get_user_id()
            resp = loads(synchronized_vacans_conn(vacans, id[0]))["upd_ids"]
            print(resp)
            for id in resp:
                CRUD_DB.upd_sync(id)
    def start_work(self):
        self.window.start_work.setEnabled(False)
        # self.worker = Worker(self.window)
        self.main_url = 'https://rabota.ua/zapros'
        self.additional_url = ''
        self.window.email.setStyleSheet("")
        self.window.password.setStyleSheet("")
        self.window.name_of_work.setStyleSheet("") 
        self.window.cv_name.setStyleSheet("") 
        self.window.city.setStyleSheet("")
        is_valid_email = fullmatch(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$', self.window.email.text())
        is_valid_password = len(self.window.password.text())
        if not is_valid_email:
            self.window.email.setStyleSheet("border: 2px solid red;")
            self.window.start_work.setEnabled(True)
            self.window.email.setToolTip("Введите корректный имейл")
            self.window.email.clear()
        if is_valid_password == 0:
            self.window.password.setStyleSheet("border: 2px solid red;")
            self.window.start_work.setEnabled(True)
            self.window.password.setToolTip("Введите корректный пароль")
            self.window.password.clear()
        city = self.window.city.currentText()
        possible_city = get_cities_conn()
        selected_city = self.window.city.currentText()
        if selected_city not in possible_city:
            self.window.city.setStyleSheet("border: 2px solid red;")
            self.window.city.setToolTip("Введите корректный город поиска")
            self.window.start_work.setEnabled(True)
        else:
            if len(self.window.name_of_work.text()) < 1:
                self.window.name_of_work.setStyleSheet("border: 2px solid red;") 
                self.window.start_work.setEnabled(True)
                self.window.name_of_work.setToolTip("Введите корректную должность")
                self.window.name_of_work.clear()
            else:
                if len(self.window.cv_name.text()) < 2:
                    self.window.cv_name.setStyleSheet("border: 2px solid red;")
                    self.window.start_work.setEnabled(True)
                    self.window.cv_name.setToolTip("Введите корректное название резюме")
                else:
                    self.main_url += f'/{self.window.name_of_work.text()}'
                    selected_geo = self.window.city.currentText().lower()
                    if 'украина' in selected_geo:
                        self.main_url += f'/украина'
                    else:
                        selected_geo = selected_geo.replace(', ', '_').replace(' ', '_')
                        self.main_url += f'/{selected_geo}'

                    checked_type_of_work = [x for x in self.window.type_of_work_group.buttons() if x.isChecked()][0].objectName()
                    id_type_work = self.type_of_work[checked_type_of_work]
                    if id_type_work != 0:
                        self.additional_url = f'?scheduleId={id_type_work}'

                    period = self.window.period_search.currentText()
                    if '24' in period:
                        yesterday = date.today() - timedelta(days=1)
                        yesterday = yesterday.strftime('%d.%m.%Y')
                        if len(self.additional_url):
                            self.additional_url += f'&period=2&lastdate={yesterday}'
                        else:
                            self.additional_url = f'?period=2&lastdate={yesterday}'
                    elif '7' in period:
                        last_7 = date.today() - timedelta(days=7)
                        last_7 = last_7.strftime('%d.%m.%Y')
                        if len(self.additional_url):
                            self.additional_url += f'&period=3&lastdate={last_7}'
                        else:
                            self.additional_url = f'?period=3&lastdate={last_7}'
                    
                    parent = self.window.variants.currentText()
                    if parent != 'Все рубрики':
                        parent_id = self.parentId[parent]
                        if len(self.additional_url):
                            self.additional_url += f'&parentId={parent_id}'
                        else:
                            self.additional_url = f'?parentId={parent_id}'


                    if not self.window.checkBox.isChecked():
                        if len(self.additional_url):
                            self.additional_url += '&agency=false'
                        else:
                            self.additional_url = '?agency=false'

                    checked_pos_lvl = [x.objectName() for x in self.window.pos_level_group.buttons() if x.isChecked()]
                    if len(checked_pos_lvl):
                        for i in checked_pos_lvl:
                            id_pos_lvl = self.profLevelIDs[i]
                            if len(self.additional_url):
                                if 'profLevelIDs' in self.additional_url:
                                    self.additional_url += f'%2c{id_pos_lvl}'
                                else:
                                    self.additional_url += f'&profLevelIDs={id_pos_lvl}'
                            else:
                                self.additional_url = f'?profLevelIDs={id_pos_lvl}'
                    self.full_url = self.main_url + self.additional_url
                    self.window.work_log.append(f'Попытка подключения к {self.full_url}')
                    # conn_obj = Connector(self.full_url, self.window)
                    # connTh = Thread(target=conn_obj.get_hrefs)
                    # connTh.start()
                    # connTh.join()
                    email = self.window.email.text().strip()
                    password = self.window.password.text().strip()
                    nameCv = self.window.cv_name.text().strip()
                    if self.window.get_same.isChecked():
                        addAlert = True
                    else:
                        addAlert = False
                    letter = self.window.add_letter.toPlainText()
                    eng_lvl = self.eng_lvl[self.window.eng_lvl.currentText()]
                    if self.window.radioButton_2.isChecked():
                        profCv = True
                    else:
                        profCv = False
                    self.thread = QtCore.QThread()
                    # создадим объект для выполнения кода в другом потоке
                    self.browserHandler = Connector(self.full_url, self.window, email, password, addAlert, letter, eng_lvl, profCv, nameCv)
                    # перенесём объект в другой поток
                    self.browserHandler.moveToThread(self.thread)
                    # после чего подключим все сигналы и слоты
                    self.browserHandler.addTextLog.connect(self.append_from_thread)
                    # подключим сигнал старта потока к методу run у объекта, который должен выполнять код в другом потоке
                    self.thread.started.connect(self.browserHandler.get_hrefs)
                    # запустим поток
                    self.browserHandler.finished.connect(self.enable_start)
                    self.thread.start()
                    # self.thread.finished.connect(self.enable_start)
                    # parseTh = Thread(target=self.get_hrefs, args=(self.full_url,))
                    # parseTh.start()
                    # parseTh.join()
                    # self.get_hrefs(self.full_url)
                    print('AFTER START')
                    

                    return
    @QtCore.pyqtSlot()
    def enable_start(self):
        self.window.start_work.setEnabled(True)
        self.thread.terminate()
    @QtCore.pyqtSlot(str)
    def append_from_thread(self, message):
        self.window.work_log.append(str(message))

class Connector(QtCore.QObject):
    running = False
    finished = QtCore.pyqtSignal()
    addTextLog = QtCore.pyqtSignal(str)
    def __init__(self, url, window, email, password, addAlert, letter, eng_lvl, profCv, nameCv):
        super().__init__()
        self.window = window
        self.url = url
        self.worker = Worker(self.window)
        self.email  = email
        self.password = password
        self.addAlert = addAlert
        self.letter = letter
        self.eng_lvl = eng_lvl
        self.profCv = profCv
        self.nameCv = nameCv
    def get_hrefs(self):
        count_vacansies = self.worker.parse_data_vacancies(self.url)
        # t = Thread(target=lambda q, url: q.put(self.worker.parse_data_vacancies(url)), args=(self.que, url))
        # t.start()
        # t.join()
        # count_vacansies = self.que.get()
        self.addTextLog.emit(f'Найдено вакансий по заданным критериям: {str(count_vacansies)}')
        if int(count_vacansies) > 0:
            for result in self.worker.send_cv(self.email, self.password, self.addAlert, self.letter, self.eng_lvl, self.profCv, self.nameCv):
                if type(result[0]) != bool:
                    if result[0] == 'errorCv':
                        if self.profCv:
                            self.addTextLog.emit(f'Невозможно найти резюме, которое ранее было созданно с именем: {self.nameCv}')
                        else:
                            self.addTextLog.emit(f'Невозможно найти резюме, которое ранее было загруженно с именем: {self.nameCv}')
                        break
                    elif result[0] == 'AlreadySened':
                        self.addTextLog.emit(f'На вакансию https://rabota.ua/{result[1]} уже был отклик')
                    else:
                        self.addTextLog.emit(f'Ошибка при отправке резюме на: https://rabota.ua/{result[1]}')

                else:
                    if result[0] == True:
                        self.addTextLog.emit(f'Резюме было отправлено на: https://rabota.ua/{result[1]}')
                    else:
                        self.addTextLog.emit(f'Ошибка при отправке резюме на: https://rabota.ua/{result[1]}')
            self.addTextLog.emit(f'{"-"*30}\nРабота приложения завершена')
        else:
            self.addTextLog.emit(f'Дальнейшая работа приложения невозможна')
        self.finished.emit()

class LogIn(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.log_wind = Ui_Login()
        self.log_wind.setupUi(self)
        self.reg_wind = Register()
        self.main_window = MyWin()
        self.log_wind.go_login_2.clicked.connect(self.open_register)
        self.log_wind.login.clicked.connect(self.login)
        self.log_wind.log_email.setStyleSheet("")

    def login(self):
        
        email = self.log_wind.log_email.text().strip()
        password = self.log_wind.log_pass.text().strip()
        if ';' in email:
            self.log_wind.log_email.setStyleSheet("border: 2px solid red;")
            self.log_wind.log_email.setToolTip("Введите корректный имейл")
        elif ';' in password:
            self.log_wind.log_pass.setStyleSheet("border: 2px solid red;")
            self.log_wind.log_pass.setToolTip("Введите корректный пароль")
        else:
            resp = json.loads(get_user_conn(email, password))
            print(resp)
            # user = resp['user']
            
            if len(resp['user']) == 0:
                buttonReply = QtWidgets.QMessageBox.question(self, 'Аккаунт не зарегестрирован', "Аккаунт с такими данными для входа не был зарегестрирован",  QtWidgets.QMessageBox.Cancel)
            else:
                user_id = resp['user'][1]
                CRUD_DB.delete_ids()
                CRUD_DB.insert_id(user_id)
                if self.log_wind.remember.isChecked():
                    CRUD_DB.delete_rememeredData()
                    CRUD_DB.insert_rememeredData(email, password)
                else:
                    CRUD_DB.delete_rememeredData()
                self.main_window.show()
                self.close()

    def open_register(self):
        self.reg_wind.show()
        self.close()

class Register(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.reg_wind = Ui_register()
        self.mail_ui = MyWin()
        self.confirm_code = ''
        self.reg_wind.setupUi(self)
        self.reg_wind.go_login.clicked.connect(self.open_login)
        self.reg_wind.login.clicked.connect(self.register)

    def register(self):
        email = self.reg_wind.log_email.text().strip()
        password1 = self.reg_wind.log_pass.text().strip()
        password2 = self.reg_wind.log_pass_2.text().strip()
        self.reg_wind.log_email.setToolTip("")
        self.reg_wind.log_pass.setToolTip("")
        self.reg_wind.log_pass_2.setToolTip("")
        self.reg_wind.email_confirm.setToolTip("")
        
        self.reg_wind.log_email.setStyleSheet("")
        self.reg_wind.log_pass.setStyleSheet("")
        self.reg_wind.log_pass_2.setStyleSheet("")
        self.reg_wind.email_confirm.setStyleSheet("")

        is_valid_email = fullmatch(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$', email)
        all_emails = json.loads(get_emails_conn())['emails']
        if not self.reg_wind.email_confirm.isEnabled():
            if email not in all_emails:
                if not is_valid_email:
                    self.reg_wind.log_email.setStyleSheet("border: 2px solid red;")
                    self.reg_wind.log_email.setToolTip("Введите корректный имейл")

                else:
                    if len(password1) <= 5 or len(password1) >= 20:
                        self.reg_wind.log_pass.setStyleSheet("border: 2px solid red;")
                        self.reg_wind.log_pass.setToolTip("Длинна пароля должна быть от 5 до 20")
                    else:
                        is_valid_password = search(r'[!@#$%^&*()_+=;:?.,]',password1)
                        if is_valid_password != None:
                            self.reg_wind.log_pass.setStyleSheet("border: 2px solid red;")
                            self.reg_wind.log_pass.setToolTip(f"Пароль не должен иметь спец.символов: {is_valid_password.group(0)}")
                        else:
                            if password1 != password2:
                                self.reg_wind.log_pass.setStyleSheet("border: 2px solid red;")
                                self.reg_wind.log_pass.setToolTip("Пароли должны совпадать")

                                self.reg_wind.log_pass_2.setStyleSheet("border: 2px solid red;")
                                self.reg_wind.log_pass_2.setToolTip("Пароли должны совпадать")
                            else:
                                self.confirm_code = randint(100000000, 1000000000)
                                self.reg_wind.email_confirm.setEnabled(True)
                                res = self.send_email(self.confirm_code, email)
                                if res == 0:
                                    buttonReply = QtWidgets.QMessageBox.question(self, 'Подтверждение имейла', "На вашу почту был отправлен имейл с кодом. Введите код в после подтверждения и нажмите кнопку регистрации еще раз",  QtWidgets.QMessageBox.Cancel)
                                else:
                                    buttonReply = QtWidgets.QMessageBox.question(self, 'Подтверждение имейла', "Не удалось отправить имейл с кодом подтверждения на почту. Убедитесь в правильности написания имейла",  QtWidgets.QMessageBox.Cancel)
                                    self.reg_wind.email_confirm.setEnabled(False)
            else:
                buttonReply = QtWidgets.QMessageBox.question(self, 'Имейл занят', "Извините, но введенный вами имейл уже зарегестрирован в системе",  QtWidgets.QMessageBox.Cancel)

        else:
            code = self.reg_wind.email_confirm.text()
            try:
                code = int(code)
            except:
                self.reg_wind.email_confirm.setStyleSheet("border: 2px solid red;")
                self.reg_wind.email_confirm.setToolTip("Указан неверный код")
            if isinstance(code, int) and code == self.confirm_code:
                    resp = loads(create_user_conn(email, password1))
                    if resp['result'] == 1:
                        id = resp['id'][0]
                        CRUD_DB.delete_ids()
                        CRUD_DB.insert_id(id)
                        self.mail_ui.show()
                        self.close()
                    else:
                        buttonReply = QtWidgets.QMessageBox.question(self, 'Имейл занят', "Извините, но введенный вами имейл уже зарегестрирован в системе",  QtWidgets.QMessageBox.Cancel)

            else:
                self.reg_wind.email_confirm.setStyleSheet("border: 2px solid red;")
                self.reg_wind.email_confirm.setToolTip("Указан неверный код")
                buttonReply = QtWidgets.QMessageBox.question(self, 'Подтверждение имейла', "Код отправленный на имейл и введенный вами отличаются",  QtWidgets.QMessageBox.Cancel)

    def send_email(self, code, email):
        result = ''
        # create message object instance
        msg = MIMEMultipart()
        
        
        message = f"Привет! Спасибо за регистрацию в нашем приложении.\nОстался последний шаг - введи этот код в форме ригистрации: {code}"
        
        # setup the parameters of the message
        password = "testpassword111"
        msg['From'] = "autojobsearcher@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Подтверждение имейла"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        #create server
        server = smtplib.SMTP('smtp.gmail.com: 587')
        
        server.starttls()
        
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
        
        
        # send the message via the server.
        try:
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            result =  0
        except Exception as err:
            result =  1
        finally:
            server.quit()
            return result
            

    def open_login(self):
        self.log_window = LogIn()
        self.log_window.show()
        self.close()









if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = LogIn()
    myapp.show()
    sys.exit(app.exec_())
    # app = QtWidgets.QApplication(sys.argv)
    # myapp = MyWin()
    # myapp.show()
    # sys.exit(app.exec_())