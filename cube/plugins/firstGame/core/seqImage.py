from collections.abc import MutableSequence
from random import random


class Sequence(MutableSequence):
    def __init__(self):
        self._lst = []

    def setTen(self, ten, step=1):
        self._lst.clear()
        self._lst.extend([str(x)for x in range(ten, ten+10, step)])

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



    def __repr__(self):
        return "{self.start} - {self.end}; step - {self.step}"

if __name__ == '__main__':

    imgseq = Sequence()
    imgseq.setTen(90)
    imgseq.setNames(0, 5, 45)
    for i in imgseq:
        print(i)



