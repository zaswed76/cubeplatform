
#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore



class ToolImagesController():
    def __init__(self, main, tool_widget):
        self.tool_widget = tool_widget
        self.main = main

    def saveBtn(self):
        self.main.saveGeometry()

    def returnBtn(self):
        self.main.returnGeometry()

    def addTen(self, ten):
        ten = self.main.tools.bottomAddPanel.showDialog()
        if ten is not None:
            self.main.scene.clear()
            self.main.logicModel.setTen(ten)
            self.main.scene.updateItems()
            self.main.tools.toolImagees.updateItems()

    def delBtns(self):
        items = self.tool_widget.selectedNames()
        self.main.logicModel.removeItems(items)
        self.tool_widget.updateItems()
        self.main.scene.updateItems()

    def downBtn(self):
        sel_lst = self.tool_widget.selectedIndexes()
        if len(sel_lst) > 1 or not sel_lst:
            return
        index = sel_lst[0]
        if index is not None and index > 0:
            e = self.tool_widget.items.pop(index)
            new_index = index-1
            self.tool_widget.items.insert(new_index, e)
            self.tool_widget.updateItems(self.tool_widget.items)
            self.tool_widget.selectToIndex(new_index)


    def upBtn(self):
        sel_lst = self.tool_widget.selectedIndexes()
        if len(sel_lst) > 1 or not sel_lst:
            return
        index = sel_lst[0]
        if index is not None and index < len(self.tool_widget.items) -1:
            e = self.tool_widget.items.pop(index)
            new_index = index+1
            self.tool_widget.items.insert(new_index, e)
            self.tool_widget.updateItems(self.view.items)
            self.tool_widget.selectToIndex(new_index)



if __name__ == '__main__':
    main = ToolImagesController()
