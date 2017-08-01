#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
from time import gmtime, strftime


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


formaters = [("%Y%m%d%H%M%S", "20161213165210"), ("%Y_%m%d_%H%M%S", "2016_1213_165210"), ("$QQ", "1481648398133 时间戳"),
             ("%Y%m%d%H%M", "201612131652"),
             ("%Y-%m-%d-%H-%M", "2016-12-13-16-52")]


def exec_cmd(cmd):
    # print({
    #     cmd
    # })
    os.system(cmd)


def print_time(type=1):
    if type < 0 or type > len(formaters) - 1:
        print("invalid type")
    else:
        mtime = str(round(time.time() * 1000))
        ftime = strftime(formaters[type][0], gmtime())
        time_str = ftime.replace('$QQ', mtime)
        print(time_str)
        exec_cmd('echo |set /p="' + time_str + '"|clip')


def handle(args):
    args_length = len(args)
    if args_length > 0:
        arg0 = args[0].strip()
        if arg0 == '':
            print_time()
        else:
            type = read_as_int(arg0)
            # print({arg0})
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
