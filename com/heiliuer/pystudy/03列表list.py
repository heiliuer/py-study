'''
Created on 2015年4月13日

@author: Administrator
'''
# 列表是使用最频繁的数据类型

a = [1, 2, 'd', 'd', 23, True];
print(a, sep="a");

# 和字符串一样 ，可以索引,可以用*重复扩展
print(a[0:3] + [1, 323, 434] * 2);
print(a[-1]);

# 列表的元素是可以改变的
a[-1] = 'wanghao';
print(a);
# 改变其中部分
a[0:2] = [22, 22, 22, 22];
# 删除部分
# a[:] = [];
a[0:] = [];
print(a);

# 列表有append pop方法  和js类似

# 列表推导式

a = [[x, x ** 2] for x in range(23)];
print(a);

freshFruit = ['apple', 'peal', 'waltermellen', 'momkey ', ' dog '];
print([fruit.strip() * 2 for fruit in freshFruit if fruit.strip() != 'dog']);


vec1 = [2, 4, 6]
vec2 = [4, 3]
# 先x进行一次，y进行多次，y行x列
print([x * y for x in vec1 for y in vec2]);


matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ];
# 矩阵转置
print([[row[i] for row in matrix] for i in range(4)]);
# 同样可以用下面代码完成
transposed = [];
for i in range(4):
    transposed.append([row[i] for row in matrix]);
print(transposed);

# 遍历多个序列
questions = ['name', 'age'];
answers = ['王豪', 23];
for q, a in zip(questions, answers):
    print('what is your {0}?{1}!'.format(q, a));
    
    
# 反向序列
for i in reversed(range(1,10,2)):
    print(i);

#排序序列

for i in sorted([1,323,2323,True,False,34.2]):
    print(i);


