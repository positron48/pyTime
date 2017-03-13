from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox

from main import Ui_MainWindow
from redmineTask import Ui_RedmineTaskDialog
from evolutionTask import Ui_EvolutionTaskDialog
from redmineTaskModel import RedmineTasksModel
from evolutionTaskModel import EvolutionTasksModel


class PyTimeGui(Ui_MainWindow):
    def __init__(self, mainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(mainWindow)

        redmineTasksData = [
            ['33254', '05.12.2016', '2', 'Разработка апи', 'Evolution', 'skillum'],
            ['32658', '11.12.2016', '3.5', 'Тестирование и выкат', 'Столплит', 'stolplit']
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

        self.redmineTasks.setModel(RedmineTasksModel(redmineTasksData))
        self.evoTasks.setModel(EvolutionTasksModel(evolutionTasksData))

    def bindTable(self, tableView, my_array):
        model = RedmineTasksModel(my_array)
        tableView.setModel(model)

    def addRedmineTask(self):
        dialog = QDialog()
        dialog.ui = Ui_RedmineTaskDialog()
        dialog.ui.setupUi(dialog)
        dialog.ui.date.setDate(QtCore.QDate.currentDate())
        dialog.ui.hours.setValue(8)

        if dialog.exec_() == QDialog.Accepted:
            self.redmineTasks.model().data.append([
                dialog.ui.taskNubmer.text(),
                dialog.ui.date.text(),
                dialog.ui.hours.value(),
                dialog.ui.comment.toPlainText(),
                dialog.ui.redmineProject.text(),
                "skillum"
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

            dialog.ui.taskNubmer.setText(task[0])
            dialog.ui.redmineProject.setText(task[4])
            dialog.ui.hours.setValue(float(task[2]))
            dialog.ui.date.setDate(QtCore.QDate.fromString(task[1], 'dd.MM.yyyy'))
            dialog.ui.comment.setText(task[3])

            if dialog.exec_() == QDialog.Accepted:
                self.redmineTasks.model().data[index] = [
                    dialog.ui.taskNubmer.text(),
                    dialog.ui.date.text(),
                    dialog.ui.hours.value(),
                    dialog.ui.comment.toPlainText(),
                    dialog.ui.redmineProject.text(),
                    task[5]
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
