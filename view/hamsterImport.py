# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hamsterImport.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HamsterImport(object):
    def setupUi(self, HamsterImport):
        HamsterImport.setObjectName("HamsterImport")
        HamsterImport.resize(288, 143)
        self.gridLayout = QtWidgets.QGridLayout(HamsterImport)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(HamsterImport)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.dateFrom = QtWidgets.QDateEdit(HamsterImport)
        self.dateFrom.setDate(QtCore.QDate(2017, 1, 1))
        self.dateFrom.setObjectName("dateFrom")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateFrom)
        self.label = QtWidgets.QLabel(HamsterImport)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.dateTo = QtWidgets.QDateEdit(HamsterImport)
        self.dateTo.setDate(QtCore.QDate(2017, 1, 2))
        self.dateTo.setObjectName("dateTo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateTo)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(HamsterImport)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(HamsterImport)
        self.buttonBox.accepted.connect(HamsterImport.accept)
        self.buttonBox.rejected.connect(HamsterImport.reject)
        QtCore.QMetaObject.connectSlotsByName(HamsterImport)

    def retranslateUi(self, HamsterImport):
        _translate = QtCore.QCoreApplication.translate
        HamsterImport.setWindowTitle(_translate("HamsterImport", "Задача evolution"))
        self.label_5.setText(_translate("HamsterImport", "Дата начала"))
        self.label.setText(_translate("HamsterImport", "Дата окончания"))

