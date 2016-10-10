'''
Created on 2015年4月13日

@author: Administrator
'''
# 元组和列表类似（可以索引，可以切片，字符串是特殊的元组），不同之处是
# 1.元组的元素不能改变,但是可以包含可变对象
# 2.构造包含0或1个元素的元组是个问题
# 空元组
tup1 = ();
# 1个元素的元组，必须额外加个逗号
tup2 = (2,);

a = (1991, 2014, 'sdf', 'sdfsdf', True);
print(a);

# 元组支持+号
a = (12, 33, True);
a += (2, 3);
print(a);
# string list tuple 都属于 sequence


# 初始化,用逗号
t = 12222, 21222, 'ddd';
print(t);
t = 1, t;
print(t);
