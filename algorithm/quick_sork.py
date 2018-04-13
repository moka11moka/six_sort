
#这一步相当于图片上的展示，将第一个值作为key,
# 比key大的放在key的右边，比key小的放在key的左边
#first和last就相当于图片中的i和j


def partition(aList, first, last):
    key = aList[first]
    low = first
    high = last
    while low < high:
        # high相当于图片中j从右往左遍历
        # 遇到比key值小的，将high所对应的值赋给low所对应的值
        # 如果没有比key小的，high-1
        while (low < high) and (key <= aList[high]):
            high = high - 1
        aList[low] = aList[high]

        # low相当于图片中的i从左往右遍历，如果遇到
        # 遇到比key值大的，将low所对应的值赋给high所对应的值
        # 如果没有比key大的，low = low + 1
        while (low < high) and (key >= aList[low]):
            low = low + 1
        aList[high] = aList[low]
        aList[low] = key
    # 出口是low==high
    return low


# quick sort实现
def quick_sort(aList, first, last):
    if first < last:
        # 结果返回的key值，最后递归
        key = partition(aList, first, last)
        quick_sort(aList, first, key-1)
        quick_sort(aList, key+1, last)
    return aList


if __name__ == '__main__':
    aList = [17, 23, 89, 35, 28, 90, 10]
    n = len(aList)
    quick_sort(aList, 0, n-1)
    print(aList)


