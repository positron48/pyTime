import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, QVariant
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog, QMessageBox, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from main import Ui_MainWindow
from redmineTask import Ui_RedmineTaskDialog
from evolutionTask import Ui_EvolutionTaskDialog

class MyFirstGuiProgram(Ui_MainWindow):
    def __init__(self, mainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(mainWindow)

        my_array = [['33254', '05.12.2016', '2', 'Разработка апи', 'Evolution', 'skillum'],
                    ['32658', '11.12.2016', '3.5', 'Тестирование и выкат', 'Столплит', 'stolplit']]

        # Connect "add" button with a custom function (addInputTextToListbox)
        self.btnRedmineTaskAdd.clicked.connect(self.addRedmineTask)
        self.btnRedmineTaskEdit.clicked.connect(self.editRedmineTask)
        self.redmineTasks.doubleClicked.connect(self.editRedmineTask)

        self.bindTable(self.redmineTasks, my_array)

    def bindTable(self, tableView, my_array):
        model = RedmineTasksModel(my_array)
        tableView.setModel(model)

    def addRedmineTask(self, data = None):
        dialog = QDialog()
        dialog.ui = Ui_RedmineTaskDialog()
        dialog.ui.setupUi(dialog)
        dialog.ui.date.setDate(QtCore.QDate.currentDate()git)
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

    def editRedmineTask(self, data=None):
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


class RedmineTasksModel(QAbstractTableModel):
    def __init__(self, data, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.data = data
        self.headerdata = ['Задача', 'Дата', 'Часы', 'Комментарий', 'Проект', 'Redmine']

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return len(self.data[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QVariant()
        return QVariant(self.data[index.row()][index.column()])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.headerdata[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            self.data[index.row()][index.column()] = value
        return True

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()

    prog = MyFirstGuiProgram(mainWindow)

    mainWindow.show()
    sys.exit(app.exec_())
