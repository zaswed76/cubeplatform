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


class ViewMap:
    def __init__(self, *args, **kwargs):
        self._data = dict()
        self.__dict__.update(*args, **kwargs)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    def __delitem__(self, key):
        del self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)


    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return '{}, D({})'.format(super(ViewMap, self).__repr__(),
                                  self.__dict__)


    def view(self, key):
        return self.__dict__[key]["view"]

    def clear(self):
        self._data.clear()

    def addScene(self, name, view, scene, logicModel):
        self._data[name] = dict(view=view, scene=scene, logicModel=logicModel)
        self.__dict__[name] = dict(view=view, scene=scene, logicModel=logicModel)

    def getView(self, name):
        return self.__dict__[name]["view"]

    def getScene(self, name):
        return self._data[name]["scene"]

    def getLogicModel(self, name):
        return self._data[name]["logicModel"]

    def isName(self, name):
        return self._data.get(name, None)

    def remove(self, name):
        del(self._data[name])

class TabWidgetScenes(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()
        self.setTabsClosable(True)


class Main(AbcQFrame):
    def __init__(self):
        super().__init__()
        self.plugin_name = None
        self._currentSceneName = None
        self.cfg = config.Config(str(Path(paths.PLUGINS_FOLDER) / "firstGame" / "config.yaml"))
        self.itemsGeometry = config.Config(str(Path(paths.PLUGINS_FOLDER) / "firstGame" / "itemGeometry.yaml"))
        self.sceneRect = self.cfg["sceneRect"]
        self.resource_path = paths.get_res_folder("cubeSerg", "images")

        self.viewMap = ViewMap()
        self.initTools()
        self.initViewsTubWidget()
        self.initView(self.currentSceneName)

        #
        self.vbox_1 = QtWidgets.QVBoxLayout(self)
        self.vbox_1.setContentsMargins(0, 0, 0, 0)
        self.vbox_1.setSpacing(0)
        self.topFrame = topFrame.TopFrame()
        self.midleFrame = QtWidgets.QFrame()
        self.bottomFrame = bottomFrame.BottomFrame()
        self.vbox_1.addWidget(self.topFrame)
        self.vbox_1.addWidget(self.midleFrame)
        self.vbox_1.addWidget(self.bottomFrame)

        self.hbox_2 = QtWidgets.QHBoxLayout(self.midleFrame)
        self.hbox_2.setContentsMargins(0, 0, 0, 0,)
        self.hbox_2.setSpacing(30)
        self.leftFrame = leftFrame.LeftFrame()
        self.rightFrame = tools.RightFrame()
        self.rightFrame.addWidget(self.tools)
        self.rightFrame.addStretch(100)
        self.hbox_2.addWidget(self.leftFrame)
        self.hbox_2.addWidget(self.viewsTubWidget)
        self.hbox_2.addWidget(self.rightFrame)

    def initTools(self):
        self.tools = tools.Tools(parent=self)
        self.toolImagesController = toolimagesController.ToolImagesController(self, self.tools)
        self.tools.setController(self.toolImagesController)
        self.tools.initTubWidget()
        self.tools.initSaveReturnBtns()
        self.tools.initBottomPanel()

    def initViewsTubWidget(self):
        self.viewsTubWidget = TabWidgetScenes()
        self.viewsTubWidget.tabCloseRequested.connect(self.toolImagesController.closeTabView)
        self.viewsTubWidget.currentChanged.connect(self.toolImagesController.changedViewTub)
        self.viewsTubWidget.setMovable(True)

    @property
    def currentSceneName(self):
        if self._currentSceneName is None: return None
        else:
            return int(self._currentSceneName)

    @currentSceneName.setter
    def currentSceneName(self, name):
        self._currentSceneName = name

    @property
    def currentScene(self):
        scene = self.viewMap.getScene(self.currentSceneName)
        return scene

    @property
    def currentView(self):
        return self.viewMap.getView(self.currentSceneName)

    @property
    def currentLogicModel(self):
        return self.viewMap.getLogicModel(self.currentSceneName)

    def _setViewToViewMap(self, name):
            logicModel = seqImage.Sequence()
            self.tools.toolImagees.setLogicModel(logicModel)
            scene = Scene(self.sceneRect, GraphicsImage, self.resource_path, ".png", self.itemsGeometry,  parent=self)
            scene.selectionChanged.connect(self.selectionSceneChange)
            scene.setLogicModel(logicModel)
            view = View(self.cfg["viewSize"], name)
            view.setScene(scene)
            self.viewMap.addScene(name, view, scene, logicModel)


    def initView(self, name):
        counttubs = self.viewsTubWidget.count()
        if counttubs == 1 and self.viewsTubWidget.tabText(0) == "None":
            self.viewMap.clear()
            self._setViewToViewMap(name)
            self.viewsTubWidget.clear()
            self.viewsTubWidget.addTab(self.viewMap.view(name), str(name))
        else:
            self._setViewToViewMap(name)
            self.viewsTubWidget.addTab(self.viewMap.getView(name), str(name))
            self.viewsTubWidget.setCurrentIndex(self.viewsTubWidget.count()-1)


    def selectionSceneChange(self):
        scene = self.currentScene
        if scene is not None:
            names = [x.name for x in self.currentScene.selectedItems()]
            self.tools.toolImagees.selectToNames(*names)



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

