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

class BottomBtn(QtWidgets.QPushButton):
    def __init__(self, name, *__args):
        super().__init__(*__args)
        self.name = name
        self.setObjectName(name)
        self.setFixedSize(18, 18)


class BottomAddPanel(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(25)
        self.setStyleSheet("background-color: #E1E1E1")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setSpacing(0)
        #
        self.delBtn = BottomBtn("firstGame_delBtn")
        self.addFilesBtn = BottomBtn("firstGame_addFilesBtn")
        self.addTenBtn = BottomBtn("firstGame_addTenBtn")
        self.hbox.addStretch(5)
        self.hbox.addWidget(self.addFilesBtn)
        self.hbox.addWidget(self.addTenBtn)
        self.hbox.addWidget(self.delBtn)


class RightFrame(QtWidgets.QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.box = QtWidgets.QHBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(1)

    def addWidget(self, w): self.box.addWidget(w)
    def addStretch(self, s): self.box.addStretch(s)



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

        self.bottomAddPanel = BottomAddPanel()
        self.box.addWidget(self.bottomAddPanel)



    def setController(self, controller):
        self._controller = controller




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Tools()
    main.show()
    sys.exit(app.exec_())