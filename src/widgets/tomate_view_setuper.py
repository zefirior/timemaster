# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/tomate_container.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tomate_view(object):
    def setupUi(self, Tomate_view):
        Tomate_view.setObjectName("Tomate_view")
        Tomate_view.resize(456, 46)
        Tomate_view.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Tomate_view)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Tomate_view)
        self.widget.setMaximumSize(QtCore.QSize(15, 25))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addWidget(self.widget)
        self.tomat_name = QtWidgets.QLineEdit(Tomate_view)
        self.tomat_name.setEnabled(False)
        self.tomat_name.setObjectName("tomat_name")
        self.horizontalLayout.addWidget(self.tomat_name)
        self.minute = QtWidgets.QLineEdit(Tomate_view)
        self.minute.setEnabled(False)
        self.minute.setMaximumSize(QtCore.QSize(60, 16777215))
        self.minute.setObjectName("minute")
        self.horizontalLayout.addWidget(self.minute)
        self.second = QtWidgets.QLineEdit(Tomate_view)
        self.second.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.second.sizePolicy().hasHeightForWidth())
        self.second.setSizePolicy(sizePolicy)
        self.second.setMaximumSize(QtCore.QSize(60, 16777215))
        self.second.setObjectName("second")
        self.horizontalLayout.addWidget(self.second)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Tomate_view)
        QtCore.QMetaObject.connectSlotsByName(Tomate_view)

    def retranslateUi(self, Tomate_view):
        _translate = QtCore.QCoreApplication.translate
        Tomate_view.setWindowTitle(_translate("Tomate_view", "Form"))

