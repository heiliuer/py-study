#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import sys


def handle_path(path):
    ab_path = os.path.abspath(path)
    if not os.path.isdir(ab_path):
        return None
    return ab_path


def print_no_newline(str):
    sys.stdout.write(str)
    sys.stdout.flush()


def read_a_str():
    try:
        cha = input()
        return cha
    except:
        return -1


def fast_del(handled_paths):
    for path in handled_paths:
        os.system("del /f/s/q \"{}\" > nul|rmdir /s/q \"{}\"".format(path, path))


if __name__ == "__main__":
    argv = sys.argv
    cwd = os.getcwd()
    handled_paths = []
    if len(argv) > 1:
        paths = argv[1:]
        for path in paths:
            handled_path = handle_path(path)
            if handled_path is not None:
                handled_paths.append(handled_path)
            else:
                print("%s is not exist!" % os.path.abspath(path))
    else:
        handled_paths.append(os.path.abspath(""))
    if len(handled_paths) > 0:
        print("\nFast delete below folders?")
        print(
            '\n'.join(
                ('  ' + str(index + 1) + '. ' + handled_path) for (index, handled_path) in
                enumerate(handled_paths)) + '\n')
        print_no_newline('Y/n:')
        ans = read_a_str()
        if ans in ["y", "Y"]:
            fast_del(handled_paths)
            print("delete completed!")
        else:
            print("nothing changed!")
