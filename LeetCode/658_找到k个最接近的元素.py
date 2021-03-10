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

class Solution2():
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 双指针删除法
        length = len(arr)
        left = 0
        right = length - 1

        # 总共需要删除length - k个元素
        remove_nums = length - k
        while remove_nums:
            # 调试语句
            # print(left, right, k)
            # 注意：这里等于号的含义，题目中说，差值相等的时候取小的
            if x - arr[left] <= arr[right] - x:
                right -= 1
            else:
                left += 1
            remove_nums -= 1
        return arr[left:left + k]


if __name__ == '__main__':
    # nums = [0, 1, 1, 1, 2, 3, 6, 7, 8, 9]
    # k, x = 9, 4
    # so = Solution()
    # print(so.findClosestElements(nums, k, x))
    
    
    nums2 = [1, 2, 3, 4, 5, 6, 7]
    k, x = 3, 5
    so = Solution2()
    print(so.findClosestElements(nums2, k, x))
    
    # nums3 = [0, 1, 2, 3, 3, 4, 7, 7, 8]
    # k, x = 3, 5
    # so = Solution2()
    # print(so.findClosestElements(nums3, k, x))
