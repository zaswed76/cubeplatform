from importlib import import_module
import os

import paths


# mod = import_module(".main", "plugins.myFirstGame")
# print(mod)

class Plugin:
    def __init__(self):
        self.full_path = None
        self.name = None
        self.main_mod = None
        self.mod_object = None


    def init_mod(self):
        self.pkg = "{}.{}".format("plugins", self.name)
        print(self.pkg)
        self.mod_object = import_module(".main", self.pkg)

    def __repr__(self):
        return "path - {}\nname - {}\nmain - {}".format(self.full_path,
                                   self.name,
                                   self.main_mod)


class PluginLoader:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir

    def find_plugins(self):
        for folder in os.listdir(self.plugin_dir):
            path_plugin_dir = os.path.join(self.plugin_dir, folder)
            if os.path.isdir(path_plugin_dir):
                name = folder
                for file in os.listdir(path_plugin_dir):
                    if file == "config.yaml":
                        config = os.path.join(path_plugin_dir, file)
                    if file == "main.py":

                        main_mod = os.path.join(path_plugin_dir, file)
                        plugin_object = Plugin()
                        plugin_object.full_path = file
                        plugin_object.name = name
                        plugin_object.main_mod = main_mod
                        plugin_object.init_mod()




if __name__ == '__main__':
    plugin_path = paths.PLUGINS_FOLDER
    pl = PluginLoader(plugin_path)
    pl.find_plugins()
