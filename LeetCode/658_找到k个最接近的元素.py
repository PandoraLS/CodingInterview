# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/4/5 15:50

from typing import List
from collections import deque


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 1:
            return arr
        l, r = 0, len(arr) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if x <= arr[mid]:
                r = mid
            else:
                l = mid

        q = deque([])
        i, j = l, r
        while len(q) < k:
            if j == len(arr) or (0 <= i and x - arr[i] <= arr[j] - x):
                q.appendleft(arr[i])
                i -= 1
            else:
                q.append(arr[j])
                j += 1
        return list(q)


if __name__ == '__main__':
    nums = [0, 1, 1, 1, 2, 3, 6, 7, 8, 9]
    k, x = 9, 4
    so = Solution()
    print(so.findClosestElements(nums, k, x))
