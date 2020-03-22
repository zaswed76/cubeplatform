#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets


class WorkStackWidget(QtWidgets.QStackedWidget):
    def __init__(self):
        """
        рабочая область которая содержит
        окно игр,
        окно настроек
        домашнее окно
        """
        super().__init__()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = WorkStackWidget()
    main.show()
    sys.exit(app.exec_())