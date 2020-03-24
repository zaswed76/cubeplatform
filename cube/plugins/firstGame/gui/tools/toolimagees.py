#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore
from functools import partial

class Dialog(QtWidgets.QInputDialog):
    def __init__(self):
        super().__init__()
        self.setIntMaximum(10)
        self.setIntMinimum(0)
        self.setIntStep(10)



class ToolImagesTub(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__()
        self.setStyleSheet("background-color: #616163")
        self.box = QtWidgets.QHBoxLayout(self)

class ToolAddImagesTub(QtWidgets.QFrame):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = parent
        self.setStyleSheet("background-color: #616163")
        self.box = QtWidgets.QVBoxLayout(self)
        self.newTen = QtWidgets.QPushButton("new ten")
        self.newTen.clicked.connect(self.showDialog)
        self.newTen.setStyleSheet("background-color: #F2F2F4")
        self.box.addWidget(self.newTen)
        self.box.addStretch(1)

    def showDialog(self):
        d = Dialog()
        i, ok = d.getInt(self, "a", "b", 0, 0, 90, 10)
        if ok:
            self.main.newTen(i)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = ToolAddImagesTub()
    main.show()
    sys.exit(app.exec_())