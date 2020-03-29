

#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class Btn(QtWidgets.QPushButton):
    def __init__(self, name, *__args):
        super().__init__(*__args)
        self.name = name
        self.setText(self.name)
        self.setMinimumWidth(28)
        self.setMaximumWidth(80)
        self.setStyleSheet("Text-align:left")
    def resizeEvent(self, e):
        w = e.size().width()
        if w < 50:
            self.setText("")
            self.setStyleSheet("Text-align:center")
        else:

            self.setText(self.name)
            self.setStyleSheet("Text-align:left")



class LeftFrame(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        # self.setMinimumWidth(40)
        # self.setMaximumWidth(200)
        self.setStyleSheet("background-color: grey")
        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setContentsMargins(4, 4, 4, 4)
        for i in range(5):
            btn = QtWidgets.QPushButton(str(i))
            btn.setStyleSheet("background-color: white")
            self.box.addWidget(btn)
        self.box.addStretch(5)

class RightFrame(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        # self.setMinimumWidth(10)
        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.btns = []
        for i in ["up", "down"]:
            btn = Btn(str(i))



            btn.setIcon(QtGui.QIcon("./{}.png".format(i)))


            self.box.addWidget(btn)
            self.btns.append(btn)
        self.box.addStretch(5)




class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.resize(300, 600)
        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setContentsMargins(0, 0, 2, 0)
        self.box.setSpacing(2)
        self.splitter = QtWidgets.QSplitter()
        self.splitter.setHandleWidth(2)
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