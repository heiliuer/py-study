'''
Created on 2015年4月13日

@author: Administrator
'''
# 集合是元素不重复的序列，基本功能是进行成员关系的测试，消除重复

# 创建集合
# 用{}
stu = {'wh', 'lb'};
print(stu);
# 创建空集合，必须用set()
nullSet = set();
# 空字典
nullDict = {};

# 用set方法
stu = set('dddddddddd');  # 自动去重
print(stu);
print('d' in stu);
print('dd' in stu);

stu = set('dddddddd' * 2);
print(stu);

# 报错 set expected at most 1 arguments, got 2
# stu = set('dddddddd' , 'wsdf');
# print(stu);


# 集合可以进行集合并，交等计算

a = set("abcdef");
b = set("defghij");
# 并
print(a | b);
# 差
print(a - b);
# 交
print(a & b);
# a,b中不同时存在的，即a|b-a&b
print(a & b);



