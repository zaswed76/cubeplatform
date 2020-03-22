#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class GraphicsImage(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, path, name, scene):
        super().__init__()
        self.scene = scene
        self.name = name
        self.path = path
        self._pixmap = QtGui.QPixmap(path)
        self.setPixmap(self._pixmap)
        self.setTransformationMode(
            QtCore.Qt.SmoothTransformation)
        self.setFlag(QtWidgets.QGraphicsPixmapItem.ItemIsMovable
                     )
        self.setFlag(QtWidgets.QGraphicsPixmapItem.ItemIsSelectable)
        self.scaled = 0.3

    def wheelEvent(self, WheelEvent):
        delta = WheelEvent.delta() / 5000
        if WheelEvent.modifiers() == QtCore.Qt.ControlModifier:

            self.scaled += delta
            self.setScale(self.scaled)
        else:
            self.setRotation(delta)


    @property
    def width(self):
        return self.sceneBoundingRect().size().width()

    @property
    def height(self):
        return self.sceneBoundingRect().size().height()

    def to_center(self):
        w = self.scene.width() / 2 - self.width / 2
        h = self.scene.height() / 2 - self.height / 2
        self.setPos(w, h)

    def to_right_top(self):
        print(self.width)
        print(self.scene.sceneRect().top())
        x = self.scene.sceneRect().right() - self.width
        y = 0
        self.setPos(x, y)



class Scene(QtWidgets.QGraphicsScene):
    def __init__(self, x, y, width, height, parent=None):
        super().__init__(parent=None)
        self.setSceneRect(x, y, width, height)

    def addItems(self, GraphicsItemList):
        for item in GraphicsItemList:
            self.addItem(item)

    def setItemsScale(self, scale: float):
        for i in self.items():
            i.setScale(scale)


class View(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setFixedSize(604, 604)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = View()
    main.show()
    sys.exit(app.exec_())