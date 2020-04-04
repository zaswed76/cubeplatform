from libs import abcseq


class Generator:
    def __init__(self):
        pass

    def getTen(self, ten: str or list, step=1):
        if isinstance(ten, str):
            iten = int(ten)
            return [str(x) for x in range(iten, iten + 10, step)]
        elif isinstance(ten, list):
            return ten

class Sequence(abcseq.Sequence):
    def __init__(self, *args):
        super().__init__(*args)




if __name__ == '__main__':
    g = Generator()
    imgseq = Sequence(1, 2, 3)
    imgseq.extend(g.getTen("0"))

    print(imgseq)
