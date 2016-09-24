'''\
    def fuc(paramsList):
        func body
'''
import sys;
def Hello():
    print('Hello');
Hello();


def Hello2(width, height):
    print(width, '*', height, '=' , width * height);
Hello2(23, 23);

a = 23;
# 全局变量
def Hello3():
    f = open("c://123.txt", "w");
    sys.stdout = f;
    a = 17;
    print(a);
#     print("d"*10000);
# Hello3();


# 关键字参数(下面的函数参数key value是关键字参数（带默认值，调用时可以不传递参数,必须放在positional argument（不带默认值）后面）)
def Hello4(key, value=''):
    print(key, value, sep=":");
Hello4(10, value=20);
# 报错 missing 1 required positional argument: 'key'
# Hello4(value=20);

# normal
Hello4(10);

# normal
Hello4(value=10, key=20);


# 函数的返回值,没有返回值，函数输出None
print(Hello4(value=10, key=20));

# 可变参数列表

def Hello5(*args):
    num = 0;
    for val in args:
        num += val;
    print("sum=", num);
Hello5(12.4, True);  # True 值为1

# 查看模块的所有方法
dir(sys);  # 输出sys.py模块中定义的所有方法的名称列表
dir();  # 输出当前模块中定义的所有方法的名称列表


# 标准模块

# sys
# sys.ps1;
# sys.ps2;
    
    





