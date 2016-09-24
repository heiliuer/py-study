# 转义
s = 'Yes,he dosen\'t';
print(s, type(s));
s = 'Yes,he dosen\nt';
print(s, type(s));

# 不转义
s = r'Yes,he dosen\'t';
print(s);
# 不转义
s = r'Yes,he dosen\nt';
print(s);

# 续行符
s = r'wwwww\
dddddddddd\
sddddddddd\
dddddd';
print(s);

s = """ddddddd
sdfsssssssss
ssssssss""";
print(s);

print('ddd' * 20);

# 字符串索引
word = 'Python';
print(word[0], word[5]);
# 从右到左，从-1递减（-1代表最后一个）
print(word[-6], word[-1]);



# 字符串进行切片
s = "abcdef"
# 复制字符串
print(s[:]);
# f
print(s[-1]);
# null
print(s[-1:1]);
# null
print(s[-2:1]);
# e
print(s[-2:-1]);


# 字符串是不能改变某个字符的值
s = "11111";
# 报错 'str' object does not support item assignment
s[0] = '1';

# 使用了一个转义符，避免在最开始产生一个不需要的空行。
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")





