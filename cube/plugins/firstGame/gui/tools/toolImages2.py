#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
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

class View(QtWidgets.QListWidget):
    def __init__(self):
        super().__init__()
        # self.setMovement(QtWidgets.QListView.Free)
        self.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.setDropIndicatorShown(True)

        self.setMovement(QtWidgets.QListView.Snap)
        self.setDragDropMode(QtWidgets.QListView.InternalMove)
        self.setDragDropOverwriteMode(False)

        for i in range(4):
            self.addItem(str(i))


    # def dropEvent(self, e):
    #     super().dropEvent(e)
    #     print(self.)



class Model(QtGui.QStandardItemModel):
    def __init__(self, *__args):
        super().__init__(*__args)

        for i in range(4):
            self.appendRow(Item(str(i)))
        print(self.co)




class Item(QtGui.QStandardItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFont(QtGui.QFont("Helvetica", 14))
        self.setSizeHint(QtCore.QSize(100, 30))
        self.setCheckable(True)
        self.setDropEnabled(False)


        # self.setAcceptDrops(True)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = QtWidgets.QFrame()
    box = QtWidgets.QVBoxLayout(main)

    view = View()
    # model = Model()
    # view.setModel(model)

    box.addWidget(view)
    main.show()
    sys.exit(app.exec_())