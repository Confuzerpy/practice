# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 125, 50, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.button)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 150, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 150, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 220, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(380, 150, 100, 50))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setGeometry(QtCore.QRect(380, 10, 100, 50))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setGeometry(QtCore.QRect(380, 80, 100, 50))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_7.setGeometry(QtCore.QRect(380, 220, 100, 50))
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(270, 150, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(280, 80, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(280, 10, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 90, 150, 27))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 180, 150, 27))
        self.textEdit_2.setObjectName("textEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def button(self):
        try:
            self.lcdNumber_4.display(
                int(self.textEdit.toPlainText()) * int(self.textEdit_2.toPlainText()))
            self.lcdNumber_5.display(
                int(self.textEdit.toPlainText()) + int(self.textEdit_2.toPlainText()))
            self.lcdNumber_6.display(
                int(self.textEdit.toPlainText()) - int(self.textEdit_2.toPlainText()))
            self.lcdNumber_7.display(
                int(self.textEdit.toPlainText()) / int(self.textEdit_2.toPlainText()))
        except ZeroDivisionError:
            self.lcdNumber_7.display("error")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Миникалькулятор"))
        self.pushButton.setText(_translate("MainWindow", "->"))
        self.label.setText(_translate("MainWindow", "Первое число(целое)"))
        self.label_2.setText(_translate("MainWindow", "Второе число(целое)"))
        self.label_6.setText(_translate("MainWindow", "Частное:"))
        self.label_7.setText(_translate("MainWindow", "Произведение:"))
        self.label_8.setText(_translate("MainWindow", "Разность:"))
        self.label_9.setText(_translate("MainWindow", "Сумма:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
