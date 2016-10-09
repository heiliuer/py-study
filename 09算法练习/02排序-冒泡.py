# 冒泡排序 时间复杂度O(n^2)
def sort_by_bubbling(array):
    a_len = len(array)
    for i, a in enumerate(array):
        for j in range(i + 1, a_len):
            if array[j] < a:
                tmp = array[j]
                array[j] = a
                array[i] = tmp


if __name__ == "__main__":
    data = [1, 5, 4]
    print("origin：", data)
    sort_by_bubbling(data)
    print("sorted: ", data)
