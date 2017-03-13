from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractListModel, QVariant, QModelIndex


class RedmineListModel(QAbstractListModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.data = datain

    def rowCount(self, parent=QModelIndex()):
        return len(self.data)

    def data(self, index, role):
        if index.isValid() and role == QtCore.Qt.DisplayRole and len(self.data) > index.row():
            return QVariant(self.data[index.row()][0])
        else:
            return QVariant()

