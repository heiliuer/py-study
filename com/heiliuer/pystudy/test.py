import os;
print("initialing code" , os.listdir());

def func1():
    print("execute function func1");
    
if __name__ == "__main__":
    print("我自身执行了");
    pass;
else:
    print("我被其他模块import了");
    pass;
print("execute by ", __name__);  # 直接执行该模块时，__name__="__main__";其他模块导入子模块时，__name__=当前模块名
