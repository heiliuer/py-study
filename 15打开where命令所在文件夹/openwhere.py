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
    os.system("explorer.exe \"{}\"".format(path))


def handle(cmd):
    cmd = "where \"{}\"".format(cmd)

    try:
        result = subprocess.check_output(cmd, shell=False, stderr=subprocess.STDOUT).decode()
    except Exception as e:
        result = e.output.decode()

    if len(result) > 0:
        files = result.split("\r\n")
        for file in files:
            if len(file.strip()) > 0:
                open_path_in_explore(os.path.dirname(file))


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 1:
        print_help()
    else:
        handle(args[0])
