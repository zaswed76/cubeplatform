#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore, QtGui



class Scene(QtWidgets.QGraphicsScene):
    def __init__(self, rect, GraphicsImage, imgdir, ext, itemsGeometry, parent=None,
                 *__args):
        """

        :param rect: (x: int, y: int, width: int, height: int)
        :param GraphicsImage: gui.imageItem.GraphicsImage
        :param imgdir: str
        :param ext: str
        :param itemsGeometry: dict
        :param parent: main
        :param __args:
        """
        super().__init__(*__args)
        self.main = parent
        self.itemsGeometry = itemsGeometry
        x, y, width, height = rect
        self.ext = ext
        self.imgdir = imgdir
        self.GraphicsImage = GraphicsImage
        self.setSceneRect(x, y, width, height)
        self.keyMap = {}
        control = {
            QtCore.Qt.Key_A: ("setAllSelected", True),
            QtCore.Qt.Key_D: ("setAllSelected", False),
            QtCore.Qt.Key_M: ("mirrorsItem", None)
        }
        self.keyMap["ctrl"] = control

    def setLogicModel(self, logic_model):
        self.logicModel = logic_model

    def updateItems(self):
        self.clear()
        for name in self.logicModel:
            item = self.GraphicsImage(self, name, self.itemsGeometry.get(name, {}), self.imgdir, self.ext, main=self.main)
            self.addItem(item)

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
        self.main.imagePixmapCheck()


    def getItemsGeometry(self):
        return [x for x in self.items()]

    def selectedfromName(self, names):
        self.setAllSelected(False)
        ids = [str(t[0]) for t in names]
        for i in self.items():
            if i.name in ids:
                i.setSelected(True)

    # def mousePressEvent(self, *args, **kwargs):
    #     print("####")
    #
    # def mouseReleaseEvent(self, QGraphicsSceneMouseEvent):
    #     print("####")



class View(QtWidgets.QGraphicsView):
    def __init__(self, size):
        super().__init__()
        self.setObjectName("firstGame_View")
        width, height = size
        self.setFixedSize(width+4, height+4)
        self.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        # self.setRenderHint(QtGui.QPainter.Antialiasing, True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = View()
    main.show()
    sys.exit(app.exec_())