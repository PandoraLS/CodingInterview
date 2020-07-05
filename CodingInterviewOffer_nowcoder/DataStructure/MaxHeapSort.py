# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/4 14:06

def maxHeapfy(alist, length, parent):
    left = 2 * parent + 1
    right = 2 * parent + 2
    largest = parent

    if left < length and alist[left] > alist[largest]:
        largest = left
    if right < length and alist[right] > alist[largest]:
        largest = right
    if largest != parent:
        alist[largest], alist[parent] = alist[parent], alist[largest]
        maxHeapfy(alist, length, largest)


def buildMaxHeap(alist):  # 构建最大堆
    n = len(alist)
    lastParent = (n - 1) // 2  # (层序遍历)最后一个父节点
    for i in range(lastParent, -1, -1):
        maxHeapfy(alist, n, i)


def heapSort(alist):
    buildMaxHeap(alist)
    n = len(alist)
    for i in range(n - 1, -1, -1):
        alist[0], alist[i] = alist[i], alist[0]
        maxHeapfy(alist, i, 0)
    return alist


if __name__ == '__main__':
    import random
    random.seed(10)
    alist = [random.randint(1,100) for i in range(10)]
    print(alist)
    print(heapSort(alist))
