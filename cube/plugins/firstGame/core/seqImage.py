
from collections.abc import MutableSequence
from pathlib import Path



class Item:
    def __init__(self, value, imgdir=None, ext=".png"):
        self.ext = ext
        self.imgdir = imgdir
        self.name = str(value)

    @property
    def path(self):
        if self.imgdir is not None:
            name = self.name + self.ext
            return str(Path(self.imgdir) / name)

    def __repr__(self):
        return f"{self.name}"


class Sequence(MutableSequence):
    def __init__(self, imgdir=None, ext=".png"):
        self.ext = ext
        self.imgdir = imgdir
        self._lst = []

    def setTen(self, ten, step=1):
        self._lst.clear()
        self._lst.extend([Item(x, self.imgdir, self.ext) for x in range(ten, ten+10, step)])

    def setNames(self, *names):
        self._lst.clear()
        self._lst.extend([Item(x, self.imgdir, self.ext) for x in names])

    @property
    def data(self):
        return self._lst

    def __setitem__(self, index, value):
        self._lst[index] = value

    def __getitem__(self, index):
        return self._lst[index]

    def __len__(self):
        return len(self._lst)

    def __delitem__(self, index):
        del self._lst[index]

    def insert(self, index, value):
        self._lst.insert(index, value)

    def __repr__(self):
        return f"{self.start} - {self.end}; step - {self.step}"

if __name__ == '__main__':
    import paths
    imgseq = Sequence(paths.get_res_folder("cubeSerg", "images"))
    imgseq.setTen(90)
    imgseq.setNames(0, 5, 45)
    for i in imgseq:
        print(i.path)



