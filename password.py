from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(275, 253)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        Form.setFont(font)
        Form.setStyleSheet("color: purple;\n"
"background-color: yellow;\n"
"border: 2px solid black;\n"
"border-radius: 5px;")
        self.result = QtWidgets.QLabel(Form)
        self.result.setGeometry(QtCore.QRect(40, 30, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result.setFont(font)
        self.result.setStyleSheet("color: purple;\n"
"background-color: black;\n"
"border: 2px solid black;\n"
"border-radius: 5px;")
        self.result.setObjectName("result")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(40, 70, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.title.setFont(font)
        self.title.setStyleSheet("color: purple;\n"
"background-color: pink;\n"
"border: 2px solid black;\n"
"border-radius: 5px;")
        self.title.setObjectName("title")
        self.cb_number = QtWidgets.QCheckBox(Form)
        self.cb_number.setGeometry(QtCore.QRect(40, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_number.setFont(font)
        self.cb_number.setStyleSheet("color: purple;\n"
"background-color: red;\n"
"border: 2px solid black;\n"
"border-radius: 5px;")
        self.cb_number.setObjectName("cb_number")
        self.cb_alphabet = QtWidgets.QCheckBox(Form)
        self.cb_alphabet.setGeometry(QtCore.QRect(40, 140, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_alphabet.setFont(font)
        self.cb_alphabet.setStyleSheet("color: purple;\n"
"background-color: red;\n"
"border: 2px solid black;\n"
"border-radius: 5px;")
        self.cb_alphabet.setObjectName("cb_alphabet")
        self.btn_OK = QtWidgets.QPushButton(Form)
        self.btn_OK.setGeometry(QtCore.QRect(80, 190, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_OK.setFont(font)
        self.btn_OK.setStyleSheet("color: purple;\n"
"background-color: red;\n"
"border: 2px solid black;\n"
"border-radius: 5px;")
        self.btn_OK.setObjectName("btn_OK")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.result.setText(_translate("Form", "Генератор паролів"))
        self.title.setText(_translate("Form", "Тут буде результат"))
        self.cb_number.setText(_translate("Form", "Використовувати числа"))
        self.cb_alphabet.setText(_translate("Form", "Використовувати алфавіт"))
        self.btn_OK.setText(_translate("Form", "Сгенерувати"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
