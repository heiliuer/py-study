# 简单选择 时间复杂度O()
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


# 简单选择 时间复杂度O()
def sort_by_insert(array):
    a_len = len(array)
    if a_len == 0:
        return
    rs = array[:1]
    for i in range(a_len):
        min_a = i
        for j in range(i + 1, a_len):
            if array[j] < array[min_a]:
                min_a = j
        if min_a > i:
            tmp = array[i]
            array[i] = array[min_a]
            array[min_a] = tmp


if __name__ == "__main__":
    data = [2, 6, 2, 1, 1, 5, 4]
    print("origin：", data)
    sort_by_select(data)
    print("sorted: ", data)
