import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_components.main_window_v1 import Ui_MainWindow


from CRUD_DB import get_filtered_cities

from re import fullmatch

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.window.start_work.clicked.connect(self.start_work)

    def start_work(self):
        self.window.email.setStyleSheet("")
        self.window.password.setStyleSheet("")
        self.window.position.setStyleSheet("") 
        is_valid_email = fullmatch(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$', self.window.email.text())
        if not is_valid_email:
            self.window.email.setStyleSheet("border: 2px solid red;") 
            self.window.email.setToolTip("Введите корректный имейл")
            self.window.email.clear()
        else:
            is_valid_password = len(self.window.password.text().strip())
            if not is_valid_password >= 3:
                self.window.password.setStyleSheet("border: 2px solid red;") 
                self.window.password.setToolTip("Введите корректный пароль")
                self.window.password.clear()
            else:
                is_valid_position = len(self.window.position.text().strip())
                if not is_valid_position >= 2:
                    self.window.position.setStyleSheet("border: 2px solid red;") 
                    self.window.position.setToolTip("Введите корректную должность")
                    self.window.position.clear()
                else:
                    #Начинать работу селениума
                    pass







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())