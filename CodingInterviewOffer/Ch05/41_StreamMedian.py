# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/2 22:37
'''
面试题41：数据流中的中位数
题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''

class Solution:
    # 常规操作
    def __init__(self):
        self.data = []

    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()

    def GetMedian(self, data):
        # write code here
        length = len(self.data)
        if length % 2 == 0:
            return (self.data[length // 2] + self.data[length // 2 - 1]) / 2.0
        else:
            return self.data[int(length // 2)]


"""
为了保证插入新数据和取中位数的时间效率都高效，这里使用大顶堆+小顶堆的容器，并且满足：
1、两个堆中的数据数目差不能超过1，这样可以使中位数只会出现在两个堆的交接处；
2、大顶堆的所有数据都小于小顶堆，这样就满足了排序要求。
构建一个最大堆和一个最小堆，分别存储比中位数小的数和大的数。
当目前两堆总数为偶数的时候，把数字存入最大堆，然后重排最大堆，如果最大堆的堆顶数字大于最小堆堆顶数字，
则把两个堆顶数字交换，重排两堆，此时两堆数字总数为奇数，直接输出最大堆堆顶数字即为中位数；
如果当前两堆总数为奇数的时候，把数字存入最小堆，重排最小堆，如果最大堆的堆顶数字大于最小堆堆顶数字，
则把两个堆顶数字交换，重排两堆，此时两堆数字总数为偶数，取两堆堆顶数字做平均即为中位数
最大堆堆顶元素要小于最小堆堆顶的元素，最大堆，堆顶元素最大，从大到小，最小堆堆顶元素最小，从小到大，这样的话，
最大堆所有元素均小于最小堆了，中位数一定出现在两堆交替之间。
"""


class Solution2:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.count = 0

    def Insert(self, num):
        if self.count & 1 == 0:  # 如果是偶数
            self.maxHeap.append(num)  # left为最大堆
        else:
            self.minHeap.append(num)  # right为最小堆
        self.count += 1

    def GetMedian(self, x):
        if self.count == 1:
            return self.maxHeap[0]
        self.MaxHeap(self.maxHeap)
        self.MinHeap(self.minHeap)
        if self.maxHeap[0] > self.minHeap[0]:
            self.maxHeap[0], self.minHeap[0] = self.minHeap[0], self.maxHeap[0]
        self.MaxHeap(self.maxHeap)
        self.MinHeap(self.minHeap)
        if self.count & 1 == 0:  # 如果是偶数个数目
            return (self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return self.maxHeap[0]

    def maxHeapfy(self, alist, length, parent):
        left = 2 * parent + 1
        right = 2 * parent + 2
        largest = parent

        if left < length and alist[left] > alist[largest]:
            largest = left
        if right < length and alist[right] > alist[largest]:
            largest = right
        if largest != parent:
            alist[largest], alist[parent] = alist[parent], alist[largest]
            self.maxHeapfy(alist, length, largest)

    def MaxHeap(self, alist):
        n = len(alist)
        lastParent = (n - 1) // 2  # (层序遍历)最后一个父节点
        for i in range(lastParent, -1, -1):
            self.maxHeapfy(alist, n, i)

    def minHeapfy(self, alist, length, parent):
        left = 2 * parent + 1
        right = 2 * parent + 2
        largest = parent

        if left < length and alist[left] < alist[largest]:
            largest = left
        if right < length and alist[right] < alist[largest]:
            largest = right
        if largest != parent:
            alist[largest], alist[parent] = alist[parent], alist[largest]
            self.maxHeapfy(alist, length, largest)

    def MinHeap(self, alist):
        n = len(alist)
        lastParent = (n - 1) // 2  # (层序遍历)最后一个父节点
        for i in range(lastParent, -1, -1):
            self.minHeapfy(alist, n, i)
   
if __name__ == '__main__':
    t = Solution()
    t.Insert(5)
    print(t.GetMedian(t))
    t.Insert(2)
    print(t.GetMedian(t))
    t.Insert(3)
    print(t.GetMedian(t))
    t.Insert(3)
    print(t.GetMedian(t))

    print('------------------------')
    t = Solution2()
    t.Insert(5)
    print(t.GetMedian(t))
    t.Insert(2)
    print(t.GetMedian(t))
    t.Insert(3)
    print(t.GetMedian(t))
    t.Insert(3)
    print(t.GetMedian(t))
