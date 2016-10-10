# 冒泡排序 时间复杂度O(n^2)
def sort_by_bubbling(array):
    a_len = len(array)
    for i, a in enumerate(array):
        for j in range(i + 1, a_len):
            if array[j] < a:
                tmp = array[j]
                array[j] = a
                array[i] = tmp


# 简单选择 时间复杂度O() 依次把n-i中最小值挪到第i位
def sort_by_select(array):
    a_len = len(array)
    if a_len == 0:
        return
    for i in range(a_len):
        min_a = i
        for j in range(i + 1, a_len):
            if array[j] < array[min_a]:
                min_a = j
        if min_a > i:
            tmp = array[i]
            array[i] = array[min_a]
            array[min_a] = tmp


# 直接插入排序 时间复杂度O() 依次将第i位挪到i-1排序好的序列合适的位置
def sort_by_insert(array):
    a_len = len(array)
    if a_len == 0:
        return
    for i in range(1, a_len):
        tmp = array[i]
        j = i - 1
        while j > -1 and tmp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = tmp


# 希尔排序 时间复杂度O() 依次每n/2分组，每组进行直接插入排序
def sort_by_shell(array):
    n = len(array)
    for gap in shell_range(n, 2):
        for j in range(gap, n):
            # 从数组第gap个元素开始
            if array[j] < array[j - gap]:
                # 每个元素与自己组内的数据进行直接插入排序
                temp = array[j]
                k = j - gap
                while k >= 0 and array[k] > temp:
                    array[k + gap] = array[k];
                    k -= gap;
                array[k + gap] = temp;


def shell_range(n, times):
    while n > 0:
        n = int(n / times)
        yield n


if __name__ == "__main__":
    data = [2, 6, 2, 1, 1, 5, 4]
    print("origin：", data)
    sort_by_shell(data)
    print("sorted: ", data)
