#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore



class AbcQFrame(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()


    def abcTest(self):
        return "AbcQFrame"



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = AbcQFrame()
    main.show()
    sys.exit(app.exec_())