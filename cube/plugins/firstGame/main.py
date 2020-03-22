#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets
from plugins.abcPlugin import AbcQFrame
from plugins.firstGame.gui.view import View, Scene, GraphicsImage


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
        path = "/home/sergdell/pyprojects/pyprojects/cubeplatform/cube/resource/gameresource/cubeSerg/images/4.png"
        self.imageItem = GraphicsImage(path, "4", self.scene)
        self.imageItem.setScale(0.3)
        self.imageItem.to_right_top()
        self.scene.addItem(self.imageItem)













if __name__ == '__main__':
    import paths
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

