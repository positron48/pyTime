from view.settings import Ui_SettingsForm
from PyQt5.QtWidgets import QMessageBox
from model.configWorker import ConfigWorker

class Ui_Setting(Ui_SettingsForm):

    def init(self):
        self.config = ConfigWorker()

        redmineData = self.config.getRedminesData()
        evolutionData = self.config.getEvolutionData()

        self.evolutionUrl.setText(evolutionData[0])
        self.evolutionLogin.setText(evolutionData[1])

        self.btnSaveEvo.clicked.connect(self.checkAndSaveEvo)

        if len(redmineData) > 0:
            currRedmine = redmineData[0]
            self.redmineUrl.setText(currRedmine[0])
            self.redmineLogin.setText(currRedmine[1])

    def checkAndSaveEvo(self):
        self.config.setEvolution([
            self.evolutionUrl.text(),
            self.evolutionLogin.text(),
            ""
        ])
        self.config.save()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Данные успешно сохранены!")
        msg.exec_()
