# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/1 22:36
from heapq import *


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        # 最小堆
        m, n = len(matrix), len(matrix[0])
        min_heap = []
        for i in range(m):
            for j in range(n):
                heappush(min_heap, matrix[i][j])
        for i in range(k-1):
            heappop(min_heap)
        return heappop(min_heap)


if __name__ == '__main__':
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    so = Solution()
    print(so.kthSmallest(matrix, 8))
