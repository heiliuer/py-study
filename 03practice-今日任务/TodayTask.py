'''
Created on 2015-8-21
@author: Lexue
'''
import os
from os.path import sys
import time
#args = sys.argv;
#args = args[1:];
# open(time.strftime('%Y-%m-%d-%H-%M') + ".txt",'a')
fileName=time.strftime('%Y-%m-%d') + ".txt";
file=open(fileName,'a');
file.close();
os.system("start "+fileName);
