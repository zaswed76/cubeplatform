#!/usr/bin/env python3


import sys
from PyQt5 import QtWidgets, QtCore



class HomeWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("homeWidget")
        self.box = QtWidgets.QHBoxLayout(self)
        self.setToolTip("Home")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = HomeWidget()
    main.show()
    sys.exit(app.exec_())






