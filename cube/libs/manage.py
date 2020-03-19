
from plugins import make

def makeplugin(name):
    if name is not None:
        make.plugin(name)
        print("создан плагин - {}".format(name))
    else:
        print("нужно указать имя, -n name;\nплагин не создан")