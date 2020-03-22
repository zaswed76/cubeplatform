#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore

class ToolsController(QtCore.QObject):
    def __init__(self, parent):
        super().__init__()
        self.main = parent

    def saveBtn(self):
        self.main.saveGeometry()

    def returnBtn(self):
        self.main.returnGeometry()

class Tools(QtWidgets.QFrame):
    def __init__(self, controller):
        super().__init__()
        self.setObjectName("firstGame_tools")
        self._controller = controller
        self.box = QtWidgets.QVBoxLayout(self)

        self.saveBtn = QtWidgets.QPushButton("save")
        self.saveBtn.clicked.connect(self._controller.saveBtn)
        self.returnBtn = QtWidgets.QPushButton("return")
        self.returnBtn.clicked.connect(self._controller.returnBtn)
        self.box.addWidget(self.saveBtn)
        self.box.addWidget(self.returnBtn)
        self.box.addStretch(1)

    def setController(self, controller):
        self._controller = controller


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Tools()
    main.show()
    sys.exit(app.exec_())