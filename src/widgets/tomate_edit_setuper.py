# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/tomate_view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(528, 48)
        Form.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMaximumSize(QtCore.QSize(15, 25))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.up = QtWidgets.QPushButton(self.widget)
        self.up.setText("")
        self.up.setFlat(False)
        self.up.setObjectName("up")
        self.verticalLayout.addWidget(self.up)
        self.down = QtWidgets.QPushButton(self.widget)
        self.down.setText("")
        self.down.setObjectName("down")
        self.verticalLayout.addWidget(self.down)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.widget)
        self.tomat_name = QtWidgets.QLineEdit(Form)
        self.tomat_name.setObjectName("tomat_name")
        self.horizontalLayout.addWidget(self.tomat_name)
        self.spin_minute = QtWidgets.QSpinBox(Form)
        self.spin_minute.setMaximum(999)
        self.spin_minute.setObjectName("spin_minute")
        self.horizontalLayout.addWidget(self.spin_minute)
        self.spin_second = QtWidgets.QSpinBox(Form)
        self.spin_second.setMaximum(59)
        self.spin_second.setObjectName("spin_second")
        self.horizontalLayout.addWidget(self.spin_second)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setMinimumSize(QtCore.QSize(50, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(62, 30))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add = QtWidgets.QPushButton(self.widget_2)
        self.add.setText("")
        self.add.setObjectName("add")
        self.horizontalLayout_3.addWidget(self.add)
        self.remove = QtWidgets.QPushButton(self.widget_2)
        self.remove.setText("")
        self.remove.setObjectName("remove")
        self.horizontalLayout_3.addWidget(self.remove)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

