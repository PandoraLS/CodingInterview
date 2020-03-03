# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/2 21:49

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        idx_q = deque()  # 双端队列，存放的是下标
        res = []  # 
        for i, num in enumerate(nums):  # i是下标,num是nums[i]
            while idx_q and idx_q[0] <= i - k:  # 如果队列头(左)被滑出，则pop出去
                idx_q.popleft()
            while idx_q and nums[idx_q[-1]] < num:
                # 如果双端队列尾部比nums[i]小，则弹出尾部，因为此时尾部小值不可能是最大值
                idx_q.pop()
            idx_q.append(i)
            if i >= k - 1:  # 如果数组nums的下标超过窗口长度，则队列头(左)为此次窗口滑动的最大值
                res.append(nums[idx_q[0]])
        return res

if __name__ == '__main__':
    so = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(so.maxSlidingWindow(nums, k))
