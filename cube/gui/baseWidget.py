#!/usr/bin/env python3

import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from gui.tool.toolpanel import ToolPanel as Tool
from gui.tool.settingsWidget import SettingsWidget
from gui.tool.homeWidget import HomeWidget
from gui import workWidget
from plugins.games1.myFirstGame import Main


class BaseWidget(QtWidgets.QFrame):
    def __init__(self, parent, cfg):
        """
        окно содержит панель настроек tool.toolpanel.ToolPanel
        и рабочее окно workWidget.WorkWidget
        :param parent:
        """
        super().__init__()
        self.cfg = cfg
        self.main = parent
        self.tool_visible = True
        self.settings_visible = False
        self.last_index = 2
        self.base_box = QtWidgets.QHBoxLayout(self)
        self.base_box.setSpacing(1)
        self.base_box.setContentsMargins(0, 0, 0, 0)
        self.left_box = QtWidgets.QVBoxLayout()
        self.center_box = QtWidgets.QHBoxLayout()
        self.base_box.addLayout(self.left_box)

        self.tool = Tool(self)
        self.tool.setVisible(self.tool_visible)
        self.left_box.addWidget(self.tool)

        self.work_frame = workWidget.WorkWidget()
        self.setWorkWidget()

        self.homeWidget = HomeWidget()
        self.work_frame.insertWidget(0, self.homeWidget)

        self.setSettingsWidget()


        self.first = Main()
        self.work_frame.insertWidget(2, self.first)

        self.showWindow()

    def showWindow(self):
        self.work_frame.setCurrentIndex(2)
        self.last_index = 2

    def setSettingsWidget(self):
        self.settingsWidget = SettingsWidget()
        self.work_frame.insertWidget(1, self.settingsWidget)

    def showSettingsWidget(self):
        if not self.settings_visible:
            self.work_frame.setCurrentIndex(1)
            self.settings_visible = True
        else:
            self.work_frame.setCurrentIndex(self.last_index)
            self.settings_visible = False


    def close(self):
        self.main.close()

    def setWorkWidget(self):

        self.work_frame.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                  QtWidgets.QSizePolicy.Expanding))
        self.work_frame.setObjectName("work_frame")
        self.base_box.addWidget(self.work_frame, stretch=5)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F12:
            self.tool_visible = not self.tool_visible
            self.tool.setVisible(self.tool_visible)

        elif e.key() == Qt.Key_Escape:
            if not self.tool_visible:
                self.tool_visible = True
                self.tool.setVisible(self.tool_visible)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BaseWidget()
    main.show()
    sys.exit(app.exec_())