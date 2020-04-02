
#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore
from plugins.firstGame import gamepaths


class ToolImagesController():
    def __init__(self, main, tool_widget):
        self.tool_widget = tool_widget
        self.main = main


    def saveGeometry(self):
        for i in self.main.currentScene.getItemsGeometry():
            self.main.itemsGeometry[i.name] = i.itemsGeometry
            self.main.itemsGeometry[i.name]["pos"] = [i.pos().x(), i.pos().y()]
        if not self.main.itemsGeometry.get("tens", False):
            self.main.itemsGeometry["tens"] = {}
        self.main.itemsGeometry["tens"][self.main.currentSceneName] = self.main.currentLogicModel.data
        self.main.itemsGeometry.save()

    def returnGeometry(self):
        print("returnGeometry")

    # def saveBtn(self):
    #     self.main.saveGeometry()

    def returnBtn(self):
        self.main.returnGeometry()

    def addFiles(self):
        print("addFiles")
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(None, directory=gamepaths.GAME_RESOURCES)
        if files:
            self.main.initViewFiles(files)
            self.main.viewMap.getScene("new_tub").clear()
            self.main.viewMap.getLogicModel("new_tub").addFiles(files)

            self.main.viewMap.getScene("new_tub").updateItems()
            self.main.viewMap.getScene("new_tub").name = "new_tub"
            self.main.tools.controlPanelScene.updateItems()

    def addTen(self, ten):
        ten = self.main.tools.bottomAddPanel.showDialog()
        line_ten = str(ten)
        if ten is not None and not self.main.viewMap.isName(line_ten):
            self.main.initView(line_ten)
            self.main.viewMap.getScene(line_ten).clear()
            tenlst = self.main.itemsGeometry.get("tens", {}).get(line_ten, ten)
            # print(tenlst, "tenlst")
            self.main.viewMap.getLogicModel(line_ten).setTen(tenlst)
            self.main.viewMap.getScene(line_ten).updateItems()
            self.main.viewMap.getScene(line_ten).name = line_ten
            self.main.tools.controlPanelScene.updateItems()

    def delBtns(self):
        items = self.tool_widget.toolImagees.selectedNames()
        self.main.logicModel.removeItems(items)
        self.tool_widget.toolImagees.updateItems()
        self.main.scene.updateItems()

    def sdownImageBtn(self):
        print("sdownImageBtn")

    def downImageBtn(self):
        sel_lst = self.tool_widget.controlPanelScene.selectedIndexes()
        if len(sel_lst) > 1 or not sel_lst:
            return
        index = sel_lst[0]
        logic_model = self.main.currentLogicModel
        new_index = logic_model.down(index)
        if new_index is not None:
            self.tool_widget.controlPanelScene.updateItems()
            self.main.currentScene.updateItems()
            self.tool_widget.controlPanelScene.selectToIndexs(new_index)

    def supImageBtn(self):
        print("supImageBtn")

    def upImageBtn(self):
        sel_lst = self.tool_widget.controlPanelScene.selectedIndexes()
        if len(sel_lst) > 1 or not sel_lst:
            return
        index = sel_lst[0]
        logic_model = self.main.currentLogicModel
        new_index = logic_model.up(index)
        if new_index is not None:
            self.tool_widget.controlPanelScene.updateItems()
            self.main.currentScene.updateItems()
            self.tool_widget.controlPanelScene.selectToIndexs(new_index)

    def closeTabView(self, i):
        # todo надо доделать
        widget = self.main.viewsTubWidget.widget(i)
        self.main.viewMap.remove(widget.name)
        self.main.viewsTubWidget.removeTab(i)


    def changedViewTub(self, i):
        name = self.main.viewsTubWidget.tabText(i)
        if name != "None":
            if name:
                logic_model = self.main.viewMap.getLogicModel(name)
                self.tool_widget.controlPanelScene.setLogicModel(logic_model)
                self.tool_widget.controlPanelScene.updateItems()

                self.main.currentSceneName = name


if __name__ == '__main__':
    main = ToolImagesController()
