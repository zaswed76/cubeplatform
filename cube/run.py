import sys
from PyQt5 import QtWidgets
import sys
import paths
print(paths.ROOT, "!!!!")
sys.path.insert(0, paths.ROOT)
from gui.mainwindow import MainWindow



def main():

    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow(paths.MAIN_CONFIG)
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()