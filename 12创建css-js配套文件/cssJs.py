import click
import os


@click.command()
@click.option('--jr', default="js", help="js根目录")
@click.option('--cr', default="css", help="css根目录")
@click.option('--lr', default="css", help="less根目录")
@click.argument('path')
@click.argument('file')
def handle(path, file, jr, cr, lr):
    """css js less文件快速创建工具"""
    mk_file(jr + os.path.sep + path, file + ".js")
    mk_file(lr + os.path.sep + path, file + ".less")
    mk_file(cr + os.path.sep + path, file + ".css")


def mk_file(path, file_name):
    if not os.path.isdir(path):
        os.makedirs(path)
    cwd = os.getcwd()
    os.chdir(path)
    if not os.path.isfile(file_name):
        touch(file_name)
    os.chdir(cwd)


def touch(file_name, times=None):
    h = open(file_name, 'a')
    try:
        os.utime(file_name, times)
    finally:
        h.close()


if __name__ == '__main__':
    handle()
