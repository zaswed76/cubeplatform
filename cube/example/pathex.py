

#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
def qt_message_handler(mode, context, message):
    if mode == QtInfoMsg:
        mode = 'INFO'
    elif mode == QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
          context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))

qInstallMessageHandler(qt_message_handler)



class Widget(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.box = QtWidgets.QVBoxLayout(self)
        self.btn = QtWidgets.QPushButton("click")
        self.btn.clicked.connect(self.press_btn)
        self.box.addWidget(self.btn)

    def press_btn(self):
        self.on_dialog()



    def on_dialog(self):
        mb = QtWidgets.QMessageBox()
        mb.setWindowTitle("Выбрать вкладку")
        mb.setText("Открыть в новой или добавить в текущую?")
        # mb.setDetailedText("text")
        button_new = mb.addButton("в новой", QtWidgets.QMessageBox.AcceptRole)
        button_to = mb.addButton("добавить", QtWidgets.QMessageBox.AcceptRole)
        button_cancel = mb.addButton("Отклонить", QtWidgets.QMessageBox.RejectRole)
        mb.exec()
        if mb.clickedButton() == button_to:
            print("to")
        elif mb.clickedButton() == button_new:
            print("new")
        else:
            print('Пользователь отказался от обновления...')
            return


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())
