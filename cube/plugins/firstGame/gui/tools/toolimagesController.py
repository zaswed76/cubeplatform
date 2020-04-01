
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
        if ten is not None and not self.main.viewList.isName(ten):
            self.main.initScene(ten)
            self.main.viewList.getScene(ten).clear()

            tenlst = self.main.itemsGeometry.get("tens", {}).get(ten, ten)
            self.main.viewList.getLogicModel(ten).setTen(tenlst)
            self.main.viewList.getScene(ten).updateItems()
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
        logic_model = self.main.currentLogicModel
        new_index = logic_model.down(index)
        if new_index is not None:
            self.tool_widget.toolImagees.updateItems()
            self.tool_widget.toolImagees.selectToIndexs(new_index)
            self.main.currentScene.updateItems()


    def upImageBtn(self):
        sel_lst = self.tool_widget.toolImagees.selectedIndexes()
        if len(sel_lst) > 1 or not sel_lst:
            return
        index = sel_lst[0]
        logic_model = self.main.currentLogicModel
        new_index = logic_model.up(index)
        if new_index is not None:
            self.tool_widget.toolImagees.updateItems()
            self.tool_widget.toolImagees.selectToIndexs(new_index)
            self.main.currentScene.updateItems()

    def changedViewTub(self, i):
        name = self.main.viewsTubWidget.tabText(i)
        if name != "None":
            if name:
                logic_model = self.main.viewList.getLogicModel(int(name))
                self.tool_widget.toolImagees.setLogicModel(logic_model)
                self.tool_widget.toolImagees.updateItems()
                self.main.currentSceneName = name


if __name__ == '__main__':
    main = ToolImagesController()
