#!/usr/bin/env python3

import sys

import os
from PyQt5 import QtWidgets, QtCore, QtGui
from functools import partial
from plugins.firstGame import gamepaths

class VBoxLayout(QtWidgets.QBoxLayout):
    def __init__(self, direction, parent, **kwargs):
        super().__init__(direction, parent)
        self.setDirection(direction)
        self.setParent(parent)
        contentMargin = kwargs.get("content_margin", (0, 0, 0, 0))
        spacing = kwargs.get("spacing", 0)
        self.setContentsMargins(*contentMargin)
        self.setSpacing(spacing)


class Dialog(QtWidgets.QInputDialog):
    def __init__(self):
        super().__init__()
        self.setIntMaximum(10)
        self.setIntMinimum(0)
        self.setIntStep(10)

class Btn(QtWidgets.QPushButton):
    def __init__(self, name, index, *__args):
        super().__init__(*__args)
        self.name = name
        self.index = index
        self.setText(name)
        self.setCheckable(True)
        self.setAutoExclusive(False)
        self.setStyleSheet('background: white;')
        self.userChecked = False
    def isUserChecked(self):
        return self.userChecked

class RightFrame(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        # self.setMinimumWidth(10)
        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)

        self.up = BtnResize("up")
        self.up.setIcon(QtGui.QIcon(os.path.join(gamepaths.ICONS, "up.png")))
        self.down = BtnResize("down")
        self.down.setIcon(QtGui.QIcon(os.path.join(gamepaths.ICONS, "down.png")))

        # self.up.clicked.connect(self._up)
        # self.down.clicked.connect(self._down)
        self.addWidget(self.up)
        self.addWidget(self.down)
        self.addStretch(5)

    def addWidget(self, widget):
        self.box.addWidget(widget)
    def addStretch(self, s):
        self.box.addStretch(s)



class BtnResize(QtWidgets.QPushButton):
    def __init__(self, name, *__args):
        super().__init__(*__args)
        self.name = name
        self.setText(self.name)
        self.setMinimumWidth(30)
        self.setMaximumWidth(80)
        self.setStyleSheet("Text-align:left")

    def resizeEvent(self, e):
        w = e.size().width()
        if w < 50:
            self.setText("")
            self.setStyleSheet("Text-align:center")
        else:

            self.setText(self.name)
            self.setStyleSheet("Text-align:left")

class ToolImagesTub(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__()

        self.main = parent
        self.basebox = QtWidgets.QVBoxLayout(self)
        self.splitter = QtWidgets.QSplitter()

        self.splitter.setHandleWidth(2)
        self.splitter.setChildrenCollapsible(False)

        self.basebox.addWidget(self.splitter)
        self.rightFrame = RightFrame()
        self.leftFrame = BtnImagePanel(parent=self.main)
        self.splitter.addWidget(self.leftFrame)
        self.splitter.addWidget(self.rightFrame)


    def selectedItems(self):
        return self.leftFrame.selectedItems()

    def selectedIndexes(self):
        return self.leftFrame.selectedIndexes()

    def selectedNames(self):
        return self.leftFrame.selectedNames()

    def setLogicModel(self, logic_model):
        self.logicModel = logic_model

    def userSelectedItems(self):
        return self.leftFrame.userSelectedItems()


    def selectToIndex(self, *indexs):
        self.leftFrame.selectToIndex(*indexs)

    def updateItems(self):
        self.leftFrame.addItems(self.logicModel)

    def _delBtn(self):
        self.main.toolImagesController.delBtns()

    def _down(self):
        self.main.toolImagesController.downBtn()


    def _up(self):
        self.main.toolImagesController.upBtn()




class BtnImagePanel(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        self.setStyleSheet("background-color: #C2C2C2")
        self.setMinimumWidth(70)
        # self.setMaximumWidth(100)
        self.box = VBoxLayout(QtWidgets.QBoxLayout.BottomToTop, self)
        self.group = QtWidgets.QButtonGroup()
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
        self.box.addStretch(5)
        for index, name in enumerate(items):
            btn = Btn(name, index)
            btn.toggled.connect(self.imgBtnCheck)
            self.box.addWidget(btn)
            self.group.addButton(btn)


    def imgBtnCheck(self):
        btn = self.sender()
        btn.userChecked = not btn.userChecked
        self.main.imgBtnCheck()

    def selectToIndex(self, *indexs):
        self.clearSelecteted()
        for i, e in enumerate(self.group.buttons()):
            if i in indexs:
                e.setChecked(True)

    def userSelectedItems(self):
        lst = []
        for index, e in enumerate(self.group.buttons()):
            if e.isUserChecked():
                lst.append((index, e))
        return lst

    def selectedItems(self):
        return [x for x in self.group.buttons() if x.isChecked()]

    def selectedIndexes(self):
        return [x.index for x in self.group.buttons() if x.isChecked()]

    def selectedNames(self):
        return [x.name for x in self.group.buttons() if x.isChecked()]


    def clearSelecteted(self):
        for e in self.group.buttons():
            e.setChecked(False)

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