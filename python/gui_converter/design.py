from parse import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont


class Ui_MainWindow(object):
    first_country = ''
    second_country = ''
    current_text = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Converter")
        MainWindow.resize(500, 507)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        text = QtWidgets.QLabel(MainWindow)
        current_date, current_time = get_current_date()
        text.setText(f'{str(current_date)}  {str(current_time)}')
        text.move(300, 480)
        font = QFont()
        font.setPointSize(11)
        text.setFont(font)
        text.adjustSize()

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(5, 230, 490, 81))
        self.comboBox.setObjectName("comboBox")
        for i in range(len(currency_name) + 1):
            self.comboBox.addItem("")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(5, 40, 490, 81))
        self.comboBox_2.setObjectName("comboBox_2")
        for i in range(len(currency_name) + 1):
            self.comboBox_2.addItem("")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 140, 300, 50))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Enter amount")
        self.lineEdit.setStyleSheet("font-size: 27px; color: blue; border: 2px solid black; "
                                    "background-color: #F0F0F0; color: darkblue; text-align: center")
        self.lineEdit.textChanged.connect(self.on_input_changed)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(100, 330, 300, 50))
        self.listWidget.setStyleSheet("font-size: 27px; color: blue; background-color: lightgray;"
                                      "border: 2px solid black; text-align: center")
        self.listWidget.setObjectName("listWidget")

        self.comboBox_2.raise_()
        self.comboBox.raise_()
        self.listWidget.raise_()
        self.lineEdit.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Converter", "Converter"))

        self.comboBox.setItemText(0, _translate("Converter", 'Выберите валюту'))
        cnt = 1
        for name, short_name in zip(currency_name, currency_short_name):
            self.comboBox.setItemText(cnt, _translate("Converter", name + f' ({short_name})'))
            cnt += 1

        self.comboBox.setStyleSheet("font-size: 27px;")
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)

        self.comboBox_2.setItemText(0, _translate("Converter", 'Выберите валюту'))
        cnt = 1
        for name, short_name in zip(currency_name, currency_short_name):
            self.comboBox_2.setItemText(cnt, _translate("Converter", name + f' ({short_name})'))
            cnt += 1
        self.comboBox_2.setStyleSheet("font-size: 27px;")
        self.comboBox_2.currentIndexChanged.connect(self.on_combobox_changed)

    def on_combobox_changed(self, index):
        self.second_country = self.comboBox.currentText()
        self.first_country = self.comboBox_2.currentText()
        if self.current_text:
            self.listWidget.clear()
            self.listWidget.addItem(str(convert(self.first_country[: -6], self.second_country[: -6],
                                            float(self.current_text))))

    def on_input_changed(self, text):
        self.listWidget.clear()
        text = ''.join(filter(lambda char: char.isdigit() or char == '.', text))
        self.lineEdit.setText(text)
        if text:
            self.current_text = text
            self.listWidget.addItem(str(convert(self.first_country[: -6], self.second_country[: -6],
                                            float(text))))

class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)