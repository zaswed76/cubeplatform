from collections.abc import MutableSequence
from random import random


class Sequence(MutableSequence):
    def __init__(self):
        self._lst = []

    def setTen(self, ten: str or list, step=1):
        self._lst.clear()
        if isinstance(ten, str):
            iten = int(ten)
            self._lst.extend([str(x)for x in range(iten, iten+10, step)])
        elif isinstance(ten, list):
            self._lst.extend(ten)

    def setNames(self, *names):
        self._lst.clear()
        self._lst.extend(str(x) for x in names)

    def shuffle(self):
        random.shuffle(self._lst)

    def reverse(self):
        self._lst.reverse()

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

    def remove(self, value):
        self._lst.remove(str(value))

    def removeItems(self, items):
        for i in items:
            self.remove(i)

    def up(self, index) -> int or None:
        new_index = index + 1
        if new_index < len(self._lst):
            item = self._lst.pop(index)
            self._lst.insert(new_index, item)
            return new_index
        else:
            return None

    def down(self, index) -> int or None:
        new_index = index - 1
        if new_index >= 0:
            item = self._lst.pop(index)
            self._lst.insert(new_index, item)
            return new_index
        else:
            return None

    def __repr__(self):
        return "-{}=".format(str(self._lst))


class SequenceFiles(MutableSequence):
    def __init__(self, *files):
        self._lst = []
        self._lst.extend(files)

    def addFiles(self, files):
        self._lst.extend(files)

    def shuffle(self):
        random.shuffle(self._lst)

    def reverse(self):
        self._lst.reverse()

    @property
    def data(self):
        return self._lst

    def insert(self, index, value):
        self._lst.insert(index, value)

    def remove(self, value):
        self._lst.remove(str(value))

    def removeItems(self, items):
        for i in items:
            self.remove(i)

    def up(self, index) -> int or None:
        new_index = index + 1
        if new_index < len(self._lst):
            item = self._lst.pop(index)
            self._lst.insert(new_index, item)
            return new_index
        else:
            return None

    def down(self, index) -> int or None:
        new_index = index - 1
        if new_index >= 0:
            item = self._lst.pop(index)
            self._lst.insert(new_index, item)
            return new_index
        else:
            return None

    def __setitem__(self, index, value):
        self._lst[index] = value

    def __getitem__(self, index):
        return self._lst[index]

    def __len__(self):
        return len(self._lst)

    def __delitem__(self, index):
        del self._lst[index]
    def __repr__(self):
        return "-{}=".format(str(self._lst))

if __name__ == '__main__':

    imgseq = Sequence()
    imgFiles = SequenceFiles()

    print(isinstance(imgseq, Sequence))
    print(isinstance(imgFiles, SequenceFiles))




