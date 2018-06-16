# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(200, 200, 800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 161, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        # self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.verticalLayout_4.addWidget(self.pushButton_3)
        # self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.verticalLayout_4.addWidget(self.pushButton_2)
        # self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        # self.pushButton.setObjectName("pushButton")
        # self.verticalLayout_4.addWidget(self.pushButton)
        # spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.verticalLayout_4.addItem(spacerItem)
        self.verticalFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame_2.setGeometry(QtCore.QRect(80, 9, 550, 431))
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 30))
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
        # self.pushButton_3.setText(_translate("MainWindow", "Test"))
        # self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        # self.pushButton.setText(_translate("MainWindow", "PushButton"))
