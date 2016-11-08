def trans(dist, src):
    import os
    for rt, dirs, files in os.walk("."):
        for f in files:
            fname = os.path.splitext(f)
            if src == "" or fname[1] == "." + src:
                new = fname[0] + '.' + dist
                os.rename(os.path.join(rt, f), os.path.join(rt, new))


def print_help():
    print('''dist [src]
    dist 目标后缀
    src  源后缀可选参数 默认实配所有后缀
    示例:
    [this py] less   ->  将所有文件后缀改为less
    [this py] less css  ->  将所有后缀css的文件改为less后缀
                ''')


def handle(args):
    if len(args) < 1:
        print_help()
    elif args[0] == "help" or args[0] == "-help":
        print_help()
    else:
        dist = args[0]
        src = ""
        if len(args) > 1:
            src = args[1]

        trans(dist, src)


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    handle(args)
