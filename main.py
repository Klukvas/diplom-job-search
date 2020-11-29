import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_components.main_window_v1 import Ui_MainWindow


from CRUD_DB import get_filtered_cities



class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        










if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())