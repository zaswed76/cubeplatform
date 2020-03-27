#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore



class HBoxLayout(QtWidgets.QHBoxLayout):
    def __init__(self, parent, **args):
        super().__init__()
        self.setParent(parent)
        contentMargin = args.get("content_margin", (0, 0, 0, 0))
        spacing = args.get("spacing", 0)
        self.setContentsMargins(*contentMargin)
        self.setSpacing(spacing)

class VBoxLayout(QtWidgets.QBoxLayout):
    def __init__(self, direction, parent, **kwargs):
        super().__init__(direction, parent)
        self.setDirection(direction)
        self.setParent(parent)
        contentMargin = kwargs.get("content_margin", (0, 0, 0, 0))
        spacing = kwargs.get("spacing", 0)
        self.setContentsMargins(*contentMargin)
        self.setSpacing(spacing)

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.box = VBoxLayout(QtWidgets.QBoxLayout.BottomToTop, self)
        self.box.addWidget(QtWidgets.QPushButton("1"))
        self.box.addWidget(QtWidgets.QPushButton("2"))
        self.box.addWidget(QtWidgets.QPushButton("3"))
        self.box.addWidget(QtWidgets.QPushButton("4"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())