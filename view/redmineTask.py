# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'redmineTask.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RedmineTaskDialog(object):
    def setupUi(self, RedmineTaskDialog):
        RedmineTaskDialog.setObjectName("RedmineTaskDialog")
        RedmineTaskDialog.resize(288, 247)
        self.gridLayout = QtWidgets.QGridLayout(RedmineTaskDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(RedmineTaskDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.taskNubmer = QtWidgets.QLineEdit(RedmineTaskDialog)
        self.taskNubmer.setObjectName("taskNubmer")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.taskNubmer)
        self.label_2 = QtWidgets.QLabel(RedmineTaskDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.redmineProject = QtWidgets.QLabel(RedmineTaskDialog)
        self.redmineProject.setText("")
        self.redmineProject.setObjectName("redmineProject")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.redmineProject)
        self.label_4 = QtWidgets.QLabel(RedmineTaskDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.hours = QtWidgets.QDoubleSpinBox(RedmineTaskDialog)
        self.hours.setObjectName("hours")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.hours)
        self.label_5 = QtWidgets.QLabel(RedmineTaskDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.date = QtWidgets.QDateEdit(RedmineTaskDialog)
        self.date.setDate(QtCore.QDate(2017, 1, 1))
        self.date.setObjectName("date")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.date)
        self.label_6 = QtWidgets.QLabel(RedmineTaskDialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.comment = QtWidgets.QTextEdit(RedmineTaskDialog)
        self.comment.setObjectName("comment")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comment)
        self.label_3 = QtWidgets.QLabel(RedmineTaskDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.taskName = QtWidgets.QLabel(RedmineTaskDialog)
        self.taskName.setText("")
        self.taskName.setObjectName("taskName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.taskName)
        self.label_7 = QtWidgets.QLabel(RedmineTaskDialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.redmineCombo = QtWidgets.QComboBox(RedmineTaskDialog)
        self.redmineCombo.setObjectName("redmineCombo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.redmineCombo)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(RedmineTaskDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(RedmineTaskDialog)
        self.buttonBox.accepted.connect(RedmineTaskDialog.accept)
        self.buttonBox.rejected.connect(RedmineTaskDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RedmineTaskDialog)

    def retranslateUi(self, RedmineTaskDialog):
        _translate = QtCore.QCoreApplication.translate
        RedmineTaskDialog.setWindowTitle(_translate("RedmineTaskDialog", "Задача redmine"))
        self.label.setText(_translate("RedmineTaskDialog", "Задача"))
        self.label_2.setText(_translate("RedmineTaskDialog", "Проект"))
        self.label_4.setText(_translate("RedmineTaskDialog", "Часы"))
        self.label_5.setText(_translate("RedmineTaskDialog", "Дата"))
        self.label_6.setText(_translate("RedmineTaskDialog", "Комментарий"))
        self.label_3.setText(_translate("RedmineTaskDialog", "Название"))
        self.label_7.setText(_translate("RedmineTaskDialog", "redmine"))

