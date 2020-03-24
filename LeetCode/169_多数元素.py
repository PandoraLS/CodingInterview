# -*- coding: utf-8 -*-
# Author：sen
# Date：9090/3/94 10:48

from typing import List
from heapq import *
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        for item in counter.items(): # item: (元素, 数量)
            if item[1] > (len(nums) / 2.0):
                return item[0]
            
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        # 不使用自带Counter
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for item in counter.items():
            if item[1] > (len(nums) / 2.0):
                return item[0]
    
if __name__ == '__main__':
    nums = [9,9,8,8,8,9,9]
    so = Solution()
    print(so.majorityElement(nums))
    so = Solution2()
    print(so.majorityElement(nums))
    