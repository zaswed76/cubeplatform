#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore
from pathlib import Path
import config
from plugins.abcPlugin import AbcQFrame
from plugins.firstGame.gui.view import View, Scene
from plugins.firstGame.gui.imageItem import GraphicsImage
from plugins.firstGame.gui.tools import (tools, toolimagesController,
                                         leftFrame, topFrame, bottomFrame)
from plugins.firstGame.core import seqImage

import paths
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

class Main(AbcQFrame):
    def __init__(self):
        super().__init__()
        self.plugin_name = None

        self.cfg = config.Config(str(Path(paths.PLUGINS_FOLDER) / "firstGame" / "config.yaml"))

        self.itemsGeometry = config.Config(str(Path(paths.PLUGINS_FOLDER) / "firstGame" / "itemGeometry.yaml"))

        self.vbox_1 = QtWidgets.QVBoxLayout(self)
        self.vbox_1.setContentsMargins(0, 0, 0, 0)
        self.vbox_1.setSpacing(0)
        self.topFrame = topFrame.TopFrame()
        self.midleFrame = QtWidgets.QFrame()
        self.bottomFrame = bottomFrame.BottomFrame()
        # self.vbox_1.addStretch(100)
        self.vbox_1.addWidget(self.topFrame)
        self.vbox_1.addWidget(self.midleFrame)
        self.vbox_1.addWidget(self.bottomFrame)
        # self.vbox_1.addStretch(100)

        self.hbox_2 = QtWidgets.QHBoxLayout(self.midleFrame)

        # self.hbox_2 = QtWidgets.QHBoxLayout(self.midleFrame)
        self.hbox_2.setContentsMargins(0, 0, 0, 0,)
        self.hbox_2.setSpacing(0)

        self.leftFrame = leftFrame.LeftFrame()

        # scene

        sceneRect = self.cfg["sceneRect"]
        resource_path = paths.get_res_folder("cubeSerg", "images")
        self.scene = Scene(sceneRect, GraphicsImage, resource_path, ".png", self.itemsGeometry,  parent=self)
        self.view = View(self.cfg["viewSize"])
        self.view.setScene(self.scene)

        self.rightFrame = tools.RightFrame()
        self.toolsController = tools.ToolsController(self)
        self.tools = tools.Tools(self.toolsController, parent=self)
        self.rightFrame.addWidget(self.tools)
        self.rightFrame.addStretch(100)



        self.hbox_2.addWidget(self.leftFrame)
        self.hbox_2.addWidget(self.view)
        self.hbox_2.addWidget(self.rightFrame)



        #
        # self.hbox = QtWidgets.QHBoxLayout(self)
        # self.hbox.setContentsMargins(0, 0, 0, 0)
        # self.hbox.setSpacing(1)
        # sceneRect = self.cfg["sceneRect"]
        # resource_path = paths.get_res_folder("cubeSerg", "images")
        # self.scene = Scene(sceneRect, GraphicsImage, resource_path, ".png", self.itemsGeometry,  parent=self)
        # self.view = View(self.cfg["viewSize"])
        # self.view.setScene(self.scene)
        # self.hbox.addStretch(35)
        # self.hbox.addWidget(self.view, stretch=35)
        #
        # self.toolsController = tools.ToolsController(self)
        # self.tools = tools.Tools(self.toolsController, parent=self)
        # self.hbox.addWidget(self.tools, stretch=5)
        #
        #
        # self.toolImagesController = toolimagesController.ToolImagesController(self, self.tools.toolImagees)
        #
        # self.logicModel = seqImage.Sequence()
        # self.scene.setLogicModel(self.logicModel)
        # self.tools.toolImagees.setLogicModel(self.logicModel)
        # self.hbox.addStretch(35)




    def saveGeometry(self):
        for i in self.scene.getItemsGeometry():
            self.itemsGeometry[i.name] = i.itemsGeometry
        self.itemsGeometry.save()

    def returnGeometry(self):
        print("returnGeometry")

    def newTen(self, ten):
        self.scene.clear()
        self.logicModel.setTen(ten)
        self.scene.updateItems()
        self.tools.toolImagees.updateItems()

    def imgBtnCheck(self):
        pass
        # selected = self.tools.toolImagees.userSelectedItems()
        # self.scene.selectedfromName(selected)


    def imagePixmapCheck(self):
        pass
        # selected = [int(x.name) for x in self.scene.selectedItems()]
        # print(selected)
        # # self.tools.toolImagees.selectToIndex(*selected)

if __name__ == '__main__':

    import os
    app = QtWidgets.QApplication(sys.argv)
    css_path = os.path.join(paths.BASE_CSS_FOLDER, "firstGame.css")
    app.setStyleSheet(open('{}'.format(css_path), "r").read())
    main = Main()
    main.setObjectName("firstGame")

    main.show()
    main.resize(700, 700)
    # main.showMaximized()
    sys.exit(app.exec_())

