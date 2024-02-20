# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WisielecGra.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QBrush, QImage
from PyQt5.QtWidgets import QMessageBox
import os
import Wisielec

class Ui_FormGra(object):
    licznik_bledow = 0
    GlowneOknoo = 0
    haslo_zgadnij = []
    obiekt_haslo = []
    uzyte_litery = []
    def __init__(self,haslo,gracz1,gracz2):
        self.gracz1 = gracz1
        self.gracz2 = gracz2
        self.haslo = haslo
        self.temp_haslo = self.haslo
        self.haslo = [char for char in self.haslo if char != " "]
        self.haslo_zgadnij = ['_' for _ in range(len(self.haslo))]

    def dodajLitere(self, litera):


        if self.usunLitere(litera):
            self.uzyte_litery.append(litera)
            if (self.licznik_bledow != 10):
                zgadles = False
                for j in range(len(self.haslo)):
                    if (self.haslo[j] == litera):

                        zgadles = True
                        self.obiekt_haslo[j].show()
                        self.obiekt_haslo[j].setText(self.haslo[j])
                        self.haslo_zgadnij[j] = self.haslo[j]
                if (zgadles == False):
                    self.licznik_bledow += 1
                    if self.licznik_bledow == 1:
                        self.linia1.show()
                    if self.licznik_bledow == 2:
                        self.line2.show()
                    if self.licznik_bledow == 3:
                        self.line3.show()
                    if self.licznik_bledow == 4:
                        self.line4.show()
                    if self.licznik_bledow == 5:
                        self.line5.show()
                        self.label.show()
                    if self.licznik_bledow == 6:
                        self.line51.show()
                        self.line52.show()
                        self.line53.show()
                    if self.licznik_bledow == 7:
                        self.line6.show()
                    if self.licznik_bledow == 8:
                        self.line7.show()
                    if self.licznik_bledow == 9:
                        self.line8.show()
                    if self.licznik_bledow == 10:
                        self.line8_2.show()
                if (self.haslo == self.haslo_zgadnij):
                    self.haslo_zgadnij.clear()
                    self.haslo.clear()
                    self.temp_haslo.clear()
                    self.uzyte_litery.clear()
                    self.obiekt_haslo.clear()
                    self.licznik_bledow = 0
                    if(self.gracz1.rola == True):
                        self.gracz2.przegrane += 1
                        self.gracz1.wygrane += 1
                    else:
                        self.gracz1.przegrane += 1
                        self.gracz2.wygrane += 1
                    wynik_gracza_1 = "Pseudonim: "+str(self.gracz1.pseudonim)+"\nWygrane: "+str(self.gracz1.wygrane)+"\nPrzegrane: "+str(self.gracz1.przegrane)
                    wynik_gracza_2 = "Pseudonim: " + str(self.gracz2.pseudonim) + "\nWygrane: " + str(self.gracz2.wygrane) + "\nPrzegrane: " + str(self.gracz2.przegrane)
                    with open(os.path.join(os.getcwd(), str(self.gracz1.pseudonim)+".txt"),"w") as file:
                        file.write(wynik_gracza_1)
                    with open(os.path.join(os.getcwd(), str(self.gracz2.pseudonim)+".txt"),"w") as file2:
                        file2.write(wynik_gracza_2)
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Warning)
                    msg_box.setWindowTitle("Wynik")
                    msg_box.setText("Zgadujący wygrał.")
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec_()
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Wisielec.Ui_MainWindow(self.gracz1, self.gracz2)
                    self.ui.setupUi(self.window)
                    self.window.show()
                    current_window = QtWidgets.QApplication.activeWindow()
                    current_window.close()





                if (self.licznik_bledow == 10):
                    self.haslo_zgadnij.clear()
                    self.temp_haslo.clear()
                    self.obiekt_haslo.clear()
                    self.uzyte_litery.clear()
                    msg_box2 = QMessageBox()
                    msg_box2.setIcon(QMessageBox.Warning)
                    msg_box2.setWindowTitle("Wynik")
                    cale_haslo = ''.join(self.haslo)
                    msg_box2.setText("Zgadujący przegrał. Hasło to: " + cale_haslo)
                    self.haslo.clear()
                    if(self.gracz1.rola == True):
                        self.gracz1.przegrane += 1
                        self.gracz2.wygrane += 1
                    else:
                        self.gracz2.przegrane += 1
                        self.gracz1.wygrane +=  1
                    msg_box2.setStandardButtons(QMessageBox.Ok)
                    wynik_gracza_1 = "Pseudonim: "+str(self.gracz1.pseudonim)+"\nWygrane: "+str(self.gracz1.wygrane)+"\nPrzegrane: "+str(self.gracz1.przegrane)
                    wynik_gracza_2 = "Pseudonim: " + str(self.gracz2.pseudonim) + "\nWygrane: " + str(self.gracz2.wygrane) + "\nPrzegrane: " + str(self.gracz2.przegrane)
                    with open(os.path.join(os.getcwd(), str(self.gracz1.pseudonim)+".txt"),"w") as file:
                        file.write(wynik_gracza_1)
                    with open(os.path.join(os.getcwd(), str(self.gracz2.pseudonim)+".txt"),"w") as file2:
                        file2.write(wynik_gracza_2)
                    msg_box2.exec_()
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Wisielec.Ui_MainWindow(self.gracz1, self.gracz2)
                    self.ui.setupUi(self.window)
                    self.window.show()
                    current_window = QtWidgets.QApplication.activeWindow()
                    current_window.close()

    def usunLitere(self, litera):
        for i in range(len(self.uzyte_litery)):
            if litera == self.uzyte_litery[i]:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle("Błąd")
                msg_box.setText("Już użyłeś tej litery!")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
                return False
        return True

    def setupUi(self, FormGra):
        FormGra.setObjectName("FormGra")
        FormGra.setFixedSize(1127, 621)
        self.linia1 = QtWidgets.QFrame(FormGra)
        self.linia1.setGeometry(QtCore.QRect(600, 460, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.linia1.setFont(font)
        self.linia1.setLineWidth(5)
        self.linia1.setMidLineWidth(0)
        self.linia1.setFrameShape(QtWidgets.QFrame.HLine)
        self.linia1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.linia1.setObjectName("linia1")
        self.linia1.hide()
        self.line2 = QtWidgets.QFrame(FormGra)
        self.line2.setGeometry(QtCore.QRect(700, 150, 20, 351))
        self.line2.setLineWidth(5)
        self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.line2.hide()
        self.line3 = QtWidgets.QFrame(FormGra)
        self.line3.setGeometry(QtCore.QRect(660, 140, 351, 16))
        self.line3.setLineWidth(5)
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")
        self.line3.hide()
        self.line4 = QtWidgets.QFrame(FormGra)
        self.line4.setGeometry(QtCore.QRect(890, 150, 16, 61))
        self.line4.setLineWidth(5)
        self.line4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line4.setObjectName("line4")
        self.line4.hide()
        self.line5 = QtWidgets.QDial(FormGra)
        self.line5.setGeometry(QtCore.QRect(850, 200, 91, 71))
        self.line5.setMinimum(0)
        self.line5.setMaximum(360)
        self.line5.setProperty("value", 360)
        self.line5.setSliderPosition(360)
        self.line5.setTracking(False)
        self.line5.setObjectName("line5")
        self.line5.hide()
        self.line8 = QtWidgets.QLabel(FormGra)
        self.line8.setGeometry(QtCore.QRect(873, 360, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.line8.setFont(font)
        self.line8.setObjectName("line8")
        self.line8.hide()
        self.line6 = QtWidgets.QLabel(FormGra)
        self.line6.setGeometry(QtCore.QRect(872, 270, 31, 61))

        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.line6.setFont(font)
        self.line6.setObjectName("line6")
        self.line6.hide()
        self.line7 = QtWidgets.QLabel(FormGra)
        self.line7.setGeometry(QtCore.QRect(891, 270, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.line7.setFont(font)
        self.line7.setObjectName("line7")
        self.line7.hide()
        self.line8_2 = QtWidgets.QLabel(FormGra)
        self.line8_2.setGeometry(QtCore.QRect(890, 360, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.line8_2.setFont(font)
        self.line8_2.setObjectName("line8_2")
        self.line8_2.hide()
        self.line53 = QtWidgets.QLabel(FormGra)
        self.line53.setGeometry(QtCore.QRect(880, 320, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.line53.setFont(font)
        self.line53.setObjectName("line53")
        self.line53.hide()
        self.line52 = QtWidgets.QLabel(FormGra)
        self.line52.setGeometry(QtCore.QRect(880, 290, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.line52.setFont(font)
        self.line52.setObjectName("line52")
        self.line52.hide()
        self.line51 = QtWidgets.QLabel(FormGra)
        self.line51.setGeometry(QtCore.QRect(880, 250, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.line51.setFont(font)
        self.line51.setObjectName("line51")
        self.line51.hide()
        self.label = QtWidgets.QLabel(FormGra)
        self.label.setGeometry(QtCore.QRect(885, 220, 41, 16))
        self.label.setObjectName("label")
        self.label.hide()
        self.Qbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("Q"))
        self.Qbutton.setGeometry(QtCore.QRect(100, 310, 35, 35))
        self.Qbutton.setObjectName("Qbutton")
        self.Wbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("W"))
        self.Wbutton.setGeometry(QtCore.QRect(150, 310, 35, 35))
        self.Wbutton.setObjectName("Wbutton")
        self.Ebutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("E"))
        self.Ebutton.setGeometry(QtCore.QRect(200, 310, 35, 35))
        self.Ebutton.setObjectName("Ebutton")
        self.Rbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("R"))
        self.Rbutton.setGeometry(QtCore.QRect(250, 310, 35, 35))
        self.Rbutton.setObjectName("Rbutton")
        self.Tbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("T"))
        self.Tbutton.setGeometry(QtCore.QRect(300, 310, 35, 35))
        self.Tbutton.setObjectName("Tbutton")
        self.Pbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("P"))
        self.Pbutton.setGeometry(QtCore.QRect(550, 310, 35, 35))
        self.Pbutton.setObjectName("Pbutton")
        self.Ubutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("U"))
        self.Ubutton.setGeometry(QtCore.QRect(400, 310, 35, 35))
        self.Ubutton.setObjectName("Ubutton")
        self.Ibutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("I"))
        self.Ibutton.setGeometry(QtCore.QRect(450, 310, 35, 35))
        self.Ibutton.setObjectName("Ibutton")
        self.Obutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("O"))
        self.Obutton.setGeometry(QtCore.QRect(500, 310, 35, 35))
        self.Obutton.setObjectName("Obutton")
        self.Ybutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("Y"))
        self.Ybutton.setGeometry(QtCore.QRect(350, 310, 35, 35))
        self.Ybutton.setObjectName("Ybutton")
        self.Gbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("G"))
        self.Gbutton.setGeometry(QtCore.QRect(310, 350, 35, 35))
        self.Gbutton.setObjectName("Gbutton")
        self.Sbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("S"))
        self.Sbutton.setGeometry(QtCore.QRect(160, 350, 35, 35))
        self.Sbutton.setObjectName("Sbutton")
        self.Dbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("D"))
        self.Dbutton.setGeometry(QtCore.QRect(210, 350, 35, 35))
        self.Dbutton.setObjectName("Dbutton")
        self.Hbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("H"))
        self.Hbutton.setGeometry(QtCore.QRect(360, 350, 35, 35))
        self.Hbutton.setObjectName("Hbutton")
        self.Jbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("J"))
        self.Jbutton.setGeometry(QtCore.QRect(410, 350, 35, 35))
        self.Jbutton.setObjectName("Jbutton")
        self.Kbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("K"))
        self.Kbutton.setGeometry(QtCore.QRect(460, 350, 35, 35))
        self.Kbutton.setObjectName("Kbutton")
        self.Fbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("F"))
        self.Fbutton.setGeometry(QtCore.QRect(260, 350, 35, 35))
        self.Fbutton.setObjectName("Fbutton")
        self.Lbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("L"))
        self.Lbutton.setGeometry(QtCore.QRect(510, 350, 35, 35))
        self.Lbutton.setObjectName("Lbutton")
        self.Abutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("A"))
        self.Abutton.setGeometry(QtCore.QRect(110, 350, 35, 35))
        self.Abutton.setObjectName("Abutton")
        self.Mbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("M"))
        self.Mbutton.setGeometry(QtCore.QRect(420, 390, 35, 35))
        self.Mbutton.setObjectName("Mbutton")
        self.Zbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("Z"))
        self.Zbutton.setGeometry(QtCore.QRect(120, 390, 35, 35))
        self.Zbutton.setObjectName("Zbutton")
        self.Xbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("X"))
        self.Xbutton.setGeometry(QtCore.QRect(170, 390, 35, 35))
        self.Xbutton.setObjectName("Xbutton")
        self.Cbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("C"))
        self.Cbutton.setGeometry(QtCore.QRect(220, 390, 35, 35))
        self.Cbutton.setObjectName("Cbutton")
        self.Vbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("V"))
        self.Vbutton.setGeometry(QtCore.QRect(270, 390, 35, 35))
        self.Vbutton.setObjectName("Vbutton")
        self.Nbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("N"))
        self.Nbutton.setGeometry(QtCore.QRect(370, 390, 35, 35))
        self.Nbutton.setObjectName("Nbutton")
        self.Bbutton = QtWidgets.QPushButton(FormGra, clicked = lambda: self.dodajLitere("B"))
        self.Bbutton.setGeometry(QtCore.QRect(320, 390, 35, 35))
        self.Bbutton.setObjectName("Bbutton")
        self.haslo1 = QtWidgets.QLabel(FormGra)
        self.haslo1.setGeometry(QtCore.QRect(110, 220, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo1.setFont(font)
        self.haslo1.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo1.setObjectName("haslo1")
        self.haslo1.hide()
        self.haslo2 = QtWidgets.QLabel(FormGra)
        self.haslo2.setGeometry(QtCore.QRect(150, 220, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo2.setFont(font)
        self.haslo2.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo2.setObjectName("haslo2")
        self.haslo2.hide()
        self.haslo3 = QtWidgets.QLabel(FormGra)
        self.haslo3.setGeometry(QtCore.QRect(190, 220, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo3.setFont(font)
        self.haslo3.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo3.setObjectName("haslo3")
        self.haslo3.hide()
        self.haslo4 = QtWidgets.QLabel(FormGra)
        self.haslo4.setGeometry(QtCore.QRect(230, 220, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo4.setFont(font)
        self.haslo4.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo4.setObjectName("haslo4")
        self.haslo4.hide()
        self.haslo5 = QtWidgets.QLabel(FormGra)
        self.haslo5.setGeometry(QtCore.QRect(270, 220, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo5.setFont(font)
        self.haslo5.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo5.setObjectName("haslo5")
        self.haslo5.hide()
        self.haslo6 = QtWidgets.QLabel(FormGra)
        self.haslo6.setGeometry(QtCore.QRect(310, 220, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo6.setFont(font)
        self.haslo6.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo6.setObjectName("haslo6")
        self.haslo6.hide()
        self.haslo7 = QtWidgets.QLabel(FormGra)
        self.haslo7.setGeometry(QtCore.QRect(350, 220, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo7.setFont(font)
        self.haslo7.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo7.setObjectName("haslo7")
        self.haslo7.hide()
        self.haslo8 = QtWidgets.QLabel(FormGra)
        self.haslo8.setGeometry(QtCore.QRect(390, 220, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo8.setFont(font)
        self.haslo8.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo8.setObjectName("haslo8")
        self.haslo8.hide()
        self.haslo9 = QtWidgets.QLabel(FormGra)
        self.haslo9.setGeometry(QtCore.QRect(430, 220, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo9.setFont(font)
        self.haslo9.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo9.setObjectName("haslo9")
        self.haslo9.hide()
        self.haslo10 = QtWidgets.QLabel(FormGra)
        self.haslo10.setGeometry(QtCore.QRect(470, 220, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo10.setFont(font)
        self.haslo10.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo10.setObjectName("haslo10")
        self.haslo10.hide()
        self.haslo11 = QtWidgets.QLabel(FormGra)
        self.haslo11.setGeometry(QtCore.QRect(510, 220, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo11.setFont(font)
        self.haslo11.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo11.setObjectName("haslo11")
        self.haslo11.hide()
        self.haslo12 = QtWidgets.QLabel(FormGra)
        self.haslo12.setGeometry(QtCore.QRect(550, 220, 31, 41))

        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo12.setFont(font)
        self.haslo12.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo12.setObjectName("haslo12")
        self.haslo12.hide()
        self.haslo1_2 = QtWidgets.QLabel(FormGra)
        self.haslo1_2.setGeometry(QtCore.QRect(110, 210, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo1_2.setFont(font)
        self.haslo1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo1_2.setObjectName("haslo1_2")
        self.haslo2_2 = QtWidgets.QLabel(FormGra)
        self.haslo2_2.setGeometry(QtCore.QRect(150, 210, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo2_2.setFont(font)
        self.haslo2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo2_2.setObjectName("haslo2_2")
        self.haslo6_2 = QtWidgets.QLabel(FormGra)
        self.haslo6_2.setGeometry(QtCore.QRect(310, 210, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo6_2.setFont(font)
        self.haslo6_2.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo6_2.setObjectName("haslo6_2")
        self.haslo12_2 = QtWidgets.QLabel(FormGra)
        self.haslo12_2.setGeometry(QtCore.QRect(550, 210, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo12_2.setFont(font)
        self.haslo12_2.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo12_2.setObjectName("haslo12_2")
        self.haslo7_2 = QtWidgets.QLabel(FormGra)
        self.haslo7_2.setGeometry(QtCore.QRect(350, 210, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo7_2.setFont(font)
        self.haslo7_2.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo7_2.setObjectName("haslo7_2")
        self.haslo10_2 = QtWidgets.QLabel(FormGra)
        self.haslo10_2.setGeometry(QtCore.QRect(470, 210, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo10_2.setFont(font)
        self.haslo10_2.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo10_2.setObjectName("haslo10_2")
        self.haslo4_2 = QtWidgets.QLabel(FormGra)
        self.haslo4_2.setGeometry(QtCore.QRect(230, 210, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo4_2.setFont(font)
        self.haslo4_2.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo4_2.setObjectName("haslo4_2")
        self.haslo5_2 = QtWidgets.QLabel(FormGra)
        self.haslo5_2.setGeometry(QtCore.QRect(270, 210, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo5_2.setFont(font)
        self.haslo5_2.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo5_2.setObjectName("haslo5_2")
        self.haslo9_2 = QtWidgets.QLabel(FormGra)
        self.haslo9_2.setGeometry(QtCore.QRect(430, 210, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo9_2.setFont(font)
        self.haslo9_2.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo9_2.setObjectName("haslo9_2")
        self.haslo8_2 = QtWidgets.QLabel(FormGra)
        self.haslo8_2.setGeometry(QtCore.QRect(390, 210, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo8_2.setFont(font)
        self.haslo8_2.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo8_2.setObjectName("haslo8_2")
        self.haslo11_2 = QtWidgets.QLabel(FormGra)
        self.haslo11_2.setGeometry(QtCore.QRect(510, 210, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo11_2.setFont(font)
        self.haslo11_2.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo11_2.setObjectName("haslo11_2")
        self.haslo3_2 = QtWidgets.QLabel(FormGra)
        self.haslo3_2.setGeometry(QtCore.QRect(190, 210, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.haslo3_2.setFont(font)
        self.haslo3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.haslo3_2.setObjectName("haslo3_2")
        self.haslo1.setStyleSheet("color: white;")
        self.haslo2.setStyleSheet("color: white;")
        self.haslo3.setStyleSheet("color: white;")
        self.haslo4.setStyleSheet("color: white;")
        self.haslo5.setStyleSheet("color: white;")
        self.haslo6.setStyleSheet("color: white;")
        self.haslo7.setStyleSheet("color: white;")
        self.haslo8.setStyleSheet("color: white;")
        self.haslo9.setStyleSheet("color: white;")
        self.haslo10.setStyleSheet("color: white;")
        self.haslo11.setStyleSheet("color: white;")
        self.haslo1_2.setStyleSheet("color: white;")
        self.haslo2_2.setStyleSheet("color: white;")
        self.haslo3_2.setStyleSheet("color: white;")
        self.haslo11_2.setStyleSheet("color: white;")
        self.haslo4_2.setStyleSheet("color: white;")
        self.haslo5_2.setStyleSheet("color: white;")
        self.haslo6_2.setStyleSheet("color: white;")
        self.haslo7_2.setStyleSheet("color: white;")
        self.haslo8_2.setStyleSheet("color: white;")
        self.haslo9_2.setStyleSheet("color: white;")
        self.haslo10_2.setStyleSheet("color: white;")
        self.haslo12_2.setStyleSheet("color: white;")
        self.haslo12.setStyleSheet("color: white;")
        self.line8.setStyleSheet("color: white;")
        self.line6.setStyleSheet("color: white;")
        self.line7.setStyleSheet("color: white;")
        self.line51.setStyleSheet("color: white;")
        self.line8_2.setStyleSheet("color: white;")
        self.line53.setStyleSheet("color: white;")
        self.line52.setStyleSheet("color: white;")


        for i in range(len(self.temp_haslo)):
            k = -1
            if self.temp_haslo[i] == " ":
                k = 0
            if( k == 0 ):
                continue
            if(i == 0):
                self.haslo1.show()
                self.obiekt_haslo.append(self.haslo1_2)
            if(i == 1):
                self.haslo2.show()
                self.obiekt_haslo.append(self.haslo2_2)
            if(i == 2):
                self.haslo3.show()
                self.obiekt_haslo.append(self.haslo3_2)
            if(i == 3):
                self.haslo4.show()
                self.obiekt_haslo.append(self.haslo4_2)
            if(i == 4):
                self.haslo5.show()
                self.obiekt_haslo.append(self.haslo5_2)
            if(i == 5):
                self.haslo6.show()
                self.obiekt_haslo.append(self.haslo6_2)
            if(i == 6):
                self.haslo7.show()
                self.obiekt_haslo.append(self.haslo7_2)
            if(i == 7):
                self.haslo8.show()
                self.obiekt_haslo.append(self.haslo8_2)
            if(i == 8):
                self.haslo9.show()
                self.obiekt_haslo.append(self.haslo9_2)
            if(i == 9):
                self.haslo10.show()
                self.obiekt_haslo.append(self.haslo10_2)
            if(i == 10):
                self.haslo11.show()
                self.obiekt_haslo.append(self.haslo11_2)
            if(i == 11):
                self.haslo12.show()
                self.obiekt_haslo.append(self.haslo12_2)

        palette = QPalette()
        background_image = QImage(os.getcwd() + "\zdjecie6.png")
        palette.setBrush(QPalette.Window, QBrush(background_image))
        FormGra.setPalette(palette)

        self.retranslateUi(FormGra)
        QtCore.QMetaObject.connectSlotsByName(FormGra)

    def retranslateUi(self, FormGra):
        _translate = QtCore.QCoreApplication.translate
        FormGra.setWindowTitle(_translate("FormGra", "Form"))
        self.line8.setText(_translate("FormGra", "/ "))
        self.line6.setText(_translate("FormGra", "/ "))
        self.line7.setText(_translate("FormGra", "\\"))
        self.line8_2.setText(_translate("FormGra", "\\"))
        self.line53.setText(_translate("FormGra", "|"))
        self.line52.setText(_translate("FormGra", "|"))
        self.line51.setText(_translate("FormGra", "|"))
        self.label.setText(_translate("FormGra", "X     X"))
        self.Qbutton.setText(_translate("FormGra", "Q"))
        self.Wbutton.setText(_translate("FormGra", "W"))
        self.Ebutton.setText(_translate("FormGra", "E"))
        self.Rbutton.setText(_translate("FormGra", "R"))
        self.Tbutton.setText(_translate("FormGra", "T"))
        self.Pbutton.setText(_translate("FormGra", "P"))
        self.Ubutton.setText(_translate("FormGra", "U"))
        self.Ibutton.setText(_translate("FormGra", "I"))
        self.Obutton.setText(_translate("FormGra", "O"))
        self.Ybutton.setText(_translate("FormGra", "Y"))
        self.Gbutton.setText(_translate("FormGra", "G"))
        self.Sbutton.setText(_translate("FormGra", "S"))
        self.Dbutton.setText(_translate("FormGra", "D"))
        self.Hbutton.setText(_translate("FormGra", "H"))
        self.Jbutton.setText(_translate("FormGra", "J"))
        self.Kbutton.setText(_translate("FormGra", "K"))
        self.Fbutton.setText(_translate("FormGra", "F"))
        self.Lbutton.setText(_translate("FormGra", "L"))
        self.Abutton.setText(_translate("FormGra", "A"))
        self.Mbutton.setText(_translate("FormGra", "M"))
        self.Zbutton.setText(_translate("FormGra", "Z"))
        self.Xbutton.setText(_translate("FormGra", "X"))
        self.Cbutton.setText(_translate("FormGra", "C"))
        self.Vbutton.setText(_translate("FormGra", "V"))
        self.Nbutton.setText(_translate("FormGra", "N"))
        self.Bbutton.setText(_translate("FormGra", "B"))
        self.haslo1.setText(_translate("FormGra", "_"))
        self.haslo2.setText(_translate("FormGra", "_"))
        self.haslo3.setText(_translate("FormGra", "_"))
        self.haslo4.setText(_translate("FormGra", "_"))
        self.haslo5.setText(_translate("FormGra", "_"))
        self.haslo6.setText(_translate("FormGra", "_"))
        self.haslo7.setText(_translate("FormGra", "_"))
        self.haslo8.setText(_translate("FormGra", "_"))
        self.haslo9.setText(_translate("FormGra", "_"))
        self.haslo10.setText(_translate("FormGra", "_"))
        self.haslo11.setText(_translate("FormGra", "_"))
        self.haslo12.setText(_translate("FormGra", "_"))
        self.haslo1_2.setText(_translate("FormGra", ""))
        self.haslo2_2.setText(_translate("FormGra", ""))
        self.haslo6_2.setText(_translate("FormGra", ""))
        self.haslo12_2.setText(_translate("FormGra", ""))
        self.haslo7_2.setText(_translate("FormGra", ""))
        self.haslo10_2.setText(_translate("FormGra", ""))
        self.haslo4_2.setText(_translate("FormGra", ""))
        self.haslo5_2.setText(_translate("FormGra", ""))
        self.haslo9_2.setText(_translate("FormGra", ""))
        self.haslo8_2.setText(_translate("FormGra", ""))
        self.haslo11_2.setText(_translate("FormGra", ""))
        self.haslo3_2.setText(_translate("FormGra", ""))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormGra = QtWidgets.QWidget()
    ui = Ui_FormGra()
    ui.setupUi(FormGra)
    FormGra.show()
    sys.exit(app.exec_())
