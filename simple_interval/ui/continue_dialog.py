# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/continue_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(278, 163)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.cur_alarm_name = QtWidgets.QLabel(Form)
        self.cur_alarm_name.setObjectName("cur_alarm_name")
        self.horizontalLayout_2.addWidget(self.cur_alarm_name, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.continue_button = QtWidgets.QPushButton(Form)
        self.continue_button.setObjectName("continue_button")
        self.horizontalLayout.addWidget(self.continue_button)
        self.cancel_button = QtWidgets.QPushButton(Form)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Завершено:"))
        self.cur_alarm_name.setText(_translate("Form", "TextLabel"))
        self.label.setText(_translate("Form", "Продолжить?"))
        self.continue_button.setText(_translate("Form", "continue"))
        self.cancel_button.setText(_translate("Form", "cancel"))

