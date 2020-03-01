# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/1 19:39

from heapq import *


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, (-num, num))
        _, max_top = heappop(self.max_heap)
        heappush(self.min_heap, max_top)
        if self.count & 1:
            min_top = heappop(self.min_heap)
            heappush(self.max_heap, (-min_top, min_top))

    def findMedian(self) -> float:
        if self.count & 1:
            return self.max_heap[0][1]
        else:
            return (self.max_heap[0][1] + self.min_heap[0]) / 2