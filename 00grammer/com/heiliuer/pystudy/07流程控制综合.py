'''
Created on 2015年4月13日

@author: Administrator
'''
# python 中没有switch 语句


# if语句
age = 0;
# age = input("please enter the age!\n");
age = int(age);
if age > 80:
    print("old");
elif age > 60:
    print("middle");
elif age > 40:
    print("hanzi");
else:
    print("young");
    
   

# for语句  for <variable> in <sequence>:
#!/usr/bin/env python3    在linux中告诉系统运行环境，使代码可以像shell一样用
edibles = ["ham", "spam2", "eggs", "nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        break
    print("Great, delicious " + food)
else:  # 好强大，靠缩进进行不同作用域中的else和if的匹配
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")


# range函数
# 从0到XX
for i in range(10):
    print(i);
print(range(10));

# 从XX到YY
for i in range(2, 10):
    print(i);
print(range(10));

# 步进
for i in range(2, 10, 3):
    print(i);
print(range(10));

print(list(range(10)));

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, 'is a prime number')
        
        
# pass语句 什么都不做
while True:
    pass;

# 最小的类
class Test:
    pass;



    
