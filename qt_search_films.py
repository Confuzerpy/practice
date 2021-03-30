from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 277)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 0, 191, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 0, 231, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 0, 111, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonClickedSearch)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 40, 390, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 80, 390, 30))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 120, 390, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 160, 390, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 200, 390, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 111, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 111, 30))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 111, 30))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 111, 30))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 161, 30))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 221, 30))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def buttonClickedSearch(self):
        self.con = sqlite3.connect("films_db.sqlite")
        self.cur = self.con.cursor()
        if self.lineEdit.text():
            if self.comboBox.currentText() == "Год выпуска":
                self.result = self.cur.execute("""SELECT * FROM films
                                        WHERE year = ?""",
                                               (self.lineEdit.text(),)
                                               ).fetchone()
                if self.result:
                    self.lineEdit_2.setText(str(self.result[0]))
                    self.lineEdit_3.setText(str(self.result[1]))
                    self.lineEdit_4.setText(str(self.result[2]))
                    self.lineEdit_5.setText(str(self.result[3]))
                    self.lineEdit_6.setText(str(self.result[4]))
                else:
                    self.label_6.setText("Ничего не найдено")

            elif self.comboBox.currentText() == "Название":
                self.result = self.cur.execute("""SELECT * FROM films
                                        WHERE title = ?""",
                                               (self.lineEdit.text(),)
                                               ).fetchone()
                if self.result:
                    self.lineEdit_2.setText(str(self.result[0]))
                    self.lineEdit_3.setText(str(self.result[1]))
                    self.lineEdit_4.setText(str(self.result[2]))
                    self.lineEdit_5.setText(str(self.result[3]))
                    self.lineEdit_6.setText(str(self.result[4]))
                else:
                    self.label_6.setText("Ничего не найдено")

            elif self.comboBox.currentText() == "Продолжительность":
                self.result = self.cur.execute("""SELECT * FROM films
                                        WHERE duration = ?""",
                                               (self.lineEdit.text(),)
                                               ).fetchone()
                if self.result:
                    self.lineEdit_2.setText(str(self.result[0]))
                    self.lineEdit_3.setText(str(self.result[1]))
                    self.lineEdit_4.setText(str(self.result[2]))
                    self.lineEdit_5.setText(str(self.result[3]))
                    self.lineEdit_6.setText(str(self.result[4]))
                else:
                    self.label_6.setText("Ничего не найдено")

        else:
            self.label_6.setText("Неправильный запрос")
        self.con.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Год выпуска"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Название"))
        self.comboBox.setItemText(2, _translate("MainWindow",
                                                "Продолжительность"))
        self.pushButton.setText(_translate("MainWindow", "Поиск"))
        self.label.setText(_translate("MainWindow", "ID:"))
        self.label_2.setText(_translate("MainWindow", "Название:"))
        self.label_3.setText(_translate("MainWindow", "Год выпуска:"))
        self.label_4.setText(_translate("MainWindow", "Жанр:"))
        self.label_5.setText(_translate("MainWindow", "Продолжительность:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
