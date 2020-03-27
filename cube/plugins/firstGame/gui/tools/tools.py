#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore
from plugins.firstGame.gui.tools import toolimagees

class ToolsController(QtCore.QObject):
    def __init__(self, parent):
        super().__init__()
        self.main = parent

    def saveBtn(self):
        self.main.saveGeometry()

    def returnBtn(self):
        self.main.returnGeometry()

class Tools(QtWidgets.QFrame):
    def __init__(self, controller, parent,  *args, **kwargs):

        super().__init__(parent, *args, **kwargs)
        self.main = parent
        self.setObjectName("firstGame_tools")
        self._controller = controller
        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(1)
        self.tub = QtWidgets.QTabWidget()
        # self.tub.setTabPosition(QtWidgets.QTabWidget.West)
        self.tub.setMovable(True)

        self.tub.addTab(toolimagees.ToolAddImagesTub(parent=self.main), "AddImages")

        self.toolImagees = toolimagees.ToolImagesTub(parent=self.main)
        self.tub.addTab(self.toolImagees, "Images")



        self.saveBtn = QtWidgets.QPushButton("save")
        self.saveBtn.setFixedWidth(200)
        self.saveBtn.clicked.connect(self._controller.saveBtn)
        self.returnBtn = QtWidgets.QPushButton("return")
        self.returnBtn.clicked.connect(self._controller.returnBtn)



        self.box.addWidget(self.saveBtn)
        self.box.addWidget(self.returnBtn)
        # self.box.addStretch(1)
        self.box.addWidget(self.tub)



    def setController(self, controller):
        self._controller = controller




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Tools()
    main.show()
    sys.exit(app.exec_())