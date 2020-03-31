#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from pathlib import Path


class GraphicsImage(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, scene, name, itemsGeometry, imgdir, ext, main=None):
        super().__init__()

        self.main = main
        self.scene = scene
        self.name = name
        self.itemsGeometry = itemsGeometry




        self.ext = ext
        self.imgdir = imgdir

        self._pixmap = QtGui.QPixmap(self.path)
        self.image_size = self._pixmap.size().width()
        self.setPixmap(self._pixmap)
        self.setTransformationMode(
            QtCore.Qt.SmoothTransformation)
        self.setFlag(QtWidgets.QGraphicsPixmapItem.ItemIsMovable
                     )
        self.setFlag(QtWidgets.QGraphicsPixmapItem.ItemIsSelectable)

        # print(self.itemsGeometry, "!!!!!!!")
        self._pos = self.itemsGeometry.get("pos", (0, 0))
        self._scaled = self.itemsGeometry.get("scaled", 1.0)
        self._rotate_mod = self.itemsGeometry.get("rotate_mod", 0.0)
        self._flip = self.itemsGeometry.get("flip", False)

        self._flip_flag = False
        self.transform = QtGui.QTransform()
        self.move_start()

    @property
    def path(self):
        if self.imgdir is not None:
            name = self.name + self.ext
            return str(Path(self.imgdir) / name)

    def __repr__(self):
        return "Pixmap-{}".format(self.name)

    def move_start(self):
        self.setPos(*self._pos)

        self.setRotation(self._rotate_mod)
        if self._flip:
            self.setFlip()
        self._transformation()
        self.setScale(self._scaled)

    def _transformation(self):
        s = (self.scale() * self.image_size) / 2
        self.setTransformOriginPoint(s, s)


    def setFlip(self):
        self.setTransform(self.transform.scale(-1, 1))
        if not self._flip_flag:
            self.moveBy(self.image_size, 0)
            self._flip_flag = True
            self._flip = True
        else:
            self.moveBy(-self.image_size, 0)
            self._flip_flag = False
            self._flip = False
        self.itemsGeometry["flip"] = self._flip


    def setRotate(self, delta):
        mod = 3
        if delta < 0:
            mod *= -1
        self._rotate_mod += mod
        self.setRotation(self._rotate_mod)
        self.itemsGeometry["rotate_mod"] = self._rotate_mod

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


    def mouseReleaseEvent(self, *args, **kwargs):
        super().mouseReleaseEvent(*args, **kwargs)
        self.main.imagePixmapCheck()





    def setScale(self, p_float):
        super().setScale(p_float)
        self.itemsGeometry["scaled"] = self.scale()


