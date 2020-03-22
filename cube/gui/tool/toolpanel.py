#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets
from gui.tool.controllPanel import ControllPanel, ControlController

default_config = dict(

)

class ToolPanel(QtWidgets.QFrame):
    def __init__(self, parent, cfg=default_config):
        """
        панель инструментов слева
        содержит controllPanel
        :rtype:
        :param parent:
        :param cfg:
        """
        super().__init__()


        self.cfg = cfg
        self.main = parent
        self.__setControllPanel()

    def __setControllPanel(self):
        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setSpacing(0)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.controllPanel = ControllPanel(parent=self.main,
                                           controller=ControlController,
                                           cfg=self.cfg)
        self.box.addWidget(self.controllPanel)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = ToolPanel()
    main.show()
    sys.exit(app.exec_())
