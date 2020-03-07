import yaml
from collections.abc import MutableMapping

class Config(MutableMapping):
    def __init__(self, cfg_pth):
        self.cfg_pth = cfg_pth
        self._data = None
        self.load()


    def load(self):
        with open(self.cfg_pth) as f:
            self._data = yaml.safe_load(f)

    def save(self):
        with open(self.cfg_pth, 'w') as f:
            yaml.dump(self._data, f)

    @property
    def data(self):
        return self._data

    def __delitem__(self, key):
        del self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
       self._data[key] = value

    def __repr__(self):
        return str("{} - {}".format(self.__class__.__name__, self.cfg_pth))

if __name__ == '__main__':
    from pprint import pprint
    cfg = Config("./settings/main_config.yaml")


    print(cfg["screen_size"])
    cfg["screen_size"] = [100, 100]
    print(cfg["screen_size"])