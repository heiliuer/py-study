import math
from pprint import pprint
s = "Hello world!";
print(str(s));
print(repr(s));  # 编译器是别的类型


# 字符串格式化输出
print("{0:2d}{1:3d}{2:4d}{sep}".format(22, 333, 444, sep=','));

print("\n字符串输出右对齐");
print("23".rjust(10));
print("23"*5);

print("\n字符串输出居中");
print("23".center(10));
print("23"*5);

print("\n字符串输出右对齐");
print("23".zfill(10));
print("23"*5);

# 输出是转换为ansci
print("{!a}".format("王豪"));
# 输出是转换为ansci
print("{!s}".format(math.pi));
# 输出是转换为repr
print("{!r}".format('nihao'));
# 保留3位小数
print("{:.3f}".format(math.pi));

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678};
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d};Dcab: {0[Dcab]:d}'.format(table));
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d};Dcab: {0[Dcab]:d}'.format(**table));

#################文件处理#######################
# 打开文件
file = open("__init__.py", "w+");
# print(file.read());
# 读取是流式的
print(file.readline());  # return a line
print(file.readlines());  # return lines[list]
# 通过迭代文件对象，获取每一行
for line in file:
    print(line);
file.write("#test");
# 获取文件对象当前位置距离开头处的字节数
file.tell();
# 位置游走
# file.seek(2, 2);
# 关闭文件
file.close();



#################pickle模块，序列化和反序列化#######################
# 按python代码格式输出字符串
pprint
