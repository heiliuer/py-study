import os
import sys
import time


def checkFile(files):
    exsitFiles = [];
    cwd = os.getcwd();
    for  file in files:
        afile = cwd + "\\" + file;
        if  os.path.exists(afile):
            exsitFiles.append(afile);
        else:
            print("[%s] does not exist!" % file);
    return exsitFiles;


def watchFile(files, config):
    lastTime = {};
    while True:
        for file in files:
            # os.system("start %s" % file);
            mtime = os.path.getmtime(file);  # unit s
            if file in lastTime and mtime != lastTime[file]:
                callback(config, file); 
            lastTime[file] = mtime;
        time.sleep(0.2);

def callback(config, file):
    os.system(config % file);
    #print(config % file);
  
  
def readConfig():
    classPath = sys.path[0];
    f = open(classPath + "/fwcmd.ini", mode='r');
    try:
        return f.read();
    finally:
        f.close();
    return None;
    

if __name__ == '__main__':
    args = sys.argv[1:];
    exsitFiles = checkFile(args);
    config = readConfig();
    if config:
        print("Wathing %d files,and Execute cmd {"%len(exsitFiles),config%"[fileName]","} when file changed!",sep='');
        watchFile(exsitFiles, config);

