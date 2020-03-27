

#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class LeftFrame(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(40)
        self.setMaximumWidth(200)
        self.setStyleSheet("background-color: grey")
        self.box = QtWidgets.QVBoxLayout(self)
        for i in range(5):
            btn = QtWidgets.QPushButton(str(i))
            btn.setStyleSheet("background-color: white")
            btn.setMinimumWidth(20)
            self.box.addWidget(btn)
        self.box.addStretch(5)

class RightFrame(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(10)
        self.box = QtWidgets.QVBoxLayout(self)
        self.btns = []
        for i in ["up", "down"]:
            btn = QtWidgets.QPushButton(str(i))



            btn.setIcon(QtGui.QIcon("./{}.png".format(i)))
            btn.setStyleSheet("Text-align:left")
            btn.setMinimumWidth(10)
            self.box.addWidget(btn)
            self.btns.append(btn)
        self.box.addStretch(5)

    def resizeEvent(self, e):
        w = e.size().width()
        if w < 75:
            for b in self.btns:

                b.setText("")
                b.setStyleSheet("Text-align:center")
                b.resize(40, 40)
                b.repaint()



class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.resize(300, 600)
        self.box = QtWidgets.QVBoxLayout(self)
        self.splitter = QtWidgets.QSplitter()
        self.splitter.setHandleWidth(4)
        self.splitter.setChildrenCollapsible(False)
        self.box.addWidget(self.splitter)
        self.splitter.addWidget(LeftFrame())
        self.splitter.addWidget(RightFrame())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())