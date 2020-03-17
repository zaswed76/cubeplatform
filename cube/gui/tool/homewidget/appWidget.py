#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtGui, QtCore



class NoteWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("noteWidget")

class AppWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("appWidget")
        self.box = QtWidgets.QHBoxLayout(self)


    def addGameIcon(self, icon):
        btn = QtWidgets.QPushButton()
        btn.setIcon(QtGui.QIcon(icon))
        btn.setIconSize(QtCore.QSize(128, 128))
        btn.setFixedSize(128, 128)
        self.box.addWidget(btn)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = AppWidget()
    main.show()
    sys.exit(app.exec_())