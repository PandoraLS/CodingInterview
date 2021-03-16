# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/1 18:09

from heapq import *


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0  # 当前大顶堆和小顶堆个数之和
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        self.count += 1
        # python默认小顶堆，用(-num, num)模拟大顶堆
        heappush(self.max_heap, (-num, num))  # 先放入最大堆
        _, max_top = heappop(self.max_heap)  # 弹出最大堆的最大值
        heappush(self.min_heap, max_top)  # 将最大堆的最大值push到最小堆
        if self.count & 1:  
            # 如果总数字数量为奇数，说明最小堆多了一个(因为最后有个数流到了最小堆中)
            # 此时需要将最小堆的最小数字送一个到最大堆中
            min_top = heappop(self.min_heap)
            heappush(self.max_heap, (-min_top, min_top))

    def findMedian(self) -> float:
        if self.count & 1: # 如果是奇数
            return self.max_heap[0][1]
        else:
            return (self.min_heap[0] + self.max_heap[0][1]) / 2


if __name__ == '__main__':
    so = MedianFinder()
    so.addNum(1)
    so.addNum(2)
    print(so.findMedian())
    so.addNum(3)
    print(so.findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
