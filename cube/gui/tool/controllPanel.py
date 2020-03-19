#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore

default_config = dict(
    width_btn=48,
    height_btn=48
)


class ControllPanel(QtWidgets.QFrame):
    def __init__(self, parent=None, controller=None, cfg=default_config):
        super().__init__()
        self.main = parent
        self.cfg = cfg

        if controller is not None:

            self.controller = controller(self.main)
        else:
            self.controller = None
        self.box = QtWidgets.QVBoxLayout(self)
        self.close_btn = self._ctrl_btn("close_btn", "close_program", 48, 48)
        self.settings_btn = self._ctrl_btn("settings_btn", "show_settings", 48, 48)
        self.home_btn = self._ctrl_btn("home_btn", "toHome", 48, 48)

        self.box.addStretch(1)
        self.box.setSpacing(1)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.addWidget(self.home_btn)
        self.box.addWidget(self.settings_btn)
        self.box.addWidget(self.close_btn)

    def _ctrl_btn(self, name, action_name, width, height):
        btn = QtWidgets.QPushButton(self)
        btn.setObjectName(name)
        btn.setFixedSize(width, height)
        if self.controller is not None:
            btn.clicked.connect(getattr(self.controller, action_name))
        return btn

class ControlController:
    def __init__(self, parent):
        self.main = parent

    def close_program(self):
        self.main.close()

    def show_settings(self):
        self.main.showSettingsWidget()

    def toHome(self):
        self.main.toHome()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = ControllPanel()
    main.show()
    sys.exit(app.exec_())