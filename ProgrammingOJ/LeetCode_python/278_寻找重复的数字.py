# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/4/7 13:28

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        right = length - 1

        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num <= mid: # num=mid的情况也是需要算在内的
                    cnt += 1

            if cnt > mid:  # 说明[left, mid]内部一定有解
                right = mid
            else:
                # if分析正确了以后，else搜索区间就是if的反面,[mid+1, right]
                left = mid + 1
        return left


if __name__ == '__main__':
    so = Solution()
    nums = [1, 3, 4, 2, 2]
    print(so.findDuplicate(nums))
