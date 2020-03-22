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
        self.image_size = self._pixmap.size().width()
        self.setPixmap(self._pixmap)
        self.setTransformationMode(
            QtCore.Qt.SmoothTransformation)
        self.setFlag(QtWidgets.QGraphicsPixmapItem.ItemIsMovable
                     )
        self.setFlag(QtWidgets.QGraphicsPixmapItem.ItemIsSelectable)

        self.scaled = 1.0
        self.rotate_mod = 0.0
        self.flip = False
        self.move_start()
        self.tr = QtGui.QTransform()



    def move_start(self):

        # self.moveBy(0, 110)
        s = (self.scale() * self.image_size) / 2



        self.setTransformOriginPoint(s, s)


    def setFlip(self):
        self.setTransform(self.tr.scale(-1, 1))
        if not self.flip:
            self.moveBy(self.image_size, 0)
            self.flip = not self.flip
        else:
            self.moveBy(-self.image_size, 0)
            self.flip = not self.flip


    def setRotate(self, delta):
        mod = 3
        if delta < 0:
            mod *= -1
        self.rotate_mod += mod
        self.setRotation(self.rotate_mod)

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
        x = self.scene.sceneRect().right() - self.width
        y = 0
        self.setPos(x, y)



class Scene(QtWidgets.QGraphicsScene):
    def __init__(self, x, y, width, height, parent=None):
        super().__init__(parent=None)
        self.setSceneRect(x, y, width, height)
        self.keyMap = {}
        control = {
            QtCore.Qt.Key_A: ("setAllSelected", True),
            QtCore.Qt.Key_D: ("setAllSelected", False),
            QtCore.Qt.Key_M: ("mirrorsItem", None)
        }
        self.keyMap["ctrl"] = control

    def addImages(self, GraphicsItemList):
        for item in GraphicsItemList:
            self.addItem(GraphicsImage(item.path, item.name, self))

    def scaledtems(self, delta: float):
        for i in self.selectedItems():
            i.setScale(i.scale() + delta)

    def mirrorsItem(self, *args):
        for i in self.selectedItems():
            i.setFlip()

    def rotateItems(self, delta: float):
        for i in self.selectedItems():
            i.setRotate(delta)

    def wheelEvent(self, WheelEvent):
        delta = WheelEvent.delta() / 5000
        if WheelEvent.modifiers() == QtCore.Qt.ControlModifier:
            self.scaledtems(delta)
        else:
            self.rotateItems(delta)

    def keyPressEvent(self, e):
       if (e.modifiers() & QtCore.Qt.ControlModifier):
           k = self.keyMap["ctrl"].get(e.key())
           if k is not None:
               getattr(self, k[0])(k[1])

    def setAllSelected(self, select):
        for i in self.items():
            i.setSelected(select)


class View(QtWidgets.QGraphicsView):
    def __init__(self, width, height):
        super().__init__()
        self.setFixedSize(width+4, height+4)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = View()
    main.show()
    sys.exit(app.exec_())