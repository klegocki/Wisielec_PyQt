
from PyQt5 import QtCore, QtGui, QtWidgets
import  WisielecWpiszHaslo
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QTextEdit, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import WisielecWybierzHaslo
import os

class Gracz:
    def __init__(self,przegrane,wygrane,rola,pseudonim,istnieje):

        self.pseudonim=pseudonim
        self.przegrane=przegrane
        self.rola=rola
        self.wygrane=wygrane
        self.istnieje=istnieje

class Ui_MainWindow(object):

    def openWindowWpiszHaslo(self):
        try:
            if self.gracz1.istnieje == 1 and self.gracz2.istnieje == 1:
                self.window = QWidget()
                self.ui = WisielecWybierzHaslo.Ui_Form(self.gracz1, self.gracz2)
                self.ui.setupUi(self.window)
                self.window.show()
                current_window = QtWidgets.QApplication.activeWindow()
                current_window.close()

            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle("Błąd")
                msg_box.setText("Nie utworzono graczy.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

        except Exception:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Błąd")
            msg_box.setText("Nie utworzono graczy.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    def closeMainWindow(self):
        current_window = QtWidgets.QApplication.activeWindow()
        current_window.close()
    def __init__(self, Startgracz1, Startgracz2):
        self.gracz1 = Startgracz1
        self.gracz2 = Startgracz2

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1130, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.przycisk_Graj = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openWindowWpiszHaslo())
        self.przycisk_Graj.setEnabled(True)
        self.przycisk_Graj.setGeometry(QtCore.QRect(460, 360, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.przycisk_Graj.setFont(font)
        self.przycisk_Graj.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.przycisk_Graj.setObjectName("przycisk_Graj")
        self.przycisk_Wyjdz = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.closeMainWindow())
        self.przycisk_Wyjdz.setEnabled(True)
        self.przycisk_Wyjdz.setGeometry(QtCore.QRect(460, 480, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.przycisk_Wyjdz.setFont(font)
        self.przycisk_Wyjdz.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.przycisk_Wyjdz.setObjectName("przycisk_Wyjdz")

        #przycisk do potwierdzania gracza1
        self.przycisk_gracz1_potwierdz = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.utworzenie_gracza_1())
        self.przycisk_gracz1_potwierdz.setEnabled(True)
        self.przycisk_gracz1_potwierdz.setGeometry(QtCore.QRect(20, 77, 152, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.przycisk_gracz1_potwierdz.setFont(font)
        self.przycisk_gracz1_potwierdz.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.przycisk_gracz1_potwierdz.setObjectName("przycisk_gracz1_potwierdz")

        #przycisk do usuwania gracza1
        self.przycisk_gracz1_usun = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.UsunGracza1())
        self.przycisk_gracz1_usun.setEnabled(True)
        self.przycisk_gracz1_usun.setGeometry(QtCore.QRect(20, 77, 152, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.przycisk_gracz1_usun.setFont(font)
        self.przycisk_gracz1_usun.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.przycisk_gracz1_usun.setObjectName("przycisk_gracz1_usun")
        self.przycisk_gracz1_usun.hide()

        #przycisk do potwierdzania gracza2
        self.przycisk_gracz2_potwierdz = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.utworzenie_gracza_2())
        self.przycisk_gracz2_potwierdz.setEnabled(True)
        self.przycisk_gracz2_potwierdz.setGeometry(QtCore.QRect(960, 77, 152, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.przycisk_gracz2_potwierdz.setFont(font)
        self.przycisk_gracz2_potwierdz.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.przycisk_gracz2_potwierdz.setObjectName("przycisk_gracz2_potwierdz")

        # przycisk do usuwania gracza2
        self.przycisk_gracz2_usun = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.UsunGracza2())
        self.przycisk_gracz2_usun.setEnabled(True)
        self.przycisk_gracz2_usun.setGeometry(QtCore.QRect(960, 77, 152, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.przycisk_gracz2_usun.setFont(font)
        self.przycisk_gracz2_usun.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.przycisk_gracz2_usun.setObjectName("przycisk_gracz2_usun")
        self.przycisk_gracz2_usun.hide()



        self.nick_gracza1 = QtWidgets.QLabel(self.centralwidget)
        self.nick_gracza1.setGeometry(QtCore.QRect(20, 0, 200, 41))
        self.nick_gracza1.setStyleSheet("color: white;")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nick_gracza1.setFont(font)
        self.nick_gracza1.setObjectName("nick_gracza1")
        self.nick_gracza2 = QtWidgets.QLabel(self.centralwidget)
        self.nick_gracza2.setGeometry(QtCore.QRect(960, 0, 200, 41))
        self.nick_gracza2.setStyleSheet("color: white;")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nick_gracza2.setFont(font)
        self.nick_gracza2.setObjectName("nick_gracza2")

        self.przycisk_zamien_role = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.zamiana_rol())
        self.przycisk_zamien_role.setEnabled(True)
        self.przycisk_zamien_role.setGeometry(QtCore.QRect(460, 420, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.przycisk_zamien_role.setFont(font)
        self.przycisk_zamien_role.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.przycisk_zamien_role.setObjectName("przycisk_zamien_role")
        self.input_gracz1 = QtWidgets.QTextEdit(self.centralwidget)
        self.input_gracz1.setGeometry(QtCore.QRect(20, 40, 151, 31))
        self.input_gracz1.setObjectName("input_gracz1")
        self.input_gracz2 = QtWidgets.QTextEdit(self.centralwidget)
        self.input_gracz2.setGeometry(QtCore.QRect(960, 40, 151, 31))
        self.input_gracz2.setObjectName("input_gracz2")

        #gracz1 rola
        self.gracz1_rola = QtWidgets.QLabel(self.centralwidget)
        self.gracz1_rola.setEnabled(True)
        self.gracz1_rola.setGeometry(QtCore.QRect(20, 105, 190, 51))
        self.gracz1_rola.setText("")
        self.gracz1_rola.setObjectName("gracz1_rola")
        self.gracz1_rola.setStyleSheet("color: white;")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.gracz1_rola.setFont(font)


        #gracz1 wygrane
        self.gracz1_wygrane = QtWidgets.QLabel(self.centralwidget)
        self.gracz1_wygrane.setEnabled(True)
        self.gracz1_wygrane.setGeometry(QtCore.QRect(20, 135, 170, 51))
        self.gracz1_wygrane.setText("Brak gracza")
        self.gracz1_wygrane.setObjectName("gracz1_wygrane: ")
        self.gracz1_wygrane.setStyleSheet("color: white;")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.gracz1_wygrane.setFont(font)

        #gracz1 przegrane
        self.gracz1_przegrane = QtWidgets.QLabel(self.centralwidget)
        self.gracz1_przegrane.setEnabled(True)
        self.gracz1_przegrane.setGeometry(QtCore.QRect(20, 170, 220, 51))
        self.gracz1_przegrane.setText("Brak gracza")
        self.gracz1_przegrane.setObjectName("gracz1_przegrane")
        self.gracz1_przegrane.setStyleSheet("color: white;")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.gracz1_przegrane.setFont(font)

        #gracz2 przegrane
        self.gracz2_przegrane = QtWidgets.QLabel(self.centralwidget)
        self.gracz2_przegrane.setEnabled(True)
        self.gracz2_przegrane.setGeometry(QtCore.QRect(960, 170, 170, 51))
        self.gracz2_przegrane.setText("Brak gracza")
        self.gracz2_przegrane.setObjectName("gracz2_przegrane")
        self.gracz2_przegrane.setStyleSheet("color: white;")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.gracz2_przegrane.setFont(font)

        #gracz2 wygrane
        self.gracz2_wygrane = QtWidgets.QLabel(self.centralwidget)
        self.gracz2_wygrane.setEnabled(True)
        self.gracz2_wygrane.setGeometry(QtCore.QRect(960, 135, 170, 51))
        self.gracz2_wygrane.setText("Brak gracza")
        self.gracz2_wygrane.setObjectName("gracz2_wygrane")
        self.gracz2_wygrane.setStyleSheet("color: white;")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.gracz2_wygrane.setFont(font)

        #gracz2 rola
        self.gracz2_rola = QtWidgets.QLabel(self.centralwidget)
        self.gracz2_rola.setEnabled(True)
        self.gracz2_rola.setGeometry(QtCore.QRect(960, 105, 170, 51))
        self.gracz2_rola.setText("")
        self.gracz2_rola.setObjectName("gracz2_rola")
        self.gracz2_rola.setStyleSheet("color: white;")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.gracz2_rola.setFont(font)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        palette = QPalette()
        background_image = QImage(os.getcwd()+"\zdjecie.png")
        palette.setBrush(QPalette.Window, QBrush(background_image))
        MainWindow.setPalette(palette)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        if(self.gracz1.istnieje == 1 and self.gracz2.istnieje==1):
            self.ZmienUiPoskonczonejRozgrywce()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wisielec"))
        self.przycisk_Graj.setText(_translate("MainWindow", "GRAJ"))
        self.przycisk_Wyjdz.setText(_translate("MainWindow", "WYJDZ"))
        self.gracz1_rola.setText(_translate("MainWindow", "Rola: wpisujący"))
        self.gracz2_rola.setText(_translate("MainWindow", "Rola: zgadujący"))

        if(self.gracz1.istnieje == 0 and self.gracz2.istnieje == 0 ):
            self.nick_gracza1.setText(_translate("MainWindow", "Gracz 1"))
            self.nick_gracza2.setText(_translate("MainWindow", "Gracz 2"))
        else:
            self.nick_gracza1.setText(_translate("MainWindow", str(self.gracz1.pseudonim)))
            self.nick_gracza2.setText(_translate("MainWindow", str(self.gracz2.pseudonim)))
        self.przycisk_zamien_role.setText(_translate("MainWindow", "ZAMIEN ROLE"))
        self.przycisk_gracz1_potwierdz.setText(_translate("MainWindow", "Potwierdź"))
        self.przycisk_gracz2_potwierdz.setText(_translate("MainWindow", "Potwierdź"))
        self.przycisk_gracz1_usun.setText(_translate("MainWindow", "Usuń"))
        self.przycisk_gracz2_usun.setText(_translate("MainWindow", "Usuń"))
       # self.gracz1_rola.setText(_translate("MainWindow", "Usuń"))



    def utworzenie_gracza_1(self):
        sprawdzCzywpisanoNick = self.input_gracz1.toPlainText()
        if(sprawdzCzywpisanoNick.strip() != ""):
            self.gracz1 = Gracz(0, 0, False, str(sprawdzCzywpisanoNick), 1)
            self.gracz1.rola = False
            self.gracz1.pseudonim = self.input_gracz1.toPlainText()
            self.gracz1.istnieje = 1
            if (self.gracz2.istnieje == 1 and self.gracz2.rola == False):
                self.gracz1.rola = True
            self.nick_gracza1.setText(self.gracz1.pseudonim)
            #zmiana gui po podaniu nicku gracza
            self.przycisk_gracz1_potwierdz.hide()
            self.input_gracz1.clear()
            self.input_gracz1.hide()
            self.przycisk_gracz1_usun.show()
            self.przycisk_gracz1_usun.setGeometry(QtCore.QRect(20, 40, 152, 40))
            self.gracz1_rola.setGeometry(QtCore.QRect(20, 68, 190, 51))
            self.gracz1_wygrane.setGeometry(QtCore.QRect(20, 98, 170, 51))
            self.gracz1_przegrane.setGeometry(QtCore.QRect(20, 130, 220, 51))
            self.nick_gracza1.setText(str(self.gracz1.pseudonim))
            self.gracz1_wygrane.setText("Wygrane "+str(self.gracz1.pseudonim) + ": " + str(self.gracz1.wygrane))
            self.gracz1_przegrane.setText("Przegrane "+str(self.gracz1.pseudonim) + ": " + str(self.gracz1.przegrane))

        else:
            #zabezpieczenie przed zostawieniem pustego pola na nick
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Błąd")
            msg_box.setText("Nie wpisano nicku. Wpisz nick")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    def utworzenie_gracza_2(self):
        sprawdzCzywpisanoNick = self.input_gracz2.toPlainText()
        if (sprawdzCzywpisanoNick.strip() != ""):
            self.gracz2 = Gracz(0, 0, False, str(sprawdzCzywpisanoNick), 1)
            self.gracz2.rola = True
            self.gracz2.pseudonim = self.input_gracz2.toPlainText()
            self.gracz2.istnieje = 1
            if (self.gracz1.istnieje == 1 and self.gracz1.rola == True):
                self.gracz2.rola = False
            self.nick_gracza2.setText(self.gracz2.pseudonim)

            # zmiana gui po podaniu nicku gracza
            self.przycisk_gracz2_potwierdz.hide()
            self.input_gracz2.clear()
            self.input_gracz2.hide()
            self.przycisk_gracz2_usun.show()
            self.przycisk_gracz2_usun.setGeometry(QtCore.QRect(960, 40, 152, 40))
            self.gracz2_rola.setGeometry(QtCore.QRect(960, 68, 170, 51))
            self.gracz2_wygrane.setGeometry(QtCore.QRect(960, 98, 170, 51))
            self.gracz2_przegrane.setGeometry(QtCore.QRect(960, 130, 170, 51))
            self.nick_gracza2.setText(str(self.gracz2.pseudonim))
            self.gracz2_wygrane.setText("Wygrane "+ str(self.gracz2.pseudonim) + ": " + str(self.gracz2.wygrane))
            self.gracz2_przegrane.setText("Przegrane "+str(self.gracz2.pseudonim) + ": " + str(self.gracz2.przegrane))
        else:
            #zabezpieczenie przed zostawieniem pustego pola na nick
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Błąd")
            msg_box.setText("Nie wpisano nicku. Wpisz nick")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

#usuwanie gracza1
    def UsunGracza1(self):
        if(self.gracz1.istnieje == 1):
            self.gracz1.istnieje = 0 #usunięcie obiektu gracza
            self.gracz1.pseudonim = ""
            self.gracz1.wygrane = 0
            self.gracz1.przegrane = 0
            self.gracz1.rola = True
            #zmiana gui po usunięciu
            self.nick_gracza1.setText("Gracz1")
            self.przycisk_gracz1_potwierdz.show()
            self.input_gracz1.show()
            self.gracz1_wygrane.setText("Brak gracza.")
            self.gracz1_przegrane.setText("Brak gracza.")
            if(self.gracz2.rola == False):
                self.gracz1_rola.setText("Rola: zgadujący")
            else:
                self.gracz1_rola.setText("Rola: wpisujący")
            self.przycisk_gracz1_usun.hide()
            self.przycisk_gracz1_potwierdz.setGeometry(QtCore.QRect(20, 77, 152, 40))
            self.przycisk_gracz1_usun.setGeometry(QtCore.QRect(20, 122, 152, 40))
            self.gracz1_rola.setGeometry(QtCore.QRect(20, 105, 190, 51))
            self.gracz1_wygrane.setGeometry(QtCore.QRect(20, 135, 170, 51))
            self.gracz1_przegrane.setGeometry(QtCore.QRect(20, 167, 220, 51))

    def UsunGracza2(self):
        if(self.gracz2.istnieje == 1):
            self.gracz2.istnieje = 0  # usunięcie obiektu gracza
            self.gracz2.pseudonim = ""
            self.gracz2.wygrane = 0
            self.gracz2.przegrane = 0
            self.gracz2.rola = True
            #zmiana gui po usunięciu
            self.nick_gracza2.setText("Gracz2")
            self.przycisk_gracz2_potwierdz.show()
            self.input_gracz2.show()
            self.gracz2_wygrane.setText("Brak gracza.")
            self.gracz2_przegrane.setText("Brak gracza.")
            if(self.gracz1.rola == False):
                self.gracz2_rola.setText("Rola: zgadujący")
            else:
                self.gracz2_rola.setText("Rola: wpisujący")
            self.przycisk_gracz2_usun.hide()
            self.przycisk_gracz2_potwierdz.setGeometry(QtCore.QRect(960, 77, 152, 40))
            self.przycisk_gracz2_usun.setGeometry(QtCore.QRect(970, 122, 152, 40))
            self.gracz2_rola.setGeometry(QtCore.QRect(960, 105, 170, 51))
            self.gracz2_wygrane.setGeometry(QtCore.QRect(960, 135, 170, 51))
            self.gracz2_przegrane.setGeometry(QtCore.QRect(960, 167, 170, 51))




    def zamiana_rol(self):

        if self.gracz1.istnieje == 1 and self.gracz2.istnieje == 1:
            self.gracz1.rola, self.gracz2.rola = self.gracz2.rola, self.gracz1.rola
            if(self.gracz1.rola == True and self.gracz2.rola == False):
                self.gracz1_rola.setText("Rola: zgadujący")
                self.gracz2_rola.setText("Rola: wpisujący")
            else:
                self.gracz1_rola.setText("Rola: wpisujący")
                self.gracz2_rola.setText("Rola: zgadujący")
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Błąd")
            msg_box.setText("Nie utworzono graczy.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    def ZmienUiPoskonczonejRozgrywce(self):
        #UI gracza1
        self.przycisk_gracz1_potwierdz.hide()
        self.input_gracz1.hide()
        self.przycisk_gracz1_usun.show()
        self.przycisk_gracz1_usun.setGeometry(QtCore.QRect(20, 40, 152, 40))
        self.gracz1_rola.setGeometry(QtCore.QRect(20, 68, 190, 51))
        self.gracz1_wygrane.setGeometry(QtCore.QRect(20, 98, 170, 51))
        self.gracz1_przegrane.setGeometry(QtCore.QRect(20, 130, 220, 51))
        self.gracz1_wygrane.setText("Wygrane "+ str(self.gracz1.pseudonim) + ": "+ str(self.gracz1.wygrane))
        self.gracz1_przegrane.setText("Przegrane "+str(self.gracz1.pseudonim) + ": "+ str(self.gracz1.przegrane))

        #UI gracza2
        self.przycisk_gracz2_potwierdz.hide()
        self.input_gracz2.hide()
        self.przycisk_gracz2_usun.show()
        self.przycisk_gracz2_usun.setGeometry(QtCore.QRect(960, 40, 152, 40))
        self.gracz2_rola.setGeometry(QtCore.QRect(960, 68, 170, 51))
        self.gracz2_wygrane.setGeometry(QtCore.QRect(960, 98, 170, 51))
        self.gracz2_przegrane.setGeometry(QtCore.QRect(960, 130, 170, 51))
        self.gracz2_wygrane.setText("Wygrane "+ str(self.gracz2.pseudonim) + ": " + str(self.gracz2.wygrane))
        self.gracz2_przegrane.setText("Przegrane " +(self.gracz2.pseudonim) + ": " + str(self.gracz2.przegrane))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GraczStart1 = Gracz(0, 0, False, "jeden", 0)
    GraczStart2 = Gracz(0, 0, False, "dwa", 0)
    GlowneOkno = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(GraczStart1,GraczStart2)
    ui.setupUi(GlowneOkno)
    GlowneOkno.show()
    sys.exit(app.exec_())
