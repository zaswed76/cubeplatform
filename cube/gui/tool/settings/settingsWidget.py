#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets
from gui.tool.settings.settingsStackWidget import *



class SettingsWidget(QtWidgets.QFrame):
    def __init__(self):
        """

        панель настроек left_panel
        кнопки слева и stackWidget справа settings_panel
        """
        super().__init__()
        self.setObjectName("settingsWidget")
        self.setToolTip("Settings")
        self.box = QtWidgets.QHBoxLayout(self)

        self.left_panel = QtWidgets.QFrame(self)
        self.left_box = QtWidgets.QVBoxLayout(self.left_panel)
        self.settings_panel = SettingsStackWidget()

        self.settings_panel.setObjectName("settings_panel")

        self.box.addWidget(self.left_panel, stretch=2)
        self.box.addWidget(self.settings_panel, stretch=20)

        self.setOptions()

    @property
    def options(self):
        return {"общие": BaseSet,
                "плагины": Plugins,
                "внешний вид": Appearance,
                "help": Help}

    def setOptions(self):
        for i, (name, widget) in enumerate(self.options.items()):
            btn = QtWidgets.QPushButton(name)
            btn.index = i
            btn.clicked.connect(self.choose_setting)
            self.left_box.addWidget(btn)
            self.settings_panel.addWidget(widget())
        self.left_box.addStretch(1)

    def choose_setting(self):
        self.settings_panel.setCurrentIndex(self.sender().index)








if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = SettingsWidget()
    main.show()
    sys.exit(app.exec_())