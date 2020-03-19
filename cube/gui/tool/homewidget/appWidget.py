#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class AppButton(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
        self.setObjectName("appButton")
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

class NoteWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("noteWidget")

class AppWidget(QtWidgets.QFrame):
    def __init__(self, parent):
        super().__init__()
        self.main = parent
        print(self.main)
        self.setObjectName("appWidget")
        self.box = QtWidgets.QHBoxLayout(self)


    def addGameIcon(self, index, icon):
        print(index, icon)
        btn = AppButton()
        btn.index = index
        btn.clicked.connect(self.press)
        btn.setIcon(QtGui.QIcon(icon))
        btn.setIconSize(QtCore.QSize(128, 128))
        btn.setFixedSize(128, 128)
        self.box.addWidget(btn)

    def press(self):
        self.main.setWorkWidgetToIndex(self.sender().index)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = AppWidget()
    main.show()
    sys.exit(app.exec_())