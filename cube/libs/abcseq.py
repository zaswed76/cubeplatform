from collections.abc import MutableSequence


class Sequence(MutableSequence):
    def __init__(self, *files):
        self._lst = []
        self._lst.extend(files)



    def insert(self, index, object):
        self._lst.insert(index, object)

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

    def __repr__(self):
        return "-{}-".format(str(self._lst))

    def shift(self, index, n_direction):
        new_index = index + n_direction
        item = self._lst.pop(index)
        if new_index < 0: new_index = 0
        self._lst.insert(new_index, item)