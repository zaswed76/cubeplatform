import sys
from PyQt5 import QtWidgets

from cube.gui import mainwindow

from cube import paths

def main():

    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = mainwindow.MainWindow(paths.MAIN_CONFIG)
    main.show()

    sys.exit(app.exec_())

main()