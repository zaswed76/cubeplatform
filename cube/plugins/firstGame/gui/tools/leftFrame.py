

#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore



class LeftFrame(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.box = QtWidgets.QHBoxLayout(self)
        self.box.addStretch(100)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = LeftFrame()
    main.show()
    sys.exit(app.exec_())