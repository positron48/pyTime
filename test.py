import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, QVariant
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from main import Ui_MainWindow


class MyFirstGuiProgram(Ui_MainWindow):
    def __init__(self, mainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(mainWindow)

        # Connect "add" button with a custom function (addInputTextToListbox)
        # self.addBtn.clicked.connect(self.addInputTextToListbox)
        my_array = [['33254', '05.12.2016', '2', 'Разработка апи', 'Evolution', 'skillum'],
                    ['32658', '11.12.2016', '3.5', 'Тестирование и выкат', 'Столплит', 'stolplit']]

        self.bindTable(self.redmineTasks, my_array)

    def bindTable(self, tableView, my_array):
        model = RedmineTasksModel(my_array)
        tableView.setModel(model)
        # tableView.setDelegate(MyDelegate)


class RedmineTasksModel(QAbstractTableModel):
    def __init__(self, data, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = data
        self.headerdata = ['Задача', 'Дата', 'Часы', 'Комментарий', 'Проект', 'Redmine']

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.headerdata[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    # def setData(self, index, value, role=QtCore.Qt.DisplayRole):

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()

    prog = MyFirstGuiProgram(mainWindow)

    mainWindow.show()
    sys.exit(app.exec_())
