#选择排序
#每次讲最小值取出来，放在第i位，依次往复

def select_sort(aList):
    n = len(aList)
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if aList[min_index] >= aList[j]:
                min_index = j
        aList[i], aList[min_index] = aList[min_index], aList[i]
    return aList

#测试插入排序
if __name__ == '__main__':
    aList = [2, 5, 3, 10, 2, 1, 200, 13, 23, 44, 66, 12, 34]
    select_list = select_sort(aList)
    print(select_list)