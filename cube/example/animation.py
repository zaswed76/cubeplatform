

class Cat:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("Мяу")

    def yuo_name(self):
        self.say()
        print("моё имя {}".format(self.name))

import random
letters = "а з в ы н к а м о ы и  и у о  ю ц ш"
ls = letters.split(" ")



print(2*1)
cat1 = Cat("Тима")
cat1.yuo_name()
cat_list = {}

for cat_n in range(100000000):
    random.shuffle(ls)
    string = "".join(ls)
    name = string[:5]
    cat_list[cat_n] = Cat(name)
    cat_list[cat_n].yuo_name()


