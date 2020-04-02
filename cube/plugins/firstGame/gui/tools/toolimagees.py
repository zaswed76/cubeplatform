#!/usr/bin/env python3




import sys

import os
from PyQt5 import QtWidgets, QtCore, QtGui
from functools import partial
from plugins.firstGame import gamepaths
from gui.glib import customwidgets as cust_widg

class ControlPanelScene(QtWidgets.QFrame):
    def __init__(self, controller):
        super().__init__()
        self._controller = controller
        self.mapPanelControl = MapPanelControl(self._controller)
        self.btnImageMapPanel = BtnImageMapPanel(self._controller)

        self.basebox = QtWidgets.QVBoxLayout(self)
        self.splitter = QtWidgets.QSplitter()
        self.splitter.setHandleWidth(2)
        self.splitter.setChildrenCollapsible(False)
        self.basebox.addWidget(self.splitter)
        self.splitter.addWidget(self.btnImageMapPanel)
        self.splitter.addWidget(self.mapPanelControl)


    def selectedItems(self):
        return self.btnImageMapPanel.selectedItems()

    def selectedIndexes(self):
        return self.btnImageMapPanel.selectedIndexes()

    def selectedNames(self):
        return self.btnImageMapPanel.selectedNames()

    def setLogicModel(self, logic_model):
        self.logicModel = logic_model

    def userSelectedItems(self):
        return self.btnImageMapPanel.userSelectedItems()


    def selectToNames(self, *names):
        self.btnImageMapPanel.selectToNames(*names)

    def selectToIndexs(self, *indexs):
        self.btnImageMapPanel.selectToIndexs(*indexs)

    def updateItems(self):
        print(self.logicModel)
        self.btnImageMapPanel.addItems(self.logicModel)

    def _delBtn(self):
        self.main.toolImagesController.delBtns()




class Dialog(QtWidgets.QInputDialog):
    def __init__(self):
        super().__init__()
        self.setIntMaximum(10)
        self.setIntMinimum(0)
        self.setIntStep(10)

class ImageMapBtn(QtWidgets.QPushButton):
    def __init__(self, name, index, *__args):
        super().__init__(*__args)
        self.name = name
        self.index = index
        self.setText(name)
        self.setCheckable(True)
        self.setAutoExclusive(False)
        self.userChecked = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setMinimumHeight(28)

    def isUserChecked(self):
        return self.userChecked


    def __repr__(self):
        return "ImageMapBtn-{}".format(self.name)

class MapPanelControl(QtWidgets.QFrame):
    def __init__(self, controller):
        super().__init__()

        self._controller = controller
        self.box = cust_widg.BoxLayout(QtWidgets.QBoxLayout.TopToBottom, self)
        self.up = self.controll("up")
        self.down = self.controll("down")
        self.sup = self.controll("sup")
        self.sdown = self.controll("sdown")

        self.up.clicked.connect(self._controller.upImageBtn)
        self.down.clicked.connect(self._controller.downImageBtn)
        self.sup.clicked.connect(self._controller.supImageBtn)
        self.sdown.clicked.connect(self._controller.sdownImageBtn)

        self.box.addWidget(self.sup)
        self.box.addWidget(self.up)
        self.box.addWidget(self.down)
        self.box.addWidget(self.sdown)
        self.box.addStretch(5)

    def controll(self, name):
        up = BtnResize(name)
        up.setIcon(QtGui.QIcon(os.path.join(gamepaths.ICONS, "{}.png".format(name))))
        return up





class BtnResize(QtWidgets.QPushButton):
    def __init__(self, name, *__args):
        super().__init__(*__args)
        self.name = name
        self.setText(self.name)

        self.setMinimumWidth(30)
        self.setMaximumWidth(80)
        self.setStyleSheet("Text-align:left")
        self.setIconSize(QtCore.QSize(18, 18))
    def resizeEvent(self, e):
        w = e.size().width()
        if w < 50:
            self.setText("")
            self.setStyleSheet("Text-align:center")
        else:

            self.setText(self.name)
            self.setStyleSheet("Text-align:left")


class BtnImageMapPanel(QtWidgets.QFrame):
    def __init__(self, controller):
        super().__init__()
        self._controller = controller
        self.setMinimumWidth(70)
        self.box = cust_widg.BoxLayout(QtWidgets.QBoxLayout.BottomToTop, self)
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
            print(name, "NNNNNNNNNNNN")
            btn = ImageMapBtn(name, index)
            self.box.addWidget(btn)
            self.group.addButton(btn)


    def imgBtnCheck(self):
        btn = self.sender()
        btn.userChecked = not btn.userChecked
        self.main.imgBtnCheck()

    def selectToNames(self, *names):
        self.clearSelecteted()
        for i, e in enumerate(self.group.buttons()):
            if e.name in names:
                e.setChecked(True)

    def selectToIndexs(self, *indexs):
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







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    # main = ToolAddImagesTub()
    # main.show()
    # sys.exit(app.exec_())