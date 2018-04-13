# coding:utf8
# 归并排序merge sort的python

def merge(a, b):
    result = []
    left = right = 0
    while right < len(a) and left < len(b):
        if a[right] < b[left]:
            result.append(a[right])
            right += 1
        else:
            result.append(b[left])
            left += 1
    # 将剩余的部分(可能存在一个长度遍历完了，但另外一个长度还有很多)
    # 入到c
    if right == len(a):
        for i in b[left:]:
            result.append(i)
    else:
        for i in a[right:]:
            result.append(i)

    return result

# 选择用递归的方式
def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


if __name__ == '__main__':
    a = [17, 23, 89, 35, 28, 90, 10, 12]
    print(merge_sort(a))