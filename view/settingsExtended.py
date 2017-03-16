from view.settings import Ui_SettingsForm
from PyQt5.QtWidgets import QMessageBox, QLineEdit
from model.redmineListModel import RedmineListModel
from model.redmineWorker import RedmineWorker
from model.evolutionApiWorker import EvoWorker

class Ui_Setting(Ui_SettingsForm):

    def init(self, config, evoWorker, redmineWorkers):
        self.config = config
        self.evoWorker = evoWorker
        self.redmineWorkers = redmineWorkers

        redmineData = self.config.getRedminesData()
        evolutionData = self.config.getEvolutionData()

        self.evolutionUrl.setText(evolutionData[0])
        self.evolutionLogin.setText(evolutionData[1])
        self.evolutionLogin.setText(evolutionData[1])
        self.evolutionPassword.setEchoMode(QLineEdit.Password)
        self.redminePassword.setEchoMode(QLineEdit.Password)

        self.btnSaveEvo.clicked.connect(self.checkAndSaveEvo)

        redmineModel = RedmineListModel(redmineData)
        self.redminesList.setModel(redmineModel)
        self.btnRedmineAdd.clicked.connect(self.addRedmine)
        self.btnRedmineEdit.clicked.connect(self.editRedmine)
        self.redminesList.doubleClicked.connect(self.editRedmine)
        self.btnRedmineDelete.clicked.connect(self.deleteRedmine)
        self.btnSaveRedmine.clicked.connect(self.saveRedmine)

        if len(redmineData) > 0:
            self.curRedmineIndex = 0
            currRedmine = redmineData[0]
            self.redmineUrl.setText(currRedmine[0])
            self.redmineLogin.setText(currRedmine[1])
            self.redminePassword.setText("")
        else:
            self.curRedmineIndex = -1

    def checkAndSaveEvo(self):

        evoWorker = EvoWorker(self.evolutionUrl.text())
        token = evoWorker.getToken(self.evolutionLogin.text(), self.evolutionPassword.text())
        if token != False:
            self.evoWorker = evoWorker

            self.config.setEvolution([
                self.evolutionUrl.text(),
                self.evolutionLogin.text(),
                token,
                "",
                self.employer.text()

            ])
            self.config.save()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Данные успешно сохранены!")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Ошибка авторизации")
            msg.exec_()

    def addRedmine(self):
        self.redminesList.model().data.append([
            "redmine",
            "login",
            ""
        ])
        self.redminesList.model().layoutChanged.emit()

        self.redmineLogin.setText("login")
        self.redmineUrl.setText("redmine")
        self.redminePassword.setText("")
        self.curRedmineIndex = len(self.redminesList.model().data) - 1

    def editRedmine(self):
        index = self.redminesList.selectedIndexes()

        if len(index) > 0:
            index = index[0].row()
            self.curRedmineIndex = index

            redmine = self.redminesList.model().data[index]
            self.redmineUrl.setText(redmine[0])
            self.redmineLogin.setText(redmine[1])
            self.redminePassword.setText("")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Выберите redmine для изменения")
            msg.exec_()

    def deleteRedmine(self):
        index = self.redminesList.selectedIndexes()
        if len(index) > 0:
            index = index[0].row()
            if len(self.redminesList.model().data) > index:
                del self.redminesList.model().data[index]
                self.redminesList.model().layoutChanged.emit()
            self.curRedmineIndex = -1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Выберите redmine для удаления")
            msg.exec_()

    def saveRedmine(self):
        if self.curRedmineIndex >= 0:

            redmineWorker = RedmineWorker(self.redmineUrl.text())
            redmineWorker.initWithLogin(self.redmineLogin.text(), self.redminePassword.text())
            token = redmineWorker.getToken()

            if token == False:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Ошибка авторизации, неверный логин или пароль")
                msg.exec_()
            else:
                self.redmineWorkers[self.curRedmineIndex] = redmineWorker
                self.redminesList.model().data[self.curRedmineIndex] = [
                    self.redmineUrl.text(),
                    self.redmineLogin.text(),
                    token
                ]
                self.redminesList.model().layoutChanged.emit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Данные успешно сохранены")
                msg.exec_()


        if len(self.redminesList.model().data) > 0:
            self.config.saveRedmineData(self.redminesList.model().data)
