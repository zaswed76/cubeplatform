
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
        items = self.tool_widget.toolImagees.selectedNames()
        self.main.logicModel.removeItems(items)
        self.tool_widget.toolImagees.updateItems()
        self.main.scene.updateItems()

    def downImageBtn(self):
        sel_lst = self.tool_widget.toolImagees.selectedIndexes()
        if len(sel_lst) > 1 or not sel_lst:
            return
        index = sel_lst[0]
        new_index = self.main.logicModel.down(index)
        if new_index is not None:
            self.tool_widget.toolImagees.updateItems()
            self.tool_widget.toolImagees.selectToIndex(new_index)
            self.main.scene.updateItems()


    def upImageBtn(self):
        sel_lst = self.tool_widget.toolImagees.selectedIndexes()
        if len(sel_lst) > 1 or not sel_lst:
            return
        index = sel_lst[0]
        new_index = self.main.logicModel.up(index)
        if new_index is not None:
            self.tool_widget.toolImagees.updateItems()
            self.tool_widget.toolImagees.selectToIndex(new_index)
            self.main.scene.updateItems()




if __name__ == '__main__':
    main = ToolImagesController()
