# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkers.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Checkers(object):
    def setupUi(self, Checkers):
        Checkers.setObjectName("Checkers")
        Checkers.resize(800, 600)
        Checkers.setMinimumSize(QtCore.QSize(800, 600))
        Checkers.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/NB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Checkers.setWindowIcon(icon)
        self.A_1 = QtWidgets.QPushButton(Checkers)
        self.A_1.setGeometry(QtCore.QRect(50, 80, 60, 60))
        self.A_1.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.A_1.setText("")
        self.A_1.setIconSize(QtCore.QSize(50, 50))
        self.A_1.setObjectName("A_1")
        self.A_2 = QtWidgets.QPushButton(Checkers)
        self.A_2.setGeometry(QtCore.QRect(110, 80, 60, 60))
        self.A_2.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.A_2.setText("")
        self.A_2.setIcon(icon)
        self.A_2.setIconSize(QtCore.QSize(50, 50))
        self.A_2.setObjectName("A_2")
        self.A_3 = QtWidgets.QPushButton(Checkers)
        self.A_3.setGeometry(QtCore.QRect(170, 80, 60, 60))
        self.A_3.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.A_3.setText("")
        self.A_3.setIconSize(QtCore.QSize(50, 50))
        self.A_3.setObjectName("A_3")
        self.A_5 = QtWidgets.QPushButton(Checkers)
        self.A_5.setGeometry(QtCore.QRect(290, 80, 60, 60))
        self.A_5.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.A_5.setText("")
        self.A_5.setIconSize(QtCore.QSize(50, 50))
        self.A_5.setObjectName("A_5")
        self.A_6 = QtWidgets.QPushButton(Checkers)
        self.A_6.setGeometry(QtCore.QRect(350, 80, 60, 60))
        self.A_6.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.A_6.setText("")
        self.A_6.setIcon(icon)
        self.A_6.setIconSize(QtCore.QSize(50, 50))
        self.A_6.setObjectName("A_6")
        self.A_4 = QtWidgets.QPushButton(Checkers)
        self.A_4.setGeometry(QtCore.QRect(230, 80, 60, 60))
        self.A_4.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.A_4.setText("")
        self.A_4.setIcon(icon)
        self.A_4.setIconSize(QtCore.QSize(50, 50))
        self.A_4.setObjectName("A_4")
        self.A_7 = QtWidgets.QPushButton(Checkers)
        self.A_7.setGeometry(QtCore.QRect(410, 80, 60, 60))
        self.A_7.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.A_7.setText("")
        self.A_7.setIconSize(QtCore.QSize(50, 50))
        self.A_7.setObjectName("A_7")
        self.A_8 = QtWidgets.QPushButton(Checkers)
        self.A_8.setGeometry(QtCore.QRect(470, 80, 60, 60))
        self.A_8.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.A_8.setText("")
        self.A_8.setIcon(icon)
        self.A_8.setIconSize(QtCore.QSize(50, 50))
        self.A_8.setObjectName("A_8")
        self.B_6 = QtWidgets.QPushButton(Checkers)
        self.B_6.setGeometry(QtCore.QRect(350, 140, 60, 60))
        self.B_6.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.B_6.setText("")
        self.B_6.setIconSize(QtCore.QSize(50, 50))
        self.B_6.setObjectName("B_6")
        self.B_7 = QtWidgets.QPushButton(Checkers)
        self.B_7.setGeometry(QtCore.QRect(410, 140, 60, 60))
        self.B_7.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.B_7.setText("")
        self.B_7.setIcon(icon)
        self.B_7.setIconSize(QtCore.QSize(50, 50))
        self.B_7.setObjectName("B_7")
        self.B_8 = QtWidgets.QPushButton(Checkers)
        self.B_8.setGeometry(QtCore.QRect(470, 140, 60, 60))
        self.B_8.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.B_8.setText("")
        self.B_8.setIconSize(QtCore.QSize(50, 50))
        self.B_8.setObjectName("B_8")
        self.B_3 = QtWidgets.QPushButton(Checkers)
        self.B_3.setGeometry(QtCore.QRect(170, 140, 60, 60))
        self.B_3.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.B_3.setText("")
        self.B_3.setIcon(icon)
        self.B_3.setIconSize(QtCore.QSize(50, 50))
        self.B_3.setObjectName("B_3")
        self.B_1 = QtWidgets.QPushButton(Checkers)
        self.B_1.setGeometry(QtCore.QRect(50, 140, 60, 60))
        self.B_1.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.B_1.setText("")
        self.B_1.setIcon(icon)
        self.B_1.setIconSize(QtCore.QSize(50, 50))
        self.B_1.setObjectName("B_1")
        self.B_5 = QtWidgets.QPushButton(Checkers)
        self.B_5.setGeometry(QtCore.QRect(290, 140, 60, 60))
        self.B_5.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.B_5.setText("")
        self.B_5.setIcon(icon)
        self.B_5.setIconSize(QtCore.QSize(50, 50))
        self.B_5.setObjectName("B_5")
        self.B_4 = QtWidgets.QPushButton(Checkers)
        self.B_4.setGeometry(QtCore.QRect(230, 140, 60, 60))
        self.B_4.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.B_4.setText("")
        self.B_4.setIconSize(QtCore.QSize(50, 50))
        self.B_4.setObjectName("B_4")
        self.B_2 = QtWidgets.QPushButton(Checkers)
        self.B_2.setGeometry(QtCore.QRect(110, 140, 60, 60))
        self.B_2.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.B_2.setText("")
        self.B_2.setIconSize(QtCore.QSize(50, 50))
        self.B_2.setObjectName("B_2")
        self.C_6 = QtWidgets.QPushButton(Checkers)
        self.C_6.setGeometry(QtCore.QRect(350, 200, 60, 60))
        self.C_6.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.C_6.setText("")
        self.C_6.setIcon(icon)
        self.C_6.setIconSize(QtCore.QSize(50, 50))
        self.C_6.setObjectName("C_6")
        self.D_5 = QtWidgets.QPushButton(Checkers)
        self.D_5.setGeometry(QtCore.QRect(290, 260, 60, 60))
        self.D_5.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.D_5.setText("")
        self.D_5.setIconSize(QtCore.QSize(50, 50))
        self.D_5.setObjectName("D_5")
        self.D_1 = QtWidgets.QPushButton(Checkers)
        self.D_1.setGeometry(QtCore.QRect(50, 260, 60, 60))
        self.D_1.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.D_1.setText("")
        self.D_1.setIconSize(QtCore.QSize(50, 50))
        self.D_1.setObjectName("D_1")
        self.C_7 = QtWidgets.QPushButton(Checkers)
        self.C_7.setGeometry(QtCore.QRect(410, 200, 60, 60))
        self.C_7.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.C_7.setText("")
        self.C_7.setIconSize(QtCore.QSize(50, 50))
        self.C_7.setObjectName("C_7")
        self.C_8 = QtWidgets.QPushButton(Checkers)
        self.C_8.setGeometry(QtCore.QRect(470, 200, 60, 60))
        self.C_8.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.C_8.setText("")
        self.C_8.setIcon(icon)
        self.C_8.setIconSize(QtCore.QSize(50, 50))
        self.C_8.setObjectName("C_8")
        self.D_8 = QtWidgets.QPushButton(Checkers)
        self.D_8.setGeometry(QtCore.QRect(470, 260, 60, 60))
        self.D_8.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.D_8.setText("")
        self.D_8.setIconSize(QtCore.QSize(50, 50))
        self.D_8.setObjectName("D_8")
        self.D_3 = QtWidgets.QPushButton(Checkers)
        self.D_3.setGeometry(QtCore.QRect(170, 260, 60, 60))
        self.D_3.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.D_3.setText("")
        self.D_3.setIconSize(QtCore.QSize(50, 50))
        self.D_3.setObjectName("D_3")
        self.D_4 = QtWidgets.QPushButton(Checkers)
        self.D_4.setGeometry(QtCore.QRect(230, 260, 60, 60))
        self.D_4.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.D_4.setText("")
        self.D_4.setIconSize(QtCore.QSize(50, 50))
        self.D_4.setObjectName("D_4")
        self.C_3 = QtWidgets.QPushButton(Checkers)
        self.C_3.setGeometry(QtCore.QRect(170, 200, 60, 60))
        self.C_3.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.C_3.setText("")
        self.C_3.setIconSize(QtCore.QSize(50, 50))
        self.C_3.setObjectName("C_3")
        self.C_1 = QtWidgets.QPushButton(Checkers)
        self.C_1.setGeometry(QtCore.QRect(50, 200, 60, 60))
        self.C_1.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.C_1.setText("")
        self.C_1.setIconSize(QtCore.QSize(50, 50))
        self.C_1.setObjectName("C_1")
        self.C_5 = QtWidgets.QPushButton(Checkers)
        self.C_5.setGeometry(QtCore.QRect(290, 200, 60, 60))
        self.C_5.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.C_5.setText("")
        self.C_5.setIconSize(QtCore.QSize(50, 50))
        self.C_5.setObjectName("C_5")
        self.C_4 = QtWidgets.QPushButton(Checkers)
        self.C_4.setGeometry(QtCore.QRect(230, 200, 60, 60))
        self.C_4.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.C_4.setText("")
        self.C_4.setIcon(icon)
        self.C_4.setIconSize(QtCore.QSize(50, 50))
        self.C_4.setObjectName("C_4")
        self.D_6 = QtWidgets.QPushButton(Checkers)
        self.D_6.setGeometry(QtCore.QRect(350, 260, 60, 60))
        self.D_6.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.D_6.setText("")
        self.D_6.setIconSize(QtCore.QSize(50, 50))
        self.D_6.setObjectName("D_6")
        self.D_7 = QtWidgets.QPushButton(Checkers)
        self.D_7.setGeometry(QtCore.QRect(410, 260, 60, 60))
        self.D_7.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.D_7.setText("")
        self.D_7.setIconSize(QtCore.QSize(50, 50))
        self.D_7.setObjectName("D_7")
        self.C_2 = QtWidgets.QPushButton(Checkers)
        self.C_2.setGeometry(QtCore.QRect(110, 200, 60, 60))
        self.C_2.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.C_2.setText("")
        self.C_2.setIcon(icon)
        self.C_2.setIconSize(QtCore.QSize(50, 50))
        self.C_2.setObjectName("C_2")
        self.D_2 = QtWidgets.QPushButton(Checkers)
        self.D_2.setGeometry(QtCore.QRect(110, 260, 60, 60))
        self.D_2.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.D_2.setText("")
        self.D_2.setIconSize(QtCore.QSize(50, 50))
        self.D_2.setObjectName("D_2")
        self.E_7 = QtWidgets.QPushButton(Checkers)
        self.E_7.setGeometry(QtCore.QRect(410, 320, 60, 60))
        self.E_7.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.E_7.setText("")
        self.E_7.setIconSize(QtCore.QSize(50, 50))
        self.E_7.setObjectName("E_7")
        self.G_8 = QtWidgets.QPushButton(Checkers)
        self.G_8.setGeometry(QtCore.QRect(470, 440, 60, 60))
        self.G_8.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.G_8.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Image/NW.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.G_8.setIcon(icon1)
        self.G_8.setIconSize(QtCore.QSize(50, 50))
        self.G_8.setObjectName("G_8")
        self.H_3 = QtWidgets.QPushButton(Checkers)
        self.H_3.setGeometry(QtCore.QRect(170, 500, 60, 60))
        self.H_3.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.H_3.setText("")
        self.H_3.setIcon(icon1)
        self.H_3.setIconSize(QtCore.QSize(50, 50))
        self.H_3.setObjectName("H_3")
        self.E_6 = QtWidgets.QPushButton(Checkers)
        self.E_6.setGeometry(QtCore.QRect(350, 320, 60, 60))
        self.E_6.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.E_6.setText("")
        self.E_6.setIconSize(QtCore.QSize(50, 50))
        self.E_6.setObjectName("E_6")
        self.E_3 = QtWidgets.QPushButton(Checkers)
        self.E_3.setGeometry(QtCore.QRect(170, 320, 60, 60))
        self.E_3.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.E_3.setText("")
        self.E_3.setIconSize(QtCore.QSize(50, 50))
        self.E_3.setObjectName("E_3")
        self.H_4 = QtWidgets.QPushButton(Checkers)
        self.H_4.setGeometry(QtCore.QRect(230, 500, 60, 60))
        self.H_4.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.H_4.setText("")
        self.H_4.setIconSize(QtCore.QSize(50, 50))
        self.H_4.setObjectName("H_4")
        self.G_1 = QtWidgets.QPushButton(Checkers)
        self.G_1.setGeometry(QtCore.QRect(50, 440, 60, 60))
        self.G_1.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.G_1.setText("")
        self.G_1.setIconSize(QtCore.QSize(50, 50))
        self.G_1.setObjectName("G_1")
        self.E_8 = QtWidgets.QPushButton(Checkers)
        self.E_8.setGeometry(QtCore.QRect(470, 320, 60, 60))
        self.E_8.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.E_8.setText("")
        self.E_8.setIconSize(QtCore.QSize(50, 50))
        self.E_8.setObjectName("E_8")
        self.E_2 = QtWidgets.QPushButton(Checkers)
        self.E_2.setGeometry(QtCore.QRect(110, 320, 60, 60))
        self.E_2.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.E_2.setText("")
        self.E_2.setIconSize(QtCore.QSize(50, 50))
        self.E_2.setObjectName("E_2")
        self.E_1 = QtWidgets.QPushButton(Checkers)
        self.E_1.setGeometry(QtCore.QRect(50, 320, 60, 60))
        self.E_1.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.E_1.setText("")
        self.E_1.setIconSize(QtCore.QSize(50, 50))
        self.E_1.setObjectName("E_1")
        self.F_8 = QtWidgets.QPushButton(Checkers)
        self.F_8.setGeometry(QtCore.QRect(470, 380, 60, 60))
        self.F_8.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.F_8.setText("")
        self.F_8.setIconSize(QtCore.QSize(50, 50))
        self.F_8.setObjectName("F_8")
        self.F_2 = QtWidgets.QPushButton(Checkers)
        self.F_2.setGeometry(QtCore.QRect(110, 380, 60, 60))
        self.F_2.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.F_2.setText("")
        self.F_2.setIconSize(QtCore.QSize(50, 50))
        self.F_2.setObjectName("F_2")
        self.F_5 = QtWidgets.QPushButton(Checkers)
        self.F_5.setGeometry(QtCore.QRect(290, 380, 60, 60))
        self.F_5.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.F_5.setText("")
        self.F_5.setIcon(icon1)
        self.F_5.setIconSize(QtCore.QSize(50, 50))
        self.F_5.setObjectName("F_5")
        self.H_1 = QtWidgets.QPushButton(Checkers)
        self.H_1.setGeometry(QtCore.QRect(50, 500, 60, 60))
        self.H_1.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.H_1.setText("")
        self.H_1.setIcon(icon1)
        self.H_1.setIconSize(QtCore.QSize(50, 50))
        self.H_1.setObjectName("H_1")
        self.H_2 = QtWidgets.QPushButton(Checkers)
        self.H_2.setGeometry(QtCore.QRect(110, 500, 60, 60))
        self.H_2.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.H_2.setText("")
        self.H_2.setIconSize(QtCore.QSize(50, 50))
        self.H_2.setObjectName("H_2")
        self.F_1 = QtWidgets.QPushButton(Checkers)
        self.F_1.setGeometry(QtCore.QRect(50, 380, 60, 60))
        self.F_1.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.F_1.setText("")
        self.F_1.setIcon(icon1)
        self.F_1.setIconSize(QtCore.QSize(50, 50))
        self.F_1.setObjectName("F_1")
        self.F_3 = QtWidgets.QPushButton(Checkers)
        self.F_3.setGeometry(QtCore.QRect(170, 380, 60, 60))
        self.F_3.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.F_3.setText("")
        self.F_3.setIcon(icon1)
        self.F_3.setIconSize(QtCore.QSize(50, 50))
        self.F_3.setObjectName("F_3")
        self.G_4 = QtWidgets.QPushButton(Checkers)
        self.G_4.setGeometry(QtCore.QRect(230, 440, 60, 60))
        self.G_4.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.G_4.setText("")
        self.G_4.setIcon(icon1)
        self.G_4.setIconSize(QtCore.QSize(50, 50))
        self.G_4.setObjectName("G_4")
        self.F_6 = QtWidgets.QPushButton(Checkers)
        self.F_6.setGeometry(QtCore.QRect(350, 380, 60, 60))
        self.F_6.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.F_6.setText("")
        self.F_6.setIconSize(QtCore.QSize(50, 50))
        self.F_6.setObjectName("F_6")
        self.G_2 = QtWidgets.QPushButton(Checkers)
        self.G_2.setGeometry(QtCore.QRect(110, 440, 60, 60))
        self.G_2.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.G_2.setText("")
        self.G_2.setIcon(icon1)
        self.G_2.setIconSize(QtCore.QSize(50, 50))
        self.G_2.setObjectName("G_2")
        self.H_8 = QtWidgets.QPushButton(Checkers)
        self.H_8.setGeometry(QtCore.QRect(470, 500, 60, 60))
        self.H_8.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.H_8.setText("")
        self.H_8.setIconSize(QtCore.QSize(50, 50))
        self.H_8.setObjectName("H_8")
        self.H_7 = QtWidgets.QPushButton(Checkers)
        self.H_7.setGeometry(QtCore.QRect(410, 500, 60, 60))
        self.H_7.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.H_7.setText("")
        self.H_7.setIcon(icon1)
        self.H_7.setIconSize(QtCore.QSize(50, 50))
        self.H_7.setObjectName("H_7")
        self.H_5 = QtWidgets.QPushButton(Checkers)
        self.H_5.setGeometry(QtCore.QRect(290, 500, 60, 60))
        self.H_5.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.H_5.setText("")
        self.H_5.setIcon(icon1)
        self.H_5.setIconSize(QtCore.QSize(50, 50))
        self.H_5.setObjectName("H_5")
        self.E_4 = QtWidgets.QPushButton(Checkers)
        self.E_4.setGeometry(QtCore.QRect(230, 320, 60, 60))
        self.E_4.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.E_4.setText("")
        self.E_4.setIconSize(QtCore.QSize(50, 50))
        self.E_4.setObjectName("E_4")
        self.F_4 = QtWidgets.QPushButton(Checkers)
        self.F_4.setGeometry(QtCore.QRect(230, 380, 60, 60))
        self.F_4.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.F_4.setText("")
        self.F_4.setIconSize(QtCore.QSize(50, 50))
        self.F_4.setObjectName("F_4")
        self.H_6 = QtWidgets.QPushButton(Checkers)
        self.H_6.setGeometry(QtCore.QRect(350, 500, 60, 60))
        self.H_6.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.H_6.setText("")
        self.H_6.setIconSize(QtCore.QSize(50, 50))
        self.H_6.setObjectName("H_6")
        self.F_7 = QtWidgets.QPushButton(Checkers)
        self.F_7.setGeometry(QtCore.QRect(410, 380, 60, 60))
        self.F_7.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.F_7.setText("")
        self.F_7.setIcon(icon1)
        self.F_7.setIconSize(QtCore.QSize(50, 50))
        self.F_7.setObjectName("F_7")
        self.G_5 = QtWidgets.QPushButton(Checkers)
        self.G_5.setGeometry(QtCore.QRect(290, 440, 60, 60))
        self.G_5.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.G_5.setText("")
        self.G_5.setIconSize(QtCore.QSize(50, 50))
        self.G_5.setObjectName("G_5")
        self.G_7 = QtWidgets.QPushButton(Checkers)
        self.G_7.setGeometry(QtCore.QRect(410, 440, 60, 60))
        self.G_7.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.G_7.setText("")
        self.G_7.setIconSize(QtCore.QSize(50, 50))
        self.G_7.setObjectName("G_7")
        self.G_3 = QtWidgets.QPushButton(Checkers)
        self.G_3.setGeometry(QtCore.QRect(170, 440, 60, 60))
        self.G_3.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.G_3.setText("")
        self.G_3.setIconSize(QtCore.QSize(50, 50))
        self.G_3.setObjectName("G_3")
        self.E_5 = QtWidgets.QPushButton(Checkers)
        self.E_5.setGeometry(QtCore.QRect(290, 320, 60, 60))
        self.E_5.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.E_5.setText("")
        self.E_5.setIconSize(QtCore.QSize(50, 50))
        self.E_5.setObjectName("E_5")
        self.G_6 = QtWidgets.QPushButton(Checkers)
        self.G_6.setGeometry(QtCore.QRect(350, 440, 60, 60))
        self.G_6.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.G_6.setText("")
        self.G_6.setIcon(icon1)
        self.G_6.setIconSize(QtCore.QSize(50, 50))
        self.G_6.setObjectName("G_6")
        self.Just = QtWidgets.QLabel(Checkers)
        self.Just.setGeometry(QtCore.QRect(30, 60, 520, 520))
        self.Just.setStyleSheet("background-color: rgb(199, 183, 161);")
        self.Just.setText("")
        self.Just.setObjectName("Just")
        self.Just2 = QtWidgets.QLabel(Checkers)
        self.Just2.setGeometry(QtCore.QRect(45, 75, 488, 488))
        self.Just2.setStyleSheet("background-color: rgb(98, 101, 120);")
        self.Just2.setText("")
        self.Just2.setObjectName("Just2")
        self.Menu = QtWidgets.QPushButton(Checkers)
        self.Menu.setGeometry(QtCore.QRect(30, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Menu.setFont(font)
        self.Menu.setStyleSheet("")
        self.Menu.setObjectName("Menu")
        self.Back = QtWidgets.QPushButton(Checkers)
        self.Back.setGeometry(QtCore.QRect(440, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Back.setFont(font)
        self.Back.setStyleSheet("")
        self.Back.setObjectName("Back")
        self.End_move = QtWidgets.QPushButton(Checkers)
        self.End_move.setGeometry(QtCore.QRect(570, 280, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.End_move.setFont(font)
        self.End_move.setStyleSheet("")
        self.End_move.setObjectName("End_move")
        self.Black = QtWidgets.QLCDNumber(Checkers)
        self.Black.setGeometry(QtCore.QRect(570, 80, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Black.setFont(font)
        self.Black.setStyleSheet("background-color: rgb(98, 101, 120);\n"
"color: rgb(157, 154, 135);")
        self.Black.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Black.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Black.setLineWidth(1)
        self.Black.setMidLineWidth(1)
        self.Black.setDigitCount(2)
        self.Black.setMode(QtWidgets.QLCDNumber.Dec)
        self.Black.setProperty("intValue", 12)
        self.Black.setObjectName("Black")
        self.White = QtWidgets.QLCDNumber(Checkers)
        self.White.setGeometry(QtCore.QRect(570, 510, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.White.setFont(font)
        self.White.setStyleSheet("background-color: rgb(199, 183, 161);\n"
"color: rgb(56, 72, 94);")
        self.White.setLineWidth(1)
        self.White.setDigitCount(2)
        self.White.setProperty("intValue", 12)
        self.White.setObjectName("White")
        self.Help = QtWidgets.QPushButton(Checkers)
        self.Help.setGeometry(QtCore.QRect(150, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Help.setFont(font)
        self.Help.setObjectName("pushButton")
        self.Just.raise_()
        self.Just2.raise_()
        self.A_1.raise_()
        self.A_2.raise_()
        self.A_3.raise_()
        self.A_5.raise_()
        self.A_6.raise_()
        self.A_4.raise_()
        self.A_7.raise_()
        self.A_8.raise_()
        self.B_6.raise_()
        self.B_7.raise_()
        self.B_8.raise_()
        self.B_3.raise_()
        self.B_1.raise_()
        self.B_5.raise_()
        self.B_4.raise_()
        self.B_2.raise_()
        self.C_6.raise_()
        self.D_5.raise_()
        self.D_1.raise_()
        self.C_7.raise_()
        self.C_8.raise_()
        self.D_8.raise_()
        self.D_3.raise_()
        self.D_4.raise_()
        self.C_3.raise_()
        self.C_1.raise_()
        self.C_5.raise_()
        self.C_4.raise_()
        self.D_6.raise_()
        self.D_7.raise_()
        self.C_2.raise_()
        self.D_2.raise_()
        self.E_7.raise_()
        self.G_8.raise_()
        self.H_3.raise_()
        self.E_6.raise_()
        self.E_3.raise_()
        self.H_4.raise_()
        self.G_1.raise_()
        self.E_8.raise_()
        self.E_2.raise_()
        self.E_1.raise_()
        self.F_8.raise_()
        self.F_2.raise_()
        self.F_5.raise_()
        self.H_1.raise_()
        self.H_2.raise_()
        self.F_1.raise_()
        self.F_3.raise_()
        self.G_4.raise_()
        self.F_6.raise_()
        self.G_2.raise_()
        self.H_8.raise_()
        self.H_7.raise_()
        self.H_5.raise_()
        self.E_4.raise_()
        self.F_4.raise_()
        self.H_6.raise_()
        self.F_7.raise_()
        self.G_5.raise_()
        self.G_7.raise_()
        self.G_3.raise_()
        self.E_5.raise_()
        self.G_6.raise_()
        self.Menu.raise_()
        self.Back.raise_()
        self.End_move.raise_()
        self.Black.raise_()
        self.White.raise_()
        self.Help.raise_()

        self.retranslateUi(Checkers)
        QtCore.QMetaObject.connectSlotsByName(Checkers)

    def retranslateUi(self, Checkers):
        _translate = QtCore.QCoreApplication.translate
        Checkers.setWindowTitle(_translate("Checkers", "Шашки"))
        self.Menu.setText(_translate("Checkers", "Меню"))
        self.Back.setText(_translate("Checkers", "Назад"))
        self.End_move.setText(_translate("Checkers", "Завершить\n"
"Ход"))
        self.Help.setText(_translate("Checkers", "Справка"))
