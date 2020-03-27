#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from functools import partial


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

class ToolImagesTub(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__()

        self.main = parent
        self.box = QtWidgets.QHBoxLayout(self)
        self.vbox = QtWidgets.QVBoxLayout()

        self.up = QtWidgets.QPushButton("^")
        self.down = QtWidgets.QPushButton("v")
        self.delBtn = QtWidgets.QPushButton("del")

        self.delBtn.clicked.connect(self._delBtn)
        self.up.clicked.connect(self._up)
        self.down.clicked.connect(self._down)
        self.vbox.addWidget(self.up)
        self.vbox.addWidget(self.down)
        self.vbox.addWidget(self.delBtn)
        self.vbox.addStretch(5)
        self.view = _ToolImagesTub(parent=self.main)
        self.box.addWidget(self.view)
        self.box.addLayout(self.vbox)

    def selectedItems(self):
        return self.view.selectedItems()

    def selectedIndexes(self):
        return self.view.selectedIndexes()

    def selectedNames(self):
        return self.view.selectedNames()

    def setLogicModel(self, logic_model):
        self.logicModel = logic_model

    def userSelectedItems(self):
        return self.view.userSelectedItems()


    def selectToIndex(self, *indexs):
        self.view.selectToIndex(*indexs)

    def selectedItems(self):
        return self.view.selectedItems()

    def addItems(self):
        self.view.addItems(self.logicModel)

    def _delBtn(self):
        self.main.delBtn()

    def _down(self):
        sel_lst = self.selectedIndexes()
        if len(sel_lst) > 1 or not sel_lst:
            return
        index = sel_lst[0]
        if index is not None and index > 0:
            e = self.view.items.pop(index)
            new_index = index-1
            self.view.items.insert(new_index, e)
            self.view.addItems(self.view.items)
            self.view.selectToIndex(new_index)


    def _up(self):
        sel_lst = self.selectedIndexes()
        if len(sel_lst) > 1 or not sel_lst:
            return
        index = sel_lst[0]
        if index is not None and index < len(self.view.items) -1:
            e = self.view.items.pop(index)
            new_index = index+1
            self.view.items.insert(new_index, e)
            self.view.addItems(self.view.items)
            self.view.selectToIndex(new_index)



class _ToolImagesTub(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        self.setStyleSheet("background-color: #616163")
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
        self.items = []
        self.items.extend(items)
        self.box.addStretch(5)
        for index, name in enumerate(self.items):
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