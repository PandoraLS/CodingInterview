# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/9 20:04
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = sorted(nums)
        j = len(a) - 1

        # 错开'中'
        for i in range(1, n, 2):  # 在偶数位把数从大到小排下去
            nums[i] = a[j]
            j -= 1
        for i in range(0, n, 2):  # 在奇数位把数从大到小排下去
            nums[i] = a[j]
            j -= 1

        return nums


if __name__ == '__main__':
    nums = [1, 5, 2, 3, 6, 4]
    so = Solution()
    print(so.wiggleSort(nums))
