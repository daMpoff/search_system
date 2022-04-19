from PyQt5 import QtWidgets, QtCore, QtGui # Импорт класса, который является базовым классом для всех объектов пользовательского интерфейса
from PyQt5.QtWidgets import QMainWindow,QApplication # Импорт классов, отвечающих за создание приложения
import sys

kodirovka = str("")
slovo = str("")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(119, 449, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_button.setFont(font)
        self.search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_button.setCheckable(False)
        self.search_button.setObjectName("search_button")
        self.search_button.clicked.connect(chat)


        self.label_text = QtWidgets.QLabel(self.centralwidget)
        self.label_text.setGeometry(QtCore.QRect(460, 30, 781, 461))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_text.setFont(font)
        self.label_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_text.setFrameShape(QtWidgets.QFrame.Box)
        self.label_text.setLineWidth(3)
        self.label_text.setTextFormat(QtCore.Qt.PlainText)
        self.label_text.setScaledContents(False)
        self.label_text.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_text.setObjectName("label_text")


        self.utf_button = QtWidgets.QRadioButton(self.centralwidget)
        self.utf_button.setGeometry(QtCore.QRect(30, 380, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.utf_button.setFont(font)
        self.utf_button.setObjectName("utf_button")


        self.win_button = QtWidgets.QRadioButton(self.centralwidget)
        self.win_button.setGeometry(QtCore.QRect(30, 349, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.win_button.setFont(font)
        self.win_button.setObjectName("win_button")


        self.slovo_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.slovo_text.setGeometry(QtCore.QRect(30, 180, 291, 31))
        self.slovo_text.setObjectName("slovo_text")


        self.url_site = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.url_site.setGeometry(QtCore.QRect(30, 120, 291, 31))
        self.url_site.setObjectName("url_site")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        x = self.slovo_text.

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Алькена"))
        self.search_button.setText(_translate("MainWindow", "ПОИСК"))
        self.label_text.setText(_translate("MainWindow", "Список совпадений"))
        self.utf_button.setText(_translate("MainWindow", "UTF-8"))
        self.win_button.setText(_translate("MainWindow", "Windows-1251"))
        self.slovo_text.setPlaceholderText(_translate("MainWindow", "Искомое слово"))
        self.url_site.setPlaceholderText(_translate("MainWindow", "Ваша ссылка на сайт"))


if __name__ == "__main__":#Если мы запускаем нашу программу с этого исполяняемого файла, то мы будем сразу же вызывать главную функцию
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

