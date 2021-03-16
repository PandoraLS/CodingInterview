# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/1 16:53

from heapq import *


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap = []
        heapify(heap)  # python默认小顶堆
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]  # heap[0]是堆顶
