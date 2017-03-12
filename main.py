# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 623)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 581))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.redmineTasks = QtWidgets.QTableView(self.horizontalLayoutWidget)
        self.redmineTasks.setObjectName("redmineTasks")
        self.verticalLayout_2.addWidget(self.redmineTasks)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.evoTasks = QtWidgets.QTableView(self.horizontalLayoutWidget)
        self.evoTasks.setObjectName("evoTasks")
        self.verticalLayout_2.addWidget(self.evoTasks)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 19, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnEvoTaskGenerate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnEvoTaskGenerate.setObjectName("btnEvoTaskGenerate")
        self.verticalLayout.addWidget(self.btnEvoTaskGenerate)
        self.btnSendToRedmine = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnSendToRedmine.setObjectName("btnSendToRedmine")
        self.verticalLayout.addWidget(self.btnSendToRedmine)
        self.btnSendToEvo = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnSendToEvo.setObjectName("btnSendToEvo")
        self.verticalLayout.addWidget(self.btnSendToEvo, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_Hamster = QtWidgets.QMenu(self.menubar)
        self.menu_Hamster.setObjectName("menu_Hamster")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHamster = QtWidgets.QAction(MainWindow)
        self.actionHamster.setObjectName("actionHamster")
        self.actionRedmine = QtWidgets.QAction(MainWindow)
        self.actionRedmine.setObjectName("actionRedmine")
        self.menu_Hamster.addAction(self.actionHamster)
        self.menu_Hamster.addAction(self.actionRedmine)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_Hamster.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Redmine"))
        self.label_2.setText(_translate("MainWindow", "Evolution"))
        self.btnEvoTaskGenerate.setText(_translate("MainWindow", "Сгенерировать записи evo"))
        self.btnSendToRedmine.setText(_translate("MainWindow", "Отправить в redmine"))
        self.btnSendToEvo.setText(_translate("MainWindow", "Отправить в evo"))
        self.menu.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_2.setTitle(_translate("MainWindow", "Сопоставление проектов"))
        self.menu_Hamster.setTitle(_translate("MainWindow", "Импорт часов"))
        self.actionHamster.setText(_translate("MainWindow", "Hamster"))
        self.actionRedmine.setText(_translate("MainWindow", "Redmine"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

