#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import sys
import os


def print_help():
    print('''[this py] <cmd>
    cmd:命令名称，如：mvn node
    示例:
        [this py] mvn   ->  打开mvn环境变量所在文件夹
                ''')


def open_path_in_explore(path):
    os.system("explorer.exe  \"{}\"".format(path))


def locate_file_in_explore(file):
    os.system("explorer.exe /select, \"{}\"".format(file))


def print_no_newline(str):
    sys.stdout.write(str)
    sys.stdout.flush()


def read_a_num():
    try:
        cha = int(input())
        return cha
    except:
        return -1


def open_file_by_num(files, num):
    if 0 < num <= len(files):
        # open_path_in_explore(os.path.dirname(files[num - 1]))
        locate_file_in_explore(files[num - 1])
        return True
    print_no_newline('invalid num:')
    return False


def handle(cmd):
    cmd = "where \"{}\"".format(cmd)

    try:
        output = subprocess.check_output(cmd, shell=False, stderr=subprocess.STDOUT)
        result = output.decode("GBK")
    except Exception as e:
        print(e.output.decode("GBK"))
        return

    if len(result) > 0:
        files = result.split("\r\n")
        files = [file for file in files if len(file) > 0]
        if len(files) > 1:
            print("select to open:")
            print('\n'.join((str(index + 1) + '. ' + file) for (index, file) in enumerate(files)))
            print_no_newline('enter num:')
            while not open_file_by_num(files, read_a_num()):
                pass
        elif len(files) == 1:
            open_file_by_num(files, 1)


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 1:
        print_help()
    else:
        handle(args[0])
