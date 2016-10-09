import time


# 二分法查找顺序列表的元素 时间复杂度O(log n)
def find_by_binary_search(array=[], data=0):
    length, low = len(array), 0
    high = length - 1
    while low <= high:
        mid = int((low + high) / 2)
        if data == array[mid]:
            return mid;
        elif data > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def get_current_timestamp():
    return int(time.time())


if __name__ == "__main__":
    start_time = get_current_timestamp()
    rs = find_by_binary_search(data=8, array=[0, 1, 2, 3, 5, 8, 9])
    print("spend time:%d , result: %d" % (get_current_timestamp() - start_time, rs))
