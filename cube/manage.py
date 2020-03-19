#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from libs import manage
import click

@click.command()
@click.option('--command', "-c", default="-", help='название команды')
@click.option('--name', "-n", default=None, help='имя плагина')
def main(command, name):
    try:
        getattr(manage, command)(name)
    except AttributeError as repl:
        print("Нет такой команды")
        raise Exception("< {} > - Нет такой команды".format(command))



if __name__ == "__main__":
    main()