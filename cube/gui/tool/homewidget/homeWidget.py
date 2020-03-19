#!/usr/bin/env python3


import sys
from PyQt5 import QtWidgets
from gui.glib.widgets import *
from gui.tool.homewidget import appWidget



class HomeWidget(QtWidgets.QFrame):
    def __init__(self, parent):
        """
        панель на которой отображаются значки плагинов
        """
        super().__init__()

        self.base_main = parent
        self.setObjectName("homeWidget")
        self.box = VBoxLayout(QtWidgets.QBoxLayout.TopToBottom,
                              self, spacing=1)
        self.bottom_box = QtWidgets.QHBoxLayout()
        self.top_box = QtWidgets.QHBoxLayout()
        self.setToolTip("Home")
        self.box.addLayout(self.top_box, stretch=30)
        self.box.addLayout(self.bottom_box, stretch=4)


        self.app_widget = appWidget.AppWidget(self.base_main)



        self.note_widget = appWidget.NoteWidget()

        self.top_box.addWidget(self.app_widget, stretch=40)
        self.top_box.addWidget(self.note_widget, stretch=15)

        self.service_widget = QtWidgets.QFrame()
        self.service_widget.setStyleSheet('background: cyan;')
        self.bottom_box.addWidget(self.service_widget)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = HomeWidget()
    main.show()
    sys.exit(app.exec_())






