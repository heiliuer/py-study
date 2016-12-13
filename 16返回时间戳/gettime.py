#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from time import gmtime, strftime
import time


def print_help():
    print('\n' + file_name + ''' [type]\n
type. result''')
    datas = (str(index + 1) + '. ' + formater[1] for index, formater in enumerate(formaters))
    print('\n'.join(datas))


def print_no_newline(str):
    sys.stdout.write(str)
    sys.stdout.flush()


def read_as_int(arg):
    try:
        return int(arg)
    except:
        pass
    return None


formaters = [("%Y%m%d%H%M%S", "20161213165210"), ("$QQ", "1481648398133 时间戳"), ("%Y%m%d%H%M", "201612131652"),
             ("%Y-%m-%d-%H-%M", "2016-12-13-16-52")]


def print_time(type=0):
    if type < 0 or type > len(formaters) - 1:
        print("invalid type")
    else:
        mtime = str(round(time.time() * 1000))
        ftime = strftime(formaters[type][0], gmtime())
        print(ftime.replace('$QQ', mtime))


def handle(args):
    if len(args) > 0:
        type = read_as_int(args[0])
        if type is None:
            print_help()
            return
        print_time(type - 1)
    else:
        print_time()


file_name = None

if __name__ == '__main__':
    argv = sys.argv
    file_name = os.path.basename(argv[0])
    handle(argv[1:])
