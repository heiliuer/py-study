'''加法'''
print("导入了模块" + __name__);
def add(*nums):
    result = 0;
    for num in nums:
        result += num;
    return result;
'''乘法'''
def time(*nums):
    result = 1;
    for num in nums:
        result *= num;
    return result;
    
