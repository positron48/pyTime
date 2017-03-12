# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evolutionTask.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EvolutionTaskDialog(object):
    def setupUi(self, EvolutionTaskDialog):
        EvolutionTaskDialog.setObjectName("EvolutionTaskDialog")
        EvolutionTaskDialog.resize(288, 247)
        self.gridLayout = QtWidgets.QGridLayout(EvolutionTaskDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(EvolutionTaskDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.formul = QtWidgets.QLineEdit(EvolutionTaskDialog)
        self.formul.setObjectName("formul")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.formul)
        self.label_2 = QtWidgets.QLabel(EvolutionTaskDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(EvolutionTaskDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.hours = QtWidgets.QDoubleSpinBox(EvolutionTaskDialog)
        self.hours.setObjectName("hours")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.hours)
        self.label_5 = QtWidgets.QLabel(EvolutionTaskDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(EvolutionTaskDialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.comment = QtWidgets.QTextEdit(EvolutionTaskDialog)
        self.comment.setObjectName("comment")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comment)
        self.lineEdit = QtWidgets.QLineEdit(EvolutionTaskDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.date = QtWidgets.QDateEdit(EvolutionTaskDialog)
        self.date.setDate(QtCore.QDate(2017, 1, 1))
        self.date.setObjectName("date")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.date)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(EvolutionTaskDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(EvolutionTaskDialog)
        self.buttonBox.accepted.connect(EvolutionTaskDialog.accept)
        self.buttonBox.rejected.connect(EvolutionTaskDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EvolutionTaskDialog)

    def retranslateUi(self, EvolutionTaskDialog):
        _translate = QtCore.QCoreApplication.translate
        EvolutionTaskDialog.setWindowTitle(_translate("EvolutionTaskDialog", "Задача evolution"))
        self.label.setText(_translate("EvolutionTaskDialog", "Формулировка"))
        self.label_2.setText(_translate("EvolutionTaskDialog", "Проект"))
        self.label_4.setText(_translate("EvolutionTaskDialog", "Часы"))
        self.label_5.setText(_translate("EvolutionTaskDialog", "Дата"))
        self.label_6.setText(_translate("EvolutionTaskDialog", "Комментарий"))

