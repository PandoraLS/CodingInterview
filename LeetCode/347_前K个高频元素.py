# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/2 18:25
from typing import List
from heapq import *
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        count_sorted = list(reversed(sorted(zip(count.values(), count.keys()))))
        res = []
        for i in range(k):
            res.append(count_sorted[i][1])
        return res


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # cc = Counter(nums)
        cnt = list(Counter(nums).items())
        cnt.sort(key=lambda x: x[1], reverse=True)
        return [cnt[i][0] for i in range(k)]


if __name__ == '__main__':
    nums = [8, 8, 7, 7, 7, 7, 7, 7, 9]
    k = 2
    so = Solution()
    print(so.topKFrequent(nums, k))
    so2 = Solution2()
    print(so2.topKFrequent(nums, k))
