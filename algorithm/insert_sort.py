#插入排序
#视作前面的都有序，逐个插入,后面的元素逐个插入

def insert_sort(aList):
    n = len(aList)
    for i in range(0, n):
        j = i
        while aList[j] <= aList[j-1]:
            aList[j-1], aList[j] = aList[j], aList[j-1]
            if j == 1:
                break
            else:
                j = j-1

    return aList


#测试插入排序
if __name__=='__main__':
    aList = [2, 5, 3, 10, 2, 1, 200, 13, 23, 44, 66, 12, 34]
    insert_sort = insert_sort(aList)
    print(insert_sort)