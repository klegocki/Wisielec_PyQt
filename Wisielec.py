
from PyQt5 import QtCore, QtGui, QtWidgets
from WisielecWpiszHaslo import *




class Gracz:
    def __init__(self,przegrane,wygrane,rola,pseudonim,istnieje):
        self.pseudonim=pseudonim
        self.przegrane=przegrane
        self.rola=rola
        self.wygrane=wygrane
        self.istnieje=istnieje


class Ui_MainWindow(object):

    def openWindowWpiszHaslo(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FormHaslo()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

    def closeMainWindow(self):
        sys.exit(app.exec_())

    def __init__(self):
        self.gracz1 = Gracz(0, 0, False, "null", 0)
        self.gracz2 = Gracz(0, 0, False, "null", 0)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 643)
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
        self.przycisk_gracz1_potwierdz = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.utworzenie_gracza_1())
        self.przycisk_gracz1_potwierdz.setEnabled(True)
        self.przycisk_gracz1_potwierdz.setGeometry(QtCore.QRect(17, 100, 156, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.przycisk_gracz1_potwierdz.setFont(font)
        self.przycisk_gracz1_potwierdz.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.przycisk_gracz1_potwierdz.setObjectName("przycisk_gracz1_potwierdz")
        self.przycisk_gracz2_potwierdz = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.utworzenie_gracza_2())
        self.przycisk_gracz2_potwierdz.setEnabled(True)
        self.przycisk_gracz2_potwierdz.setGeometry(QtCore.QRect(958, 100, 156, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.przycisk_gracz2_potwierdz.setFont(font)
        self.przycisk_gracz2_potwierdz.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.przycisk_gracz2_potwierdz.setObjectName("przycisk_gracz2_potwierdz")
        self.nick_gracza1 = QtWidgets.QLabel(self.centralwidget)
        self.nick_gracza1.setGeometry(QtCore.QRect(20, 0, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nick_gracza1.setFont(font)
        self.nick_gracza1.setObjectName("nick_gracza1")
        self.nick_gracza2 = QtWidgets.QLabel(self.centralwidget)
        self.nick_gracza2.setGeometry(QtCore.QRect(1040, 0, 71, 41))
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
        self.gracz1_rola = QtWidgets.QLabel(self.centralwidget)
        self.gracz1_rola.setEnabled(True)
        self.gracz1_rola.setGeometry(QtCore.QRect(20, 90, 151, 51))
        self.gracz1_rola.setText("")
        self.gracz1_rola.setObjectName("gracz1_rola")
        self.gracz1_wygrane = QtWidgets.QLabel(self.centralwidget)
        self.gracz1_wygrane.setEnabled(True)
        self.gracz1_wygrane.setGeometry(QtCore.QRect(20, 160, 151, 51))
        self.gracz1_wygrane.setText("")
        self.gracz1_wygrane.setObjectName("gracz1_wygrane")
        self.gracz1_przegrane = QtWidgets.QLabel(self.centralwidget)
        self.gracz1_przegrane.setEnabled(True)
        self.gracz1_przegrane.setGeometry(QtCore.QRect(20, 230, 151, 51))
        self.gracz1_przegrane.setText("")
        self.gracz1_przegrane.setObjectName("gracz1_przegrane")
        self.gracz2_przegrane = QtWidgets.QLabel(self.centralwidget)
        self.gracz2_przegrane.setEnabled(True)
        self.gracz2_przegrane.setGeometry(QtCore.QRect(970, 220, 151, 51))
        self.gracz2_przegrane.setText("")
        self.gracz2_przegrane.setObjectName("gracz2_przegrane")
        self.gracz2_wygrane = QtWidgets.QLabel(self.centralwidget)
        self.gracz2_wygrane.setEnabled(True)
        self.gracz2_wygrane.setGeometry(QtCore.QRect(970, 150, 151, 51))
        self.gracz2_wygrane.setText("")
        self.gracz2_wygrane.setObjectName("gracz2_wygrane")
        self.gracz2_rola = QtWidgets.QLabel(self.centralwidget)
        self.gracz2_rola.setEnabled(True)
        self.gracz2_rola.setGeometry(QtCore.QRect(970, 80, 151, 51))
        self.gracz2_rola.setText("")
        self.gracz2_rola.setObjectName("gracz2_rola")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wisielec"))
        self.przycisk_Graj.setText(_translate("MainWindow", "GRAJ"))
        self.przycisk_Wyjdz.setText(_translate("MainWindow", "WYJDZ"))
        self.nick_gracza1.setText(_translate("MainWindow", "Gracz 1"))
        self.nick_gracza2.setText(_translate("MainWindow", "Gracz 2"))
        self.przycisk_zamien_role.setText(_translate("MainWindow", "ZAMIEN ROLE"))
        self.przycisk_gracz1_potwierdz.setText(_translate("MainWindow", "Potwierdz"))
        self.przycisk_gracz2_potwierdz.setText(_translate("MainWindow", "Potwierdz"))

    def utworzenie_gracza_1(self):
        self.gracz1.rola = False
        self.gracz1.pseudonim = self.input_gracz1.toPlainText()
        self.gracz1.istnieje = 1
        self.nick_gracza1.setText(self.gracz1.pseudonim)
        print("gracz1: " + self.gracz1.pseudonim)

    def utworzenie_gracza_2(self):
        self.gracz2.rola = True
        self.gracz2.pseudonim = self.input_gracz2.toPlainText()
        self.gracz2.istnieje = 1
        self.nick_gracza2.setText(self.gracz2.pseudonim)
        print("gracz2: " + self.gracz2.pseudonim)

    def zamiana_rol(self):
        if self.gracz1.istnieje == 1 and self.gracz2.istnieje == 1:
            self.gracz1, self.gracz2 = self.gracz2, self.gracz1
            self.nick_gracza1.setText(self.gracz1.pseudonim)
            self.nick_gracza2.setText(self.gracz2.pseudonim)
            print("gracz1: " + self.gracz1.pseudonim)
            print("gracz2: " + self.gracz2.pseudonim)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
