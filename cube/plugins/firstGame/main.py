#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets
from plugins.abcPlugin import AbcQFrame
from plugins.firstGame.gui.view import View, Scene, GraphicsImage
import paths
from pathlib import Path

class Main(AbcQFrame):
    def __init__(self):
        super().__init__()
        self.plugin_name = None

        self.hbox = QtWidgets.QHBoxLayout(self)
        self.scene = Scene(0, 0, 600, 600, self)
        self.view = View()
        self.view.setScene(self.scene)
        self.view.setStyleSheet("QGraphicsView { background-color: lightgrey }")
        self.hbox.addWidget(self.view)

        self.imageItem = GraphicsImage(paths.get_res_folder("cubeSerg/images/4.png"), "4", self.scene)
        self.imageItem2 = GraphicsImage(paths.get_res_folder("cubeSerg/images/50.png"), "50", self.scene)
        self.imageItem.setScale(0.3)
        self.imageItem.to_right_top()
        self.scene.addItems((self.imageItem, self.imageItem2))
        self.scene.setItemsScale(0.3)


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

