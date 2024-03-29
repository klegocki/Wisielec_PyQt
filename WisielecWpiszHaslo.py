# -*- coding: utf-8 -*-
import os
# Form implementation generated from reading ui file 'WisielecWpiszHaslo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QImage, QBrush
from PyQt5.QtWidgets import QMessageBox
import WisielecGra



class Ui_FormHaslo(object):
    haslo = []

    def __init__(self, gracz1, gracz2):
        self.gracz1 = gracz1
        self.gracz2 = gracz2
    def dodajLitere(self, litera):
        self.haslo.append(litera)
        self.labelHaslo.setText("".join(self.haslo))

    def zatwierdzHaslo(self):
        if (len(self.haslo) > 2 and len(self.haslo) < 13):
            self.window = QtWidgets.QWidget()
            self.ui = WisielecGra.Ui_FormGra(self.haslo, self.gracz1, self.gracz2)
            self.ui.setupUi(self.window)
            self.window.show()
            current_window = QtWidgets.QApplication.activeWindow()
            current_window.close()

        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Błąd")
            msg_box.setText("Hasło musi zawierać od 3 do 12 liter.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    def cofnijLitere(self):
        if self.haslo:
            self.haslo.pop()
            self.labelHaslo.setText("".join(self.haslo))
        else:
            ''' '''
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setStyleSheet((
                "QMessageBox { background-color: white; }"
                "QMessageBox QLabel { color: black; }"
                "QMessageBox QPushButton { background-color: #4CAF50; color: white; }"
                "QMessageBox QPushButton:hover { background-color: #45a049; }"
            ))
            msg_box.setWindowTitle("Błąd")
            msg_box.setText("Wprowadź co najmniej jedną literę, aby móc cofnąć.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    def usunHaslo(self):
        self.haslo.clear()
        self.labelHaslo.setText("".join(self.haslo))

    def setupUi(self, FormHaslo):
        FormHaslo.setObjectName("FormHaslo")
        FormHaslo.setFixedSize(788,459)
        self.HVbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("V"))
        self.HVbutton.setGeometry(QtCore.QRect(330, 390, 35, 35))
        self.HVbutton.setObjectName("HVbutton")
        self.HIbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("I"))
        self.HIbutton.setGeometry(QtCore.QRect(510, 310, 35, 35))
        self.HIbutton.setObjectName("HIbutton")
        self.HMbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("M"))
        self.HMbutton.setGeometry(QtCore.QRect(480, 390, 35, 35))
        self.HMbutton.setObjectName("HMbutton")
        self.HWbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("W"))
        self.HWbutton.setGeometry(QtCore.QRect(210, 310, 35, 35))
        self.HWbutton.setObjectName("HWbutton")
        self.HLbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("L"))
        self.HLbutton.setGeometry(QtCore.QRect(570, 350, 35, 35))
        self.HLbutton.setObjectName("HLbutton")
        self.HSbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("S"))
        self.HSbutton.setGeometry(QtCore.QRect(220, 350, 35, 35))
        self.HSbutton.setObjectName("HSbutton")
        self.HQbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("Q"))
        self.HQbutton.setGeometry(QtCore.QRect(160, 310, 35, 35))
        self.HQbutton.setObjectName("HQbutton")
        self.HAbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("A"))
        self.HAbutton.setGeometry(QtCore.QRect(170, 350, 35, 35))
        self.HAbutton.setObjectName("HAbutton")
        self.HDbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("D"))
        self.HDbutton.setGeometry(QtCore.QRect(270, 350, 35, 35))
        self.HDbutton.setObjectName("HDbutton")
        self.HNbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("N"))
        self.HNbutton.setGeometry(QtCore.QRect(430, 390, 35, 35))
        self.HNbutton.setObjectName("HNbutton")
        self.HPbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("P"))
        self.HPbutton.setGeometry(QtCore.QRect(610, 310, 35, 35))
        self.HPbutton.setObjectName("HPbutton")
        self.HFbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("F"))
        self.HFbutton.setGeometry(QtCore.QRect(320, 350, 35, 35))
        self.HFbutton.setObjectName("HFbutton")
        self.HTbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("T"))
        self.HTbutton.setGeometry(QtCore.QRect(360, 310, 35, 35))
        self.HTbutton.setObjectName("HTbutton")
        self.HYbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("Y"))
        self.HYbutton.setGeometry(QtCore.QRect(410, 310, 35, 35))
        self.HYbutton.setObjectName("HYbutton")
        self.HBbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("B"))
        self.HBbutton.setGeometry(QtCore.QRect(380, 390, 35, 35))
        self.HBbutton.setObjectName("HBbutton")
        self.HUbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("U"))
        self.HUbutton.setGeometry(QtCore.QRect(460, 310, 35, 35))
        self.HUbutton.setObjectName("HUbutton")
        self.HGbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("G"))
        self.HGbutton.setGeometry(QtCore.QRect(370, 350, 35, 35))
        self.HGbutton.setObjectName("HGbutton")
        self.HKbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("K"))
        self.HKbutton.setGeometry(QtCore.QRect(520, 350, 35, 35))
        self.HKbutton.setObjectName("HKbutton")
        self.HZbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("Z"))
        self.HZbutton.setGeometry(QtCore.QRect(180, 390, 35, 35))
        self.HZbutton.setObjectName("HZbutton")
        self.HXbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("X"))
        self.HXbutton.setGeometry(QtCore.QRect(230, 390, 35, 35))
        self.HXbutton.setObjectName("HXbutton")
        self.HHbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("H"))
        self.HHbutton.setGeometry(QtCore.QRect(420, 350, 35, 35))
        self.HHbutton.setObjectName("HHbutton")
        self.HRbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("R"))
        self.HRbutton.setGeometry(QtCore.QRect(310, 310, 35, 35))
        self.HRbutton.setObjectName("HRbutton")
        self.HObutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("O"))
        self.HObutton.setGeometry(QtCore.QRect(560, 310, 35, 35))
        self.HObutton.setObjectName("HObutton")
        self.HJbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("J"))
        self.HJbutton.setGeometry(QtCore.QRect(470, 350, 35, 35))
        self.HJbutton.setObjectName("HJbutton")
        self.HEbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("E"))
        self.HEbutton.setGeometry(QtCore.QRect(260, 310, 35, 35))
        self.HEbutton.setObjectName("HEbutton")
        self.HCbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.dodajLitere("C"))
        self.HCbutton.setGeometry(QtCore.QRect(280, 390, 35, 35))
        self.HCbutton.setObjectName("HCbutton")
        self.labelInstrukcja = QtWidgets.QLabel(FormHaslo)
        self.labelInstrukcja.setGeometry(QtCore.QRect(255, 1, 270, 90))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelInstrukcja.setFont(font)
        self.labelInstrukcja.setObjectName("labelInstrukcja")
        self.labelHaslo = QtWidgets.QLabel(FormHaslo)
        self.labelHaslo.setGeometry(QtCore.QRect(130, 100, 531, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.labelHaslo.setFont(font)
        self.labelHaslo.setText("")
        self.labelHaslo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHaslo.setObjectName("labelHaslo")
        self.Cofnijbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.cofnijLitere())
        self.Cofnijbutton.setGeometry(QtCore.QRect(160, 250, 151, 41))
        self.Cofnijbutton.setObjectName("Cofnijbutton")
        self.Usunbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.usunHaslo())
        self.Usunbutton.setGeometry(QtCore.QRect(330, 250, 151, 41))
        self.Usunbutton.setObjectName("Usunbutton")
        self.Zatwierdzbutton = QtWidgets.QPushButton(FormHaslo, clicked=lambda: self.zatwierdzHaslo())
        self.Zatwierdzbutton.setGeometry(QtCore.QRect(500, 250, 151, 41))
        self.Zatwierdzbutton.setObjectName("Zatwierdzbutton")
        self.label = QtWidgets.QLabel(FormHaslo)
        self.label.setGeometry(QtCore.QRect(520, 1, 500, 90))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        if (self.gracz1.rola == False):
            self.labelInstrukcja.setText("Hasło wpisuje: "+str(self.gracz1.pseudonim))
        else:
            self.labelInstrukcja.setText("Hasło wpisuje: "+str(self.gracz2.pseudonim))

        palette = QPalette()
        background_image = QImage(os.getcwd() + "\zdjecie5.png")
        palette.setBrush(QPalette.Window, QBrush(background_image))
        FormHaslo.setPalette(palette)

        self.retranslateUi(FormHaslo)
        QtCore.QMetaObject.connectSlotsByName(FormHaslo)

    def retranslateUi(self, FormHaslo):
        _translate = QtCore.QCoreApplication.translate
        FormHaslo.setWindowTitle(_translate("FormHaslo", "Form"))
        self.HVbutton.setText(_translate("FormHaslo", "V"))
        self.HIbutton.setText(_translate("FormHaslo", "I"))
        self.HMbutton.setText(_translate("FormHaslo", "M"))
        self.HWbutton.setText(_translate("FormHaslo", "W"))
        self.HLbutton.setText(_translate("FormHaslo", "L"))
        self.HSbutton.setText(_translate("FormHaslo", "S"))
        self.HQbutton.setText(_translate("FormHaslo", "Q"))
        self.HAbutton.setText(_translate("FormHaslo", "A"))
        self.HDbutton.setText(_translate("FormHaslo", "D"))
        self.HNbutton.setText(_translate("FormHaslo", "N"))
        self.HPbutton.setText(_translate("FormHaslo", "P"))
        self.HFbutton.setText(_translate("FormHaslo", "F"))
        self.HTbutton.setText(_translate("FormHaslo", "T"))
        self.HYbutton.setText(_translate("FormHaslo", "Y"))
        self.HBbutton.setText(_translate("FormHaslo", "B"))
        self.HUbutton.setText(_translate("FormHaslo", "U"))
        self.HGbutton.setText(_translate("FormHaslo", "G"))
        self.HKbutton.setText(_translate("FormHaslo", "K"))
        self.HZbutton.setText(_translate("FormHaslo", "Z"))
        self.HXbutton.setText(_translate("FormHaslo", "X"))
        self.HHbutton.setText(_translate("FormHaslo", "H"))
        self.HRbutton.setText(_translate("FormHaslo", "R"))
        self.HObutton.setText(_translate("FormHaslo", "O"))
        self.HJbutton.setText(_translate("FormHaslo", "J"))
        self.HEbutton.setText(_translate("FormHaslo", "E"))
        self.HCbutton.setText(_translate("FormHaslo", "C"))
        #self.labelInstrukcja.setText(_translate("FormHaslo", "Haso wpisuje: "))
        self.Cofnijbutton.setText(_translate("FormHaslo", "COFNIJ"))
        self.Usunbutton.setText(_translate("FormHaslo", "USUN"))
        self.Zatwierdzbutton.setText(_translate("FormHaslo", "ZATWIERDZ"))






if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    FormHaslo = QtWidgets.QWidget()
    ui = Ui_FormHaslo()
    ui.setupUi(FormHaslo)
    FormHaslo.show()
    sys.exit(app.exec_())
