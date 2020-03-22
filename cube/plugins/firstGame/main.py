#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets
from plugins.abcPlugin import AbcQFrame
from plugins.firstGame.gui.view import View, Scene
from plugins.firstGame.gui.imageItem import GraphicsImage
from plugins.firstGame.gui.tools import Tools, ToolsController
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

        self.hbox = QtWidgets.QHBoxLayout(self)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setSpacing(1)
        self.scene = Scene(0, 0, 800, 800, GraphicsImage, paths.get_res_folder("cubeSerg", "images"), ".png", self)
        self.view = View(800, 800)
        self.view.setScene(self.scene)
        self.view.setStyleSheet("QGraphicsView { background-color: lightgrey }")
        self.hbox.addWidget(self.view, stretch=35)

        self.toolsController = ToolsController(self)
        self.tools = Tools(self.toolsController)
        # self.tools.setController(self.toolsController)

        self.hbox.addWidget(self.tools, stretch=5)

        self.seqImage = seqImage.Sequence()
        self.seqImage.setNames(92)
        self.scene.addImages(self.seqImage)

    def saveGeometry(self):
        self.scene.getItemsGeometry()

    def returnGeometry(self):
        print("returnGeometry")

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

