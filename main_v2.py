import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_components.gui_v2 import Ui_MainWindow


import CRUD_DB
from datetime import date, timedelta
from re import fullmatch
from worker_v2 import Worker

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.window.work_log.setReadOnly(True)
        self.window.start_work.clicked.connect(self.start_work)
        self.type_of_work = {'all': 0, 'full': 1, 'practice': 4, 'not_full': 2, 'remote': 3, 'project': 5, 'part': 7, 'season': 6 }
        self.profLevelIDs = {'director': 6, 'head_department': 5, 'Senior': 4, 'Middle': 3, 'junior': 2, 'work_spec':1}
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
        self.eng_lvl = {'родной': 8, 'свободно': 7, 'продвинутый': 6, 'выше среднего': 5, 'средний': 4, 'ниже среднего': 3, 'базовый': 2, 'не владею': 1}
        self.all_ids = []
    def start_work(self):
        self.window.start_work.setEnabled(False)
        self.worker = Worker(self.window)
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
        possible_city = CRUD_DB.get_all_cities()
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
                    self.get_hrefs(self.full_url)
                    return

    def get_hrefs(self, url):
        count_vacansies = self.worker.parse_data_vacancies(url)
        self.window.work_log.append(f'Найдено вакансий по заданным критериям: {str(count_vacansies)}')
        if int(count_vacansies) > 0:
            email = self.window.email.text()
            password = self.window.password.text()
            nameCv = self.window.cv_name.text()
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
            for result in self.worker.send_cv(email, password, addAlert, letter, eng_lvl, profCv, nameCv):
                if type(result[0]) != bool:
                    if result[0] == 'errorCv':
                        if profCv:
                            self.window.work_log.append(f'Невозможно найти резюме, которое ранее было созданно с именем: {nameCv}')
                        else:
                            self.window.work_log.append(f'Невозможно найти резюме, которое ранее было загруженно с именем: {nameCv}')
                        break
                    elif result[0] == 'AlreadySened':
                        self.window.work_log.append(f'На вакансию https://rabota.ua/{result[1]} уже был отклик')
                    else:
                        self.window.work_log.append(f'Ошибка при отправке резюме на: https://rabota.ua/{result[1]}')

                else:
                    if result[0] == True:
                        self.window.work_log.append(f'Резюме было отправлено на: https://rabota.ua/{result[1]}')
                    else:
                        self.window.work_log.append(f'Ошибка при отправке резюме на: https://rabota.ua/{result[1]}')
        else:
            self.window.work_log.append(f'Дальнейшая работа приложения невозможна')
        self.window.start_work.setEnabled(True)
        return












if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())