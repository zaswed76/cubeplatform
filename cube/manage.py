#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from libs import _manage


import argparse
parser = argparse.ArgumentParser(description='Great Description To Be Here')
parser.add_argument("command")
parser.add_argument("args", nargs='*', default=[])

register_command = ("makeplugin", "delplugin")

def main():

    command = parser.parse_args().command
    if command in register_command:
        args = parser.parse_args().args
        getattr(_manage, command)(args)
    else:
        print("< {} > - нет такой команды".format(command))





if __name__ == "__main__":
    main()