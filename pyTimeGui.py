from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox

from model.evolutionTaskModel import EvolutionTasksModel
from model.redmineTaskModel import RedmineTasksModel

from view.evolutionTask import Ui_EvolutionTaskDialog
from view.main import Ui_MainWindow
from view.redmineTask import Ui_RedmineTaskDialog
from view.settingsExtended import Ui_Setting
from view.hamsterImport import Ui_HamsterImport
from view.redmineEvoProjectsExtended import Ui_RedminEevoProjectsExtended

from model.configWorker import ConfigWorker
from model.redmineWorker import RedmineWorker
from model.hamsterWorker import HamsterWorker
from model.evolutionApiWorker import EvoWorker

import datetime

class PyTimeGui(Ui_MainWindow):
    def __init__(self, mainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(mainWindow)

        redmineTasksData = [
            ['10474', '05.12.2016', '2', 'Разработка апи', 'Evolution', 'http://redmine.stolplit.ru', 'lalala'],
            ['34965', '11.12.2016', '3.5', 'Тестирование и выкат', 'Столплит', 'https://redmine.stolplit.ru', 'lololo']
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
        self.importFromHamster.triggered.connect(self.importTasksFromHamster)
        self.setProjects.triggered.connect(self.setRedmineEvoProjects)

        self.redmineTasks.setModel(RedmineTasksModel(redmineTasksData))
        self.evoTasks.setModel(EvolutionTasksModel(evolutionTasksData))

        self.btnEvoTaskGenerate.clicked.connect(self.generateEvoTasks)

        self.btnSendToEvo.clicked.connect(self.sendToEvo)

        self.config = ConfigWorker()

        evoConfig = self.config.getEvolutionData()
        if evoConfig[2] != "":
            self.evoWorker = EvoWorker(evoConfig[0], evoConfig[2])
        else:
            self.evoWorker = False

        self.redmineWorkers = []
        redmineData = self.config.getRedminesData()
        for (i, item) in enumerate(redmineData):
            redmineWorker = RedmineWorker(item[0])
            redmineWorker.initWithKey(item[2])
            self.redmineWorkers.append(redmineWorker)

        self.refreshAllTime()

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

        self.refreshAllTime()

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
            if len(task[1]) == 10:
                dialog.ui.date.setDate(QtCore.QDate.fromString(task[1], 'dd.MM.yyyy'))
            else:
                dialog.ui.date.setDate(QtCore.QDate.fromString(task[1], 'dd.MM.yy'))

            dialog.ui.comment.setText(task[3])
            dialog.ui.taskName.setText(task[6])

            if dialog.exec_() == QDialog.Accepted:
                redmineIndexValue = dialog.ui.redmineCombo.itemData(dialog.ui.redmineCombo.currentIndex())
                redmineWorker = RedmineWorker(redminesData[redmineIndexValue][0])
                redmineWorker.initWithKey(redminesData[redmineIndexValue][2])
                taskNumber = dialog.ui.taskNubmer.text()

                projectName = dialog.ui.redmineProject.text()
                taskName = ""
                if taskNumber != "":
                    taskData = redmineWorker.getTaskData(int(taskNumber))

                    if taskData != False:
                        projectName = taskData[2]
                        taskName = taskData[1]

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

        self.refreshAllTime()

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

        self.refreshAllTime()

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

        dialog.ui.init(self.config, self.evoWorker, self.redmineWorkers)

        dialog.exec_()

    def sendTimeToRedmine(self):
        redmineTasks = self.redmineTasks.model().data
        redmineData = self.config.getRedminesData()

        redmineIndexes = {}
        for (i, item) in enumerate(redmineData):
            redmineIndexes[item[0]] = i

        msg = ""
        for task in redmineTasks:
            if task[5] in redmineIndexes:
                if len(task[1]) == 10:
                    date = datetime.datetime.strptime(task[1], "%d.%m.%Y").date().strftime('%Y-%m-%d')
                else:
                    date = datetime.datetime.strptime(task[1], "%d.%m.%y").date().strftime('%Y-%m-%d')

                redmine = self.redmineWorkers[redmineIndexes[task[5]]]
                if redmine.setTime(task[0], date, task[2], task[3]):
                    msg += task[0] + " добавлена в redmine\n"
                else:
                    msg += task[0] + " " + task[3] + " - что-то пошло не так\n"

        if msg != "":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(msg)
            msgBox.exec_()

    def importTasksFromHamster(self):

        dialog = QDialog()
        dialog.ui = Ui_HamsterImport()
        dialog.ui.setupUi(dialog)

        dialog.ui.dateFrom.setDate(QtCore.QDate.currentDate())
        dialog.ui.dateTo.setDate(QtCore.QDate.currentDate().addDays(1))

        if dialog.exec_() == QDialog.Accepted:
            dayFrom = dialog.ui.dateFrom.text()
            dayTo = dialog.ui.dateTo.text()

            if len(dayFrom) == 10:
                dayFrom = datetime.datetime.strptime(dayFrom, "%d.%m.%Y").date()
            else:
                dayFrom = datetime.datetime.strptime(dayFrom, "%d.%m.%y").date()

            if len(dayTo) == 10:
                dayTo = datetime.datetime.strptime(dayTo, "%d.%m.%Y").date()
            else:
                dayTo = datetime.datetime.strptime(dayTo, "%d.%m.%y").date()

            hamsterWorker = HamsterWorker()
            hamsterTasks = hamsterWorker.getTasksByDates(dayFrom, dayTo)

            if hamsterTasks != False:
                self.redmineTasks.model().data = []
                self.redmineTasks.model().layoutChanged.emit()

                count = 0
                for task in hamsterTasks.values():

                    redmineId = int(self.config.getRedmineIdByHamsterProjectName(task['cat']))
                    redmineWorker = self.redmineWorkers[redmineId]
                    taskRedmine = redmineWorker.getTaskData(task['task_id'])
                    if taskRedmine is False:
                        taskName = ""
                        taskProject = task['cat']
                    else:
                        taskName = taskRedmine[1]
                        taskProject = taskRedmine[2]

                    self.redmineTasks.model().data.append([
                        str(task['task_id']),
                        task['start'].strftime('%d.%m.%Y'),
                        str(task['hours']),
                        task['description'],
                        taskProject,
                        redmineWorker.getUrl(),
                        taskName
                    ])
                    self.redmineTasks.model().layoutChanged.emit()
                    count += 1

                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Импортировано:" + str(count))
                msgBox.exec_()
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Не найден файл базы данных Hamster")
                msgBox.exec_()

        self.refreshAllTime()

        self.evoTasks.model().data = []
        self.evoTasks.model().layoutChanged.emit()

    def setRedmineEvoProjects(self):
        dialog = QDialog()
        dialog.ui = Ui_RedminEevoProjectsExtended()
        dialog.ui.setupUi(dialog)

        dialog.ui.init(self.config)

        dialog.exec_()

    def generateEvoTasks(self):
        redmineTasks = self.redmineTasks.model().data
        evoProjects = self.evoWorker.getProjects()

        evoProjectNames = []
        evoProjectNamesToId = {}
        evoProjectIdToName = {}
        if evoProjects != False:
            for project in evoProjects:
                evoProjectNames.append(project['title'])
                evoProjectNamesToId[project['title']] = project['id']
                evoProjectIdToName[project['id']] = project['title']

        self.evoTasks.model().data = []
        for task in redmineTasks:
            redmineProject = task[4]
            evoProjectId = int(self.config.getEvoIdByRedmineProjectName(redmineProject))
            if evoProjectId in evoProjectIdToName:
                evoProject = evoProjectIdToName[evoProjectId]
            else:
                evoProject = "!!! " + redmineProject

            if task[6] == '':
                evoFormul = task[3]
            else:
                evoFormul = task[6]

            self.evoTasks.model().data.append([
                evoFormul,
                task[1],
                task[2],
                task[0],
                evoProject
            ])
            self.evoTasks.model().layoutChanged.emit()

        self.refreshAllTime()

    def refreshAllTime(self):
        allTime = 0
        for task in self.redmineTasks.model().data:
            allTime += float(task[2])
        self.fullTimeLabel.setText(str(allTime))

    def sendToEvo(self):
        evoTasks = self.evoTasks.model().data

        evoProjects = self.evoWorker.getProjects()
        if evoProjects != False:
            evoProjectNames = []
            evoProjectNamesToId = {}
            evoProjectIdToName = {}
            for project in evoProjects:
                evoProjectNames.append(project['title'])
                evoProjectNamesToId[project['title']] = project['id']
                evoProjectIdToName[project['id']] = project['title']

        evoData = self.config.getEvolutionData()
        employerId = evoData[3]

        msg = ""

        for task in evoTasks:
            projectId = evoProjectNamesToId[task[4]]
            result = self.evoWorker.sendTask(
                task[0],
                task[1],
                task[2],
                task[3],
                employerId,
                projectId
            )
            if result is False:
                msg += task[0] + " failed\n"
            else:
                msg += task[0] + " success\n"

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Данные отправлены:\n" + msg)
        msgBox.exec_()