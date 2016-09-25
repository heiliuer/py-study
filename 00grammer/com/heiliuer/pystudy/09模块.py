# python解析器执行的东西，是流逝的，变量关闭就消失了
# python 加入模块的定义，将脚本放到文件中，利用python xxx.py <参数>
# python 09模块.py 1 2 3 4 45
import sys;  # 引入模块sys.py
print('参数列表如下：');
print(sys.argv, sep=',');

# 模块名不能已数字开头，要以字母或者下划线开头， 不然导入报错

# 输出记录搜索模块的路径的值，类似环境变量path
print(sys.path);  # 例如  ['D:\\Users\\Administrator\\Documents\\eclipsePython\\PythonHello\\com\\heiliuer', 'D:\\Users\\Administrator\\Documents\\eclipsePython\\PythonHello', 'D:\\Users\\Administrator\\Documents\\eclipsePython\\PythonHello\\com', 'D:\\Program Files\\Python34\\lib\\site-packages\\django-1.9-py3.4.egg', 'D:\\Program Files\\Python34\\DLLs', 'D:\\Program Files\\Python34\\lib', 'D:\\Program Files\\Python34', 'D:\\Program Files\\Python34\\lib\\site-packages', 'C:\\Windows\\system32\\python34.zip']

# 模块除了自定义方法外，还可以包含其他可执行代码，这些代码一般用来初始化这个模块，而且只会在第一次引入时调用

def fun1():
    print("excute fun1");
