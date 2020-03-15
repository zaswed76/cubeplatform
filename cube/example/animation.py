
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lol()
    def lol (self):
        self.resize(500,300)
        lb = QLabel('ТЕКСТ',self)
        lb.move(100,100)
        effect = QGraphicsColorizeEffect()
        lb.setGraphicsEffect(effect)
        an = QPropertyAnimation(effect, b"color", self)
        an.setStartValue((QColor(20,20,10)))
        an.setEndValue((QColor(200,200,10)))
        an.setDuration(200)
        an.start()
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())