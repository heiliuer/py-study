'''
Created on 2015年4月13日

@author: Administrator
'''
# 字典是一种映射类型，有无序的键值对组成
# 键值必须是不可变类型，list和元组不能作为关键字，键值要唯一

print(type({1}));
# 空字典
print(type({}));

data = {'name':'wanghao', "age":23};
print(data);
print("data", data['name']);
# del data['age'];
print(data);
# keys() return a set-like object providing a view on D's keys
print(data.keys());
print(set(data.keys()));
print(list(data.keys()));
# values() retunr an object providing a view on D's values
print(data.values());
print(set(data.values()));
print(list(data.values()));

print("name" in data);
print("name" not  in data);
print(sorted(list(data.keys())));


# dict build
data = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]);
print(data);
data = dict(sape=4139, guido=4127, jack=4098);
print(data);

# build for
data = {x: x ** 10 for x in (2, 4, 6)};  # **指数运算
print(data);

data = "ddd""ddd";
print(data);

data = {'guido': 4127, 'irv': 4127, 'jack': 4098};
print('guido' in data);#True
print(4127 in data);#False

#遍历
for k,v in data.items():
    print(k,v,sep=':');
#获取索引值和key值遍历
for i,k in enumerate(data):
    print(i,k,sep=',');



