from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractTableModel, QVariant


class RedmineTasksModel(QAbstractTableModel):
    def __init__(self, data, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.data = data
        self.headerdata = ['Задача', 'Дата', 'Часы', 'Комментарий', 'Проект', 'Redmine', 'Название задачи']

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        if len(self.data):
            return len(self.data[0])
        return 0

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
