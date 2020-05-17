# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xyl.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.c4 = QtWidgets.QPushButton(self.centralwidget)
        self.c4.setGeometry(QtCore.QRect(170, 90, 51, 361))
        self.c4.setStyleSheet("background-color: rgb(212, 0, 0);")
        self.c4.setText("")
        self.c4.setObjectName("c4")
        self.d4 = QtWidgets.QPushButton(self.centralwidget)
        self.d4.setGeometry(QtCore.QRect(240, 90, 51, 331))
        self.d4.setStyleSheet("background-color: rgb(229, 76, 0);")
        self.d4.setText("")
        self.d4.setObjectName("d4")
        self.e4 = QtWidgets.QPushButton(self.centralwidget)
        self.e4.setGeometry(QtCore.QRect(310, 90, 51, 301))
        self.e4.setStyleSheet("background-color: rgb(232, 232, 0);")
        self.e4.setText("")
        self.e4.setObjectName("e4")
        self.f4 = QtWidgets.QPushButton(self.centralwidget)
        self.f4.setGeometry(QtCore.QRect(380, 90, 51, 271))
        self.f4.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.f4.setText("")
        self.f4.setObjectName("f4")
        self.g4 = QtWidgets.QPushButton(self.centralwidget)
        self.g4.setGeometry(QtCore.QRect(450, 90, 51, 241))
        self.g4.setStyleSheet("background-color: rgb(75, 151, 226);")
        self.g4.setText("")
        self.g4.setObjectName("g4")
        self.a4 = QtWidgets.QPushButton(self.centralwidget)
        self.a4.setGeometry(QtCore.QRect(520, 90, 51, 211))
        self.a4.setStyleSheet("background-color: rgb(0, 0, 165);")
        self.a4.setText("")
        self.a4.setObjectName("a4")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(590, 90, 51, 181))
        self.b4.setStyleSheet("background-color: rgb(221, 0, 166);")
        self.b4.setText("")
        self.b4.setObjectName("b4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 30, 341, 51))
        self.label.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Xylophone"))

