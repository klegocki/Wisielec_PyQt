import sys
from PyQt5.QtWidgets import QApplication
from Wisielec import Ui_MainWindow  # Zaimportuj klasę Ui_MainWindow z pliku Wisielec

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())