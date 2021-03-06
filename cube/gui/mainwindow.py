import os
import sys
from PyQt5 import QtWidgets
from config import Config
from gui import baseWidget
from libs import filesTool
import paths
from plugins import pluginLoader


class MainWindow(QtWidgets.QFrame):
    def __init__(self, config_pth, *args, **kwargs):
        """
        главное окно в котором настраиваются стили
        окно содержит виджет - baseWidget.BaseWidget
        :param config_pth:
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setObjectName("main")
        self.cfg = Config(config_pth)
        # self.showFullScreen()
        self._set_style_sheet(self.cfg["style_name"])

        self.plugins = pluginLoader.PluginLoader(paths.PLUGINS_FOLDER)
        self.plugins.find_plugins()

        self._setBaseWidget()

    def _setBaseWidget(self):
        self.box = QtWidgets.QHBoxLayout(self)
        self.box.setSpacing(0)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.baseWidget = baseWidget.BaseWidget(self, self.cfg)
        self.baseWidget.setPlugins(self.plugins)
        self.box.addWidget(self.baseWidget)



    def closeEvent(self, event):
        self.cfg["screen_size"] = [self.size().width(), self.size().height()]
        self.cfg.save()

    def _set_style_sheet(self, sheetName):
        """
        :param sheetName: str имя стиля
        """
        css_folder = os.path.join(paths.CSS_FOLDER, sheetName)
        styleSheet = filesTool.fileInput(css_folder)
        QtWidgets.QApplication.instance().setStyleSheet(styleSheet)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

