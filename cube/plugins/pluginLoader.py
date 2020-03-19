from importlib import import_module
import os
import yaml
import paths

from collections.abc import MutableMapping


def load(cfg):
    with open(cfg) as f:
        return yaml.safe_load(f)


def save(cfg, data):
    with open(cfg, 'w') as f:
        yaml.dump(data, f)

class Plugins(MutableMapping):
    def __init__(self):
        self.__plugins = {}

    def __contains__(self, item):
        for i, plugin in self.__plugins.items():
            if item is plugin:
                return True

    def __repr__(self):
        return str("plugins.rst - {}".format(self.__plugins))

    def __getitem__(self, item):

        return self.__plugins[item]

    def __delitem__(self, item):
        del (self.__plugins[item])

    def __setitem__(self, index, item):

        self.__plugins[index] = item

    def __iter__(self):
        return iter(self.__plugins)

    def __len__(self):
        return len(self.__plugins)


class Plugin:
    def __init__(self):
        self.full_path = None
        self.name = None
        self.main_mod = None
        self.config = None
        self.mod_object = None
        self.index = None
        self.app_icon = None

    def init_mod(self):
        self.pkg = "{}.{}".format("plugins", self.name)
        self.mod_object = import_module(".main", self.pkg)

    def __repr__(self):
        return "id: {}\npath - {}\nname - {}\nmain - {}".format(
            self.index,
            self.full_path,
            self.name,
            self.main_mod)


class PluginLoader:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
        self.stack_index = 2
        self.__plugins = Plugins()



    @property
    def plugins(self):
        return self.__plugins

    def find_plugins(self):
        self.cfg = load(os.path.join(self.plugin_dir,  "manifest.yaml"))
        if not self.cfg["plugins"]:
            print("в манифесте не зарегистроированы плагины")
            return

        for folder in os.listdir(self.plugin_dir):

            path_plugin_dir = os.path.join(self.plugin_dir, folder)
            if os.path.isdir(path_plugin_dir):
                name = folder


                for file in os.listdir(path_plugin_dir):
                    if file == self.cfg["main_name"]:
                        config = os.path.join(path_plugin_dir, self.cfg["config_name"])
                        main_mod = os.path.join(path_plugin_dir, file)
                        plugin_object = Plugin()
                        plugin_object.full_path = file
                        plugin_object.name = name
                        plugin_object.main_mod = main_mod
                        plugin_object.index = self.stack_index
                        config = os.path.join(path_plugin_dir, self.cfg["config_name"])
                        app_icon = os.path.join(path_plugin_dir, self.cfg["app_icon"])
                        plugin_object.app_icon = app_icon

                        if os.path.isfile(config):
                            plugin_object.config = config
                            plugin_object.init_mod()
                            try:
                                index = self.cfg["plugins"][name]['index']
                            except KeyError:
                                print("{} - в манифесте не указан такой плагин".format(name))
                            else:
                                plugin_object.index = index
                                self.plugins[index] = plugin_object


    def __repr__(self):
        return str(self.__plugins)


if __name__ == '__main__':
    plugin_path = paths.PLUGINS_FOLDER
    pl = PluginLoader(plugin_path)
    pl.find_plugins()
    for i in pl.plugins.values():
        print(i)
        print("--------------")
