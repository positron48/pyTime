from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox

from model.evolutionTaskModel import EvolutionTasksModel
from model.redmineTaskModel import RedmineTasksModel
from view.evolutionTask import Ui_EvolutionTaskDialog

from view.main import Ui_MainWindow
from view.redmineTask import Ui_RedmineTaskDialog
from view.settingsExtended import Ui_Setting
from model.configWorker import ConfigWorker
from model.redmineWorker import RedmineWorker

import datetime

class PyTimeGui(Ui_MainWindow):
    def __init__(self, mainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(mainWindow)

        redmineTasksData = [
            ['41307', '05.12.2016', '2', 'Разработка апи', 'Evolution', 'http://redmine.skillum.ru', 'lalala'],
            #['34965', '11.12.2016', '3.5', 'Тестирование и выкат', 'Столплит', 'http://redmine.stolplit.ru', 'lololo']
        ]

        evolutionTasksData = [['33254', '05.12.2016', '2', 'Разработка апи', 'Evolution']]

        self.btnRedmineTaskAdd.clicked.connect(self.addRedmineTask)
        self.btnRedmineTaskEdit.clicked.connect(self.editRedmineTask)
        self.redmineTasks.doubleClicked.connect(self.editRedmineTask)
        self.btnRedmineTaskDelete.clicked.connect(self.removeRedmineTask)

        self.btnEvoTaskAdd.clicked.connect(self.addEvoTask)
        self.btnEvoTaskEdit.clicked.connect(self.editEvoTask)
        self.evoTasks.doubleClicked.connect(self.editEvoTask)
        self.btnEvoTaskDelete.clicked.connect(self.removeEvoTask)

        self.btnSendToRedmine.clicked.connect(self.sendTimeToRedmine)

        self.menuSettings.triggered.connect(self.settings)

        self.redmineTasks.setModel(RedmineTasksModel(redmineTasksData))
        self.evoTasks.setModel(EvolutionTasksModel(evolutionTasksData))
        self.config = ConfigWorker()

    def bindTable(self, tableView, my_array):
        model = RedmineTasksModel(my_array)
        tableView.setModel(model)

    def addRedmineTask(self):
        dialog = QDialog()
        dialog.ui = Ui_RedmineTaskDialog()
        dialog.ui.setupUi(dialog)
        dialog.ui.date.setDate(QtCore.QDate.currentDate())
        dialog.ui.hours.setValue(8)

        redminesData = self.config.getRedminesData()
        for (i, item) in enumerate(redminesData):
            dialog.ui.redmineCombo.addItem(item[0], i)

        if dialog.exec_() == QDialog.Accepted:

            redmineIndexValue = dialog.ui.redmineCombo.itemData(dialog.ui.redmineCombo.currentIndex())
            redmineWorker = RedmineWorker(redminesData[redmineIndexValue][0])
            redmineWorker.initWithKey(redminesData[redmineIndexValue][2])
            taskData = redmineWorker.getTaskData(int(dialog.ui.taskNubmer.text()))
            if taskData != False:
                projectName = taskData[2]
                taskName = taskData[1]
            else:
                projectName = dialog.ui.redmineProject.text()
                taskName = ""

            self.redmineTasks.model().data.append([
                dialog.ui.taskNubmer.text(),
                dialog.ui.date.text(),
                dialog.ui.hours.value(),
                dialog.ui.comment.toPlainText(),
                projectName,
                dialog.ui.redmineCombo.itemText(dialog.ui.redmineCombo.currentIndex()),
                taskName
            ])
            self.redmineTasks.model().layoutChanged.emit()

    def editRedmineTask(self):
        index = self.redmineTasks.selectedIndexes()
        if len(index) > 0:
            index = index[0].row()
            task = self.redmineTasks.model().data[index]
            dialog = QDialog()
            dialog.ui = Ui_RedmineTaskDialog()
            dialog.ui.setupUi(dialog)

            redminesData = self.config.getRedminesData()
            for (i, item) in enumerate(redminesData):
                dialog.ui.redmineCombo.addItem(item[0], i)
                if item[0] == task[5]:
                    dialog.ui.redmineCombo.setCurrentIndex(i)

            dialog.ui.taskNubmer.setText(task[0])
            dialog.ui.redmineProject.setText(task[4])
            dialog.ui.hours.setValue(float(task[2]))
            dialog.ui.date.setDate(QtCore.QDate.fromString(task[1], 'dd.MM.yyyy'))
            dialog.ui.comment.setText(task[3])
            dialog.ui.taskName.setText(task[6])

            if dialog.exec_() == QDialog.Accepted:
                redmineIndexValue = dialog.ui.redmineCombo.itemData(dialog.ui.redmineCombo.currentIndex())
                redmineWorker = RedmineWorker(redminesData[redmineIndexValue][0])
                redmineWorker.initWithKey(redminesData[redmineIndexValue][2])
                taskData = redmineWorker.getTaskData(int(dialog.ui.taskNubmer.text()))
                if taskData != False:
                    projectName = taskData[2]
                    taskName = taskData[1]
                else:
                    projectName = dialog.ui.redmineProject.text()
                    taskName = ""

                self.redmineTasks.model().data[index] = [
                    dialog.ui.taskNubmer.text(),
                    dialog.ui.date.text(),
                    dialog.ui.hours.value(),
                    dialog.ui.comment.toPlainText(),
                    projectName,
                    dialog.ui.redmineCombo.itemText(dialog.ui.redmineCombo.currentIndex()),
                    taskName
                ]

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Выберите задачу для изменения")
            msg.exec_()

    def removeRedmineTask(self):
        index = self.redmineTasks.selectedIndexes()
        if len(index) > 0:
            index = index[0].row()
            del self.redmineTasks.model().data[index]
            self.redmineTasks.model().layoutChanged.emit()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Выберите задачу для удаления")
            msg.exec_()

    def addEvoTask(self):
        dialog = QDialog()
        dialog.ui = Ui_EvolutionTaskDialog()
        dialog.ui.setupUi(dialog)
        dialog.ui.date.setDate(QtCore.QDate.currentDate())
        dialog.ui.hours.setValue(8)

        if dialog.exec_() == QDialog.Accepted:
            self.evoTasks.model().data.append([
                dialog.ui.formul.text(),
                dialog.ui.date.text(),
                dialog.ui.hours.value(),
                dialog.ui.comment.toPlainText(),
                dialog.ui.project.text()
            ])
            self.evoTasks.model().layoutChanged.emit()

    def editEvoTask(self):
        index = self.evoTasks.selectedIndexes()
        if len(index) > 0:
            index = index[0].row()
            task = self.evoTasks.model().data[index]
            dialog = QDialog()
            dialog.ui = Ui_EvolutionTaskDialog()
            dialog.ui.setupUi(dialog)

            dialog.ui.formul.setText(task[0])
            dialog.ui.project.setText(task[4])
            dialog.ui.hours.setValue(float(task[2]))
            dialog.ui.date.setDate(QtCore.QDate.fromString(task[1], 'dd.MM.yyyy'))
            dialog.ui.comment.setText(task[3])

            if dialog.exec_() == QDialog.Accepted:
                self.evoTasks.model().data[index] = [
                    dialog.ui.formul.text(),
                    dialog.ui.date.text(),
                    dialog.ui.hours.value(),
                    dialog.ui.comment.toPlainText(),
                    dialog.ui.project.text()
                ]

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Выберите задачу для изменения")
            msg.exec_()

    def removeEvoTask(self):
        index = self.evoTasks.selectedIndexes()
        if len(index) > 0:
            index = index[0].row()
            del self.evoTasks.model().data[index]
            self.evoTasks.model().layoutChanged.emit()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Выберите задачу для удаления")
            msg.exec_()

    def settings(self):
        dialog = QDialog()
        dialog.ui = Ui_Setting()
        dialog.ui.setupUi(dialog)

        dialog.ui.init()

        dialog.exec_()

    def sendTimeToRedmine(self):
        redmineTasks = self.redmineTasks.model().data
        redminesApi = []
        redmineData = self.config.getRedminesData()

        redmineIndexes = {}

        for (i, item) in enumerate(redmineData):
            redmineWorker = RedmineWorker(item[0])
            redmineWorker.initWithKey(item[2])
            redminesApi.append(redmineWorker)
            redmineIndexes[item[0]] = i

        for task in redmineTasks:
            msg = ""
            if task[5] in redmineIndexes:
                date = datetime.datetime.strptime(task[1], "%d.%m.%Y").date().strftime('%Y-%m-%d')

                redmine = redminesApi[redmineIndexes[task[5]]]
                if redmine.setTime(task[0], date, task[2], task[3]):
                    msg += task[0] + " добавлена в redmine\n"
                else:
                    msg += task[0] + " - что-то пошло не так\n"

            if msg != "":
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText(msg)
                msgBox.exec_()