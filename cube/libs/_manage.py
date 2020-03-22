#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from plugins import make

def makeplugin(args):

    if args:
        if len(args) == 1:
            name = args[0]
            make.plugin(name)
            print("создан плагин - {}".format(name))
        else:
            print("колличество арггументов должно быть - 1")
    else:
        print("нужно указать имя, -n name;\nплагин не создан")

def dellplugin(arg):
    print(arg)