import os
import sys
import time


def checkFile(files):
    exsitFiles = [];
    cwd = os.getcwd();
    for file in files:
        afile = cwd + "\\" + file;
        if os.path.exists(afile):
            exsitFiles.append(afile);
        else:
            print("[%s] does not exist!" % file);
    return exsitFiles;


def watchFile(files, config):
    lastTime = {};
    while True:
        for file in files:
            # os.system("start %s" % file);
            try:
                mtime = os.path.getmtime(file);  # unit s
                if file in lastTime and mtime != lastTime[file]:
                    callback(config, file);
                lastTime[file] = mtime;
            except:
                pass;
            try:
                time.sleep(0.2);
            except:
                print("exit!");
                return;


def callback(config, file):
    os.system(config % file);
    # print(config % file);


def readConfig():
    configFile = "/fwcmd.ini";
    classPath = sys.path[0];
    f = None;
    try:
        f = open(classPath + configFile, mode='r');
        return f.read();
    except:
        print("classPath:%s is not exist!" % configFile);
        pass;
    finally:
        if f:
            f.close();
    return "echo %s changed!";


if __name__ == '__main__':
    files = sys.argv[1:];
    # exsitFiles = checkFile(files);
    config = readConfig();
    if config:
        print("Wathing %d files,and Execute cmd {" % len(files), config % "[fileName]", "} when file changed!", sep='');
        watchFile(files, config);
