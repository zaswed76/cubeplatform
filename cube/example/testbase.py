#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore



class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.box = QtWidgets.QHBoxLayout(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())