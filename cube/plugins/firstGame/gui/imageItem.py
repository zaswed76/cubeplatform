#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from pathlib import Path


class GraphicsImage(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, scene, name, imgdir, ext):
        super().__init__()
        self.scene = scene
        self.name = name
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

        self.scaled = 1.0
        self.rotate_mod = 0.0
        self.flip = False
        self.move_start()
        self.tr = QtGui.QTransform()

    @property
    def path(self):
        if self.imgdir is not None:
            name = self.name + self.ext
            return str(Path(self.imgdir) / name)

    def __repr__(self):
        return f"Pixmap-{self.name}"

    def move_start(self):
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