'''
Created on 2015-9-11
cmds 工具 给多个路径执行命令
@author: Lexue
'''
import os
import sys

#cmd
cmd="call mvn eclipse:clean eclipse:eclipse";

args=sys.argv;
if len(args)<=1:
    print("\n请输入要执行的路径(多个)！");
args=args[1:];
path=[];
findP=False;
P="";
for index in range(len(args)):
	p=args[index];
	if not findP and (p=="-p" or p=="-P"):
		findP=True;
		continue;
	if findP:
		P+=" "+p;
	else:
		path.append(p);
#print(path,,P);
'''
	注释
'''	
cmd+=P;
for p in path:
    try:
        os.chdir(p);
        os.system(cmd);
        os.chdir("../");
    except:
        print(p,' 路径不存在');      
    

