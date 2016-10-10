# 不使用临时变量，交换两个整数值
import math


def swap_without_temp_var(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b


# 判断素数
def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num))):
            if num % i == 0:
                return False
    return True


if __name__ == "__main__":
    print(swap_without_temp_var(20, 5555))

    num = 1
    print("%d is prime ? %s" % (num, is_prime(num)))
    num = 23
    print("%d is prime ? %s" % (num, is_prime(num)))
