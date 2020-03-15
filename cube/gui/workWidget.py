#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore
from gui.tool.settingsWidget import SettingsWidget



class WorkWidget(QtWidgets.QStackedWidget):
    def __init__(self):
        """
        рабочая область которая содержит все игровые окна,
        окно настроек
        """
        super().__init__()






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = WorkWidget()
    main.show()
    sys.exit(app.exec_())