# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WisielecPokazWylosowaneHaslo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

import WisielecWybierzTemat
import WisielecGra

class Ui_Form(object):

    def __init__(self, gracz1, gracz2, haslo):
        self.gracz1 = gracz1
        self.gracz2 = gracz2
        self.haslo = haslo
        print(self.gracz1.pseudonim)
        print(self.gracz2.pseudonim)
        print(self.gracz1.rola)
        print(self.gracz2.rola)

    def zmienScene(self, scena):
        if (scena == "COFNIJ"):
            self.window = QWidget()
            self.ui = WisielecWybierzTemat.Ui_Form(self.gracz1, self.gracz2)
            self.ui.setupUi(self.window)
            self.window.show()
            current_window = QtWidgets.QApplication.activeWindow()
            current_window.close()
        if (scena == "ZATWIERDZ"):
            self.window = QtWidgets.QWidget()
            self.ui = WisielecGra.Ui_FormGra(self.haslo, self.gracz1, self.gracz2)
            self.ui.setupUi(self.window)
            self.window.show()
            current_window = QtWidgets.QApplication.activeWindow()
            current_window.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 250)
        self.cofnij_button = QtWidgets.QPushButton(Form, clicked=lambda: self.zmienScene("COFNIJ"))
        self.cofnij_button.setGeometry(QtCore.QRect(10, 80, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cofnij_button.setFont(font)
        self.cofnij_button.setObjectName("cofnij_button")
        self.akceptuj_button = QtWidgets.QPushButton(Form, clicked=lambda: self.zmienScene("ZATWIERDZ"))
        self.akceptuj_button.setGeometry(QtCore.QRect(300, 80, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.akceptuj_button.setFont(font)
        self.akceptuj_button.setObjectName("akceptuj_button")
        self.informacja_label = QtWidgets.QLabel(Form)
        self.informacja_label.setGeometry(QtCore.QRect(10, 20, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.informacja_label.setFont(font)
        self.informacja_label.setObjectName("informacja_label")
        self.haslo_label = QtWidgets.QLabel(Form)
        self.haslo_label.setGeometry(QtCore.QRect(160, 20, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.haslo_label.setFont(font)
        self.haslo_label.setText("")
        self.haslo_label.setObjectName("haslo_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Zatwierdź"))
        self.cofnij_button.setText(_translate("Form", "COFNIJ"))
        self.akceptuj_button.setText(_translate("Form", "AKCEPTUJ"))
        self.informacja_label.setText(_translate("Form", "Twoje hasło to:"))
        tekst_haslo= ''.join(self.haslo)
        self.haslo_label.setText(tekst_haslo)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
