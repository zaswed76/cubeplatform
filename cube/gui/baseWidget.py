#!/usr/bin/env python3

import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from gui.tool.toolpanel import ToolPanel as Tool
from gui.tool.settings.settingsWidget import SettingsWidget
from gui.tool.homewidget.homeWidget import HomeWidget
from gui import workStackWidget


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
        self.plugins = dict()
        self.tool_visible = True
        self.settings_visible = False
        # последний видимый индекс
        self.last_index = 0
        self.base_box = QtWidgets.QHBoxLayout(self)
        self.base_box.setSpacing(1)
        self.base_box.setContentsMargins(0, 0, 0, 0)
        self.left_box = QtWidgets.QVBoxLayout()
        self.center_box = QtWidgets.QHBoxLayout()
        self.base_box.addLayout(self.left_box)
        # ---- tool -------
        self.tool = Tool(self)
        self.tool.setVisible(self.tool_visible)
        self.left_box.addWidget(self.tool)

        # ---- workStackWidget -------
        self.workStackWidget = workStackWidget.WorkStackWidget()
        self.workStackWidget.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                  QtWidgets.QSizePolicy.Expanding))
        self.workStackWidget.setObjectName("work_frame")
        self.base_box.addWidget(self.workStackWidget, stretch=5)

        self.homeWidget = HomeWidget(self)


        self.workStackWidget.insertWidget(0, self.homeWidget)

        self.setSettingsWidget()
        self.showWindow()

    def toHome(self):
        self.workStackWidget.setCurrentIndex(0)
        self.last_index = 0

    def setWorkWidgetToIndex(self, index):
        self.workStackWidget.setCurrentIndex(index)
        self.last_index = index

    def showWindow(self):
        self.workStackWidget.setCurrentIndex(2)
        self.last_index = 2

    def setSettingsWidget(self):
        self.settingsWidget = SettingsWidget()
        self.workStackWidget.insertWidget(1, self.settingsWidget)

    def showSettingsWidget(self):
        if not self.settings_visible:
            self.workStackWidget.setCurrentIndex(1)
            self.settings_visible = True
        else:
            self.workStackWidget.setCurrentIndex(self.last_index)
            self.settings_visible = False


    def close(self):
        self.main.close()



    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F12:
            self.tool_visible = not self.tool_visible
            self.tool.setVisible(self.tool_visible)

        elif e.key() == Qt.Key_Escape:
            if not self.tool_visible:
                self.tool_visible = True
                self.tool.setVisible(self.tool_visible)

    def setPlugins(self, plugins):
        for plugin in plugins.plugins.values():
            self.plugins[plugin.index] = plugin.mod_object.Main()
            self.plugins[plugin.index].setObjectName(plugin.name)
            self.plugins[plugin.index].setToolTip(plugin.name)
            self.workStackWidget.insertWidget(plugin.index, self.plugins[plugin.index])
            self.homeWidget.app_widget.addGameIcon(plugin.index, plugin.app_icon)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BaseWidget()
    main.show()
    sys.exit(app.exec_())