#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore



class Main(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Main()
    main.show()
    sys.exit(app.exec_())