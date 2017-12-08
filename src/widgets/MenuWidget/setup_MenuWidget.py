# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuWidget(object):
    def setupUi(self, MenuWidget):
        MenuWidget.setObjectName("MenuWidget")
        MenuWidget.resize(155, 242)
        MenuWidget.setMinimumSize(QtCore.QSize(50, 100))
        MenuWidget.setWindowOpacity(0.0)
        MenuWidget.setAutoFillBackground(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(MenuWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 151, 239))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        self.label.setMaximumSize(QtCore.QSize(40, 40))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setPixmap(QtGui.QPixmap("../content/image/512px-Reorder_font_awesome.svg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.pushButton_3 = HidButton(self.verticalLayoutWidget)
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.verticalLayout_2.addWidget(self.pushButton_3)
        # self.pushButton = HidButton(self.verticalLayoutWidget)
        # self.pushButton.setObjectName("pushButton")
        # self.verticalLayout_2.addWidget(self.pushButton)
        # self.pushButton_2 = HidButton(self.verticalLayoutWidget)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.verticalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        # self.retranslateUi(MenuWidget)
        QtCore.QMetaObject.connectSlotsByName(MenuWidget)

    # def retranslateUi(self, MenuWidget):
    #     _translate = QtCore.QCoreApplication.translate
    #     MenuWidget.setWindowTitle(_translate("MenuWidget", "Menu"))
    #     self.pushButton_3.setText(_translate("MenuWidget", "PushButton"))
    #     self.pushButton.setText(_translate("MenuWidget", "PushButton"))
    #     self.pushButton_2.setText(_translate("MenuWidget", "PushButton"))

