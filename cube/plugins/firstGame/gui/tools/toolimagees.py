#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
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
        self.box = QtWidgets.QVBoxLayout(self)
        self.list = QtWidgets.QListView()
        self.list.setDropIndicatorShown(False)
        # self.list.setMovement(QtWidgets.QListView.Snap)
        self.list.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.entry = QtGui.QStandardItemModel()
        self.list.setModel(self.entry)
        self.box.addWidget(self.list)

        for text in ["Itemname1", "Itemname2", "Itemname3", "Itemname4"]:
            it = QtGui.QStandardItem(text)
            self.entry.appendRow(it)
        # self.tub.setTabPosition(QtWidgets.QTabWidget.West)
        #
        # for x in range(0, 101, 10):
        #     btn = QtWidgets.QPushButton(str(x))
        #     btn.setFixedWidth(200)
        #     self.tub.addTab(btn, str(x))

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