'''
Created on 2015年5月7日

@author: Administrator
'''
import os;
import sys
from _overlapped import NULL


def goToPwdFolder(pwd):
    for i in pwd:
        try:
            #           os.mkdir(i);
            os.chdir(i);
        except Exception:
            print("folder[%s%s] not exits:" % (os.getcwd(), i));
            return;
            #        os.chdir(i);
    os.system("start .");


#     [chr(c) for c in range(97,123)]+
files = [str(c) for c in range(0, 10)];


def make(deep, cdir=NULL):
    if cdir:
        os.chdir(cdir);
    newDeep = deep - 1;
    if newDeep >= 0:
        for i in files:
            try:
                # print("cwd:",os.getcwd()," and mkdir ",i);
                os.mkdir(i);
            except Exception:
                pass;
            make(newDeep, i);
    os.chdir("..");


if __name__ == "__main__":
    args = sys.argv;
    argsLength = len(args);
    if argsLength == 1 or args[1] == "help" or args[1] == "-help":
        print('''\
用法说明
make 生成混淆文件夹
**** 访问密码文件夹
        '''
              );
        sys.exit();
    arg = args[1];
    if arg == "make":
        if argsLength < 3:
            print("make 缺少参数（deep深度）");
            exit();
        else:
            print("正在生成混淆文件夹。。。");
            make(deep=int(args[2]));
            print("完成");
    else:
        goToPwdFolder(args[1]);
