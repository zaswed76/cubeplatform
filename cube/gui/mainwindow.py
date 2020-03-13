import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QFile



import paths
from config import Config





class MainWindow(QtWidgets.QFrame):
    def __init__(self, config_pth, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName("center")


        self.cfg = Config(paths.MAIN_CONFIG)
        self.showFullScreen()

        self.set_style_sheet("wood")

        self.base_box = QtWidgets.QVBoxLayout(self)
        self.base_box.setSpacing(1)
        self.base_box.setContentsMargins(0, 0, 0, 0)
        self.top_box = QtWidgets.QHBoxLayout()
        self.center_box = QtWidgets.QHBoxLayout()
        self.base_box.addLayout(self.top_box)


        self.close_btn = self._ctrl_btn("close_btn", "close_program", 48, 48)
        self.settings_btn = self._ctrl_btn("settings_btn", "show_settings", 48, 48)


        self.top_box.addStretch(1)
        self.top_box.setSpacing(1)
        self.top_box.setContentsMargins(0, 0, 0, 0)
        self.top_box.addWidget(self.settings_btn)
        self.top_box.addWidget(self.close_btn)

        self.work_frame = QtWidgets.QFrame()
        self.work_frame.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding))
        self.work_frame.setObjectName("work_frame")
        self.base_box.addWidget(self.work_frame, stretch=5)





    def _ctrl_btn(self, name, action_name, width, height):
        btn = QtWidgets.QPushButton(self)
        btn.setObjectName(name)
        btn.setFixedSize(width, height)
        print(name, action_name)
        btn.clicked.connect(getattr(self, action_name))
        return btn

    def close_program(self):
        self.close()

    def show_settings(self):
        print("show_settings")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F12:
            self.set_screen()

    def closeEvent(self, event):
        self.cfg["screen_size"] = [self.size().width(), self.size().height()]
        self.cfg.save()

    def set_style_sheet(self, sheetName):
        """
        :param sheetName: str имя стиля
        """
        file_name = sheetName + '.css'
        file = QFile('./css/{}'.format(file_name))
        file.open(QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')
        QtWidgets.QApplication.instance().setStyleSheet(styleSheet)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

