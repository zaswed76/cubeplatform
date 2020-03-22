#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore

class BaseSet(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("settings_baseSet")

class Plugins(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("settings_plugins")

class Appearance(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("settings_appearance")

class Help(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("settings_help")

class SettingsStackWidget(QtWidgets.QStackedWidget):
    def __init__(self):
        """
        рабочая область которая содержит окна настроек
        """
        super().__init__()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = SettingsStackWidget()
    main.show()
    sys.exit(app.exec_())