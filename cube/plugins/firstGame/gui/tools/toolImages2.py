#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtCore import *




def qt_message_handler(mode, context, message):
    if mode == QtInfoMsg:
        mode = 'INFO'
    elif mode == QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
          context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))

qInstallMessageHandler(qt_message_handler)

class Btn(QtWidgets.QPushButton):
    def __init__(self, *__args):

        super().__init__(*__args)
        self.setCheckable(True)
        # self.setAutoExclusive(True)

class View(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.box = QtWidgets.QVBoxLayout(self)

        self.items = []


    def clearLayout(self):
        while self.box.count() > 0:
            item = self.box.takeAt(0)
            if not item:
               continue
            w = item.widget()
            if w:
               w.deleteLater()

    def addItems(self, items):
        self.clearLayout()
        self.group = QtWidgets.QButtonGroup()
        self.group.setExclusive(False)
        self.items = []
        self.items.extend(items)
        for i in self.items:
            i = Btn(str(i))
            self.box.addWidget(i)
            self.group.addButton(i)

    def selectToIndex(self, index):
        for i, e in enumerate(self.group.buttons()):
            if i == index:
                e.setChecked(True)


    def selectedItems(self):
        for index, e in enumerate(self.group.buttons()):
            if e.isChecked():
                return (index)




class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

        self.box = QtWidgets.QHBoxLayout(self)
        self.vbox = QtWidgets.QVBoxLayout()
        self.up = QtWidgets.QPushButton("^")
        self.down = QtWidgets.QPushButton("v")
        self.up.clicked.connect(self._up)
        self.down.clicked.connect(self._down)
        self.vbox.addWidget(self.up)

        self.vbox.addWidget(self.down)


        self.view = View()
        self.box.addWidget(self.view)
        self.box.addLayout(self.vbox)

        self.view.addItems([1, 2, 3])

    def _up(self):
        index = self.view.selectedItems()
        if index is not None and index > 0:
            e = self.view.items.pop(index)
            new_index = index-1
            self.view.items.insert(new_index, e)
            print(self.view.items, "!!!!!!!!")
            self.view.addItems(self.view.items)
            self.view.selectToIndex(new_index)

    def _down(self):
        index = self.view.selectedItems()
        if index is not None and index < len(self.view.items) -1:
            e = self.view.items.pop(index)
            new_index = index+1
            self.view.items.insert(new_index, e)
            self.view.addItems(self.view.items)
            self.view.selectToIndex(new_index)

if __name__ == '__main__':


    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())