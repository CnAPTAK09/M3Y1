from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow
from password import Ui_MainWindow
import random

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_OK.clicked.connect(self.generation)

    def generation(self):
        s_number = '0123456789'
        s_alphabet = 'qwertyuiopasdfghjklzxcvbnQWERTYUIOPASDFGHJKLZXCVBNM'
        pas = ''
        if self.ui.cb_number.isChecked():
            for i in range(16):
                pas = pas + random.choice(s_number)
        if self.ui.cb_alphabet.isChecked():
            for i in range(16):
                pas = pas + random.choice(s_alphabet)
        if self.ui.cb_number.isChecked() and self.ui.cb_alphabet.isChecked():
            for i in range(16):
                pas = pas + random.choice(s_number + s_alphabet)
        self.ui.result.setText(pas)


app = QApplication([])
window = Widget()

window.show()
app.exec_()

