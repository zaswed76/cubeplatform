#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore
from plugins.firstGame.gui.tools import toolimagees
from gui.glib import customwidgets
# from plugins.firstGame import gamepaths

class Dialog(QtWidgets.QInputDialog):
    def __init__(self):
        super().__init__()
        self.setIntMaximum(10)
        self.setIntMinimum(0)
        self.setIntStep(10)




class BottomBtn(QtWidgets.QPushButton):
    def __init__(self, name, *__args):
        super().__init__(*__args)
        self.name = name
        self.setObjectName(name)
        self.setFixedSize(18, 18)


class BottomAddPanel(customwidgets.ToolTypeFrame):
    def __init__(self, name, controller, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self._controller = controller
        self.setFixedHeight(25)
        self.setStyleSheet("background-color: #E1E1E1")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setSpacing(0)
        #
        self.delBtn = BottomBtn("firstGame_delBtn")
        self.addFilesBtn = BottomBtn("firstGame_addFilesBtn")
        self.addTenBtn = BottomBtn("firstGame_addTenBtn")
        self.addFilesBtn.clicked.connect(self._controller.addFiles)
        self.addTenBtn.clicked.connect(self._controller.addTen)
        self.hbox.addStretch(5)
        self.hbox.addWidget(self.addFilesBtn)
        self.hbox.addWidget(self.addTenBtn)
        self.hbox.addWidget(self.delBtn)

    def showDialog(self):
        d = Dialog()
        i, ok = d.getInt(self, "a", "b", 0, 0, 90, 10)
        if ok:
            return str(i)
        else: return None

class RightFrame(QtWidgets.QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.box = QtWidgets.QHBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(1)

    def addWidget(self, w): self.box.addWidget(w)
    def addStretch(self, s): self.box.addStretch(s)



class Tools(QtWidgets.QFrame):
    def __init__(self, parent,  *args, **kwargs):

        """

        :param parent:
        :param args:
        :param kwargs:
        """
        super().__init__(parent, *args, **kwargs)
        self.main = parent
        self.setObjectName("firstGame_tools")
        self._controller = None
        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(1)


    def initTubWidget(self):
        self.tub = QtWidgets.QTabWidget()
        self.tub.setMovable(True)
        self.toolImagees = toolimagees.ControlPanelScene(self._controller)
        self.tub.addTab(self.toolImagees, "Images")
        self.box.insertWidget(2, self.tub)

    def initBottomPanel(self):
        self.bottomAddPanel = BottomAddPanel("bottomAddPanel", self._controller)
        self.box.insertWidget(3, self.bottomAddPanel)

    def initSaveReturnBtns(self):
        self.saveBtn = QtWidgets.QPushButton("save")
        self.saveBtn.setFixedWidth(200)
        self.saveBtn.clicked.connect(self._controller.saveGeometry)
        self.returnBtn = QtWidgets.QPushButton("return")
        self.returnBtn.clicked.connect(self._controller.returnBtn)
        self.box.insertWidget(0, self.saveBtn)
        self.box.insertWidget(1, self.returnBtn)


    def setController(self, controller):
        self._controller = controller




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Tools()
    main.show()
    sys.exit(app.exec_())