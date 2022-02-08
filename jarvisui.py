# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog,QTextBrowser,QLineEdit,QVBoxLayout,QDesktopWidget

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.setWindowTitle('Just a dialog')
        self.lineedit = QLineEdit("Write something and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()

    def update_ui(self):
        self.browser.append(self.lineedit.text())

def SplashScreenShow(str):
    splash_pix = QPixmap(str)
    splash_pix=splash_pix.scaledToHeight(600)
    splash = QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    time.sleep(2)
    form = Form()
    splash.finish(form)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1119, 852)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1121, 851))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/iron-man.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 750, 161, 71))
        self.pushButton.setSizeIncrement(QtCore.QSize(15, 15))
        self.pushButton.setBaseSize(QtCore.QSize(5, 22))
        self.pushButton.setStyleSheet("background-color:transparent;\n"
        "color:rgb(255, 255, 255);\n"
        "font: 20pt \"Agency FB\";\n"
        "border-style:outset;\n"
        "border-width:2px;\n"
        "border-radius:10px;\n"
        "border-color:white;")
        self.pushButton.setIconSize(QtCore.QSize(10, 10))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 750, 161, 71))
        self.pushButton_2.setStyleSheet("background-color:transparent;\n"
        "color:rgb(255, 255, 255);\n"
        "font: 20pt \"Agency FB\";\n"
        "border-style:outset;\n"
        "border-width:2px;\n"
        "border-radius:10px;\n"
        "border-color:white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(200, 30, 256, 192))
        self.textBrowser.setStyleSheet("background-color:transparent;\n"
        "color:rgb(255, 255, 255);\n"
        "font: 20pt \"Agency FB\";")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(800, 30, 256, 192))
        self.textBrowser_2.setStyleSheet("background-color:transparent;\n"
        "color:rgb(255, 255, 255);\n"
        "font: 20pt \"Agency FB\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 680, 591, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/initiating.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 331, 201))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/jarvis.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "CREATE"))
        self.pushButton_2.setText(_translate("MainWindow", "DESTROY"))


if __name__ == "__main__":
    import sys,time
    app = QtWidgets.QApplication(sys.argv)
    #SplashScreenShow('images/tonystark.gif')
    #SplashScreenShow('images/jarvis.gif')
    #SplashScreenShow('images/initiating.gif')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
