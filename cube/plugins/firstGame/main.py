#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets
from plugins.abcPlugin import AbcQFrame
from plugins.firstGame.gui.view import View, Scene, GraphicsImage
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
        self.scene = Scene(0, 0, 800, 800, self)
        self.view = View(800, 800)
        self.view.setScene(self.scene)
        self.view.setStyleSheet("QGraphicsView { background-color: lightgrey }")
        self.hbox.addWidget(self.view)

        self.seqImage = seqImage.Sequence(paths.get_res_folder("cubeSerg/images"))
        self.seqImage.setNames(2)
        self.scene.addImages(self.seqImage)



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

