import sys

from PyQt5 import QtWidgets

from pyTimeGui import PyTimeGui

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()

    prog = PyTimeGui(mainWindow)

    mainWindow.show()
    sys.exit(app.exec_())
