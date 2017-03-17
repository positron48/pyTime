from view.redmineEvoProjects import Ui_RedminEevoProjects
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QCompleter
from PyQt5.QtCore import QStringListModel, QItemSelectionModel
from model.redmineWorker import RedmineWorker
from model.evolutionApiWorker import EvoWorker
from model.hamsterWorker import HamsterWorker
from model.redmineProjects import RedmineProjectsModel

class Ui_RedminEevoProjectsExtended(Ui_RedminEevoProjects):

    def init(self, config):
        self.config = config

        redmineData = self.config.getRedminesData()

        redmineProjects = []

        for (i, item) in enumerate(redmineData):
            redmineWorker = RedmineWorker(item[0])
            redmineWorker.initWithKey(item[2])

            projects = redmineWorker.getProjects()
            for project in projects:
                redmineProjects.append([project.id, project.name])

        projectsModel = RedmineProjectsModel(redmineProjects)
        self.redmineProjectsView.setModel(projectsModel)

        evolutionData = self.config.getEvolutionData()
        evoWorker = EvoWorker(evolutionData[0], evolutionData[2])
        evoProjects = evoWorker.getProjects()

        if evoProjects != False:
            self.evoProjectNames = []
            self.evoProjectNamesToId = {}
            self.evoProjectIdToName = {}
            for project in evoProjects:
                self.evoProjectNames.append(project['title'])
                self.evoProjectNamesToId[project['title']] = project['id']
                self.evoProjectIdToName[project['id']] = project['title']

            completer = QCompleter()
            self.evoProject.setCompleter(completer)

            model = QStringListModel()
            completer.setModel(model)
            model.setStringList(self.evoProjectNames)
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("При получении данных из evo произошла ошибка")
            msgBox.exec_()

        self.selectedIndex = 0

        self.redmineProjectsView.selectionModel().selectionChanged.connect(self.changeProject)
        self.saveRedmineEvoProject.clicked.connect(self.saveProject)

        Qindex = projectsModel.createIndex(0, 0)
        self.redmineProjectsView.selectionModel().select(Qindex, QItemSelectionModel.Select)

        self.hamsterWorker = HamsterWorker()
        self.hamsterProjects = self.hamsterWorker.getProjects()
        hamsterProjectsModel = QStringListModel()
        hamsterProjectsModel.setStringList(self.hamsterProjects)
        self.hamsterProjectView.setModel(hamsterProjectsModel)
        Qindex = hamsterProjectsModel.createIndex(0, 0)
        self.hamsterProjectView.selectionModel().select(Qindex, QItemSelectionModel.Select)

        redminesData = self.config.getRedminesData()
        for (i, item) in enumerate(redminesData):
            self.redmineCombo.addItem(item[0], i)

        self.hamsterProjectView.selectionModel().selectionChanged.connect(self.changeHamsterRedmine)
        self.saveHumsterProject.clicked.connect(self.saveHamsterRedmine)
        self.selectedIndexHamster = 0
        self.changeHamsterRedmine()

    def changeProject(self):
        index = self.redmineProjectsView.selectedIndexes()[0].row()
        if index >= 0:
            self.selectedIndex = index
            selectedProjectName = self.redmineProjectsView.model().data[index]
            evoId = self.config.getEvoIdByRedmineProjectName(selectedProjectName[1])
            if evoId != -1:
                evoId = int(evoId)

            if evoId in self.evoProjectIdToName:
                evoId = int(evoId)
                self.evoProject.setText(self.evoProjectIdToName[evoId])
            else:
                self.evoProject.setText("")
        else:
            self.selectedIndex = -1

    def saveProject(self):
        if self.selectedIndex >= 0:
            selectedProjectName = self.redmineProjectsView.model().data[self.selectedIndex]
            evoProjectName = self.evoProject.text()
            if evoProjectName in self.evoProjectNamesToId:
                self.config.setRedmineProjectToEvoId(selectedProjectName[1], self.evoProjectNamesToId[evoProjectName])
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Соответствие сохранено")
                msgBox.exec_()
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Проект с таким именем не найден")
                msgBox.exec_()

    def changeHamsterRedmine(self):
        index = self.hamsterProjectView.selectedIndexes()[0].row()
        if index >= 0:
            self.selectedIndexHamster = index
            selectedHamsterProjectName = self.hamsterProjects[index]
            redmineId = self.config.getRedmineIdByHamsterProjectName(selectedHamsterProjectName)
            if redmineId != -1:
                self.redmineCombo.setCurrentIndex(int(redmineId))
            else:
                self.redmineCombo.setCurrentIndex(0)
        else:
            self.selectedIndexHamster = -1

    def saveHamsterRedmine(self):
        if self.selectedIndexHamster >= 0:
            selectedProjectName = self.hamsterProjects[self.selectedIndexHamster]
            redmineId = self.redmineCombo.currentIndex()

            self.config.setRedmineIdByHamsterProjectName(selectedProjectName, redmineId)
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Соответствие сохранено")
            msgBox.exec_()