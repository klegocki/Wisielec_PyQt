# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WisielecWybierzTemat.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
import WisielecPokazWylosowaneHaslo
import requests

#tymaczasowy import do ułatwienia testowania, usunąc po testowaniu
import Wisielec
import random



class Ui_Form(object):

    haslo = []

    def __init__(self, gracz1, gracz2):
        self.gracz1 = gracz1
        self.gracz2 = gracz2
        print(self.gracz1.pseudonim)
        print(self.gracz2.pseudonim)
        print(self.gracz1.rola)
        print(self.gracz2.rola)


    def HaslaAPI(self, word, max_results=5):
        base_url = 'https://api.datamuse.com/words?={word}'
        params = {
            'rel_syn': word,
            'max': max_results
        }

        response = requests.get(base_url, params=params)


        if response.status_code == 200:
            odpowiedz = response.json()
            hasla = [f"{entry['word']}" for entry in odpowiedz]
            self.haslo = random.choice(hasla)
            self.zmienOkno()

        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Błąd")
            msg_box.setText("Błąd połączenia z serwerem")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
            return None




    def zmienOkno(self):
            self.window = QWidget()
            self.ui = WisielecPokazWylosowaneHaslo.Ui_Form(self.gracz1, self.gracz2, self.haslo)
            self.ui.setupUi(self.window)
            self.window.show()
            current_window = QtWidgets.QApplication.activeWindow()
            current_window.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(589, 376)
        self.skarby_button = QtWidgets.QPushButton(Form, clicked=lambda: self.HaslaAPI("Treasure"))
        self.skarby_button.setGeometry(QtCore.QRect(300, 80, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.skarby_button.setFont(font)
        self.skarby_button.setObjectName("skarby_button")
        self.piraci_button = QtWidgets.QPushButton(Form, clicked=lambda: self.HaslaAPI("Pirate"))
        self.piraci_button.setGeometry(QtCore.QRect(10, 80, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.piraci_button.setFont(font)
        self.piraci_button.setObjectName("piraci_button")
        self.labelInstrukcja = QtWidgets.QLabel(Form)
        self.labelInstrukcja.setGeometry(QtCore.QRect(190, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelInstrukcja.setFont(font)
        self.labelInstrukcja.setObjectName("labelInstrukcja")
        self.wody_button = QtWidgets.QPushButton(Form, clicked=lambda: self.HaslaAPI("Water"))
        self.wody_button.setGeometry(QtCore.QRect(10, 220, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.wody_button.setFont(font)
        self.wody_button.setObjectName("wody_button")
        self.miasta_button = QtWidgets.QPushButton(Form, clicked=lambda: self.HaslaAPI("City"))
        self.miasta_button.setEnabled(True)
        self.miasta_button.setGeometry(QtCore.QRect(300, 220, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.miasta_button.setFont(font)
        self.miasta_button.setObjectName("miasta_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.skarby_button.setText(_translate("Form", "SKARBY"))
        self.piraci_button.setText(_translate("Form", "PIRACI"))
        self.labelInstrukcja.setText(_translate("Form", "Wybierz temat"))
        self.wody_button.setText(_translate("Form", "WODY"))
        self.miasta_button.setText(_translate("Form", "MIASTA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    #usunąc po skończeniu testowania
    GraczStart1 = Wisielec.Gracz(0, 0, False, "jeden", 0)
    GraczStart2 =  Wisielec.Gracz(0, 0, False, "dwa", 0)
    ##
    ui = Ui_Form(GraczStart1,GraczStart2)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())