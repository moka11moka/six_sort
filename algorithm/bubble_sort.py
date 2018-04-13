# 自己实现的一个冒泡排序
# 冒泡排序是最基本的排序，最符合我们能够想到的排序
#思路：就是将最大的一个数（最小）依次比较之后，然后做交换，最后放在最后的位置

#外层循环是内部循环的总和
def bubble_sort(aList):
    n = len(aList)
    for j in range(0, n-1):
        for i in range(0, n-j-1):
            if aList[i] >= aList[i+1]:
                aList[i], aList[i+1] = aList[i+1], aList[i]
    return aList

# 测试

if __name__ == '__main__':
    #注意：list是用[],tuple才用()
    aList = [2, 5, 3, 10, 2, 1,200, 13, 23, 44, 5, 66, 12, 34]
    bubble_list = bubble_sort(aList)
    print(bubble_list)
