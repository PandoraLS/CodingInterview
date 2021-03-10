# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/4/6 15:37

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        length = len(nums)
        left = 0
        right = length - 1
        while left < right:  # bisect_left确定res[0]
            mid = left + (right - left) // 2
            # 当nums[mid]严格小于target时，不是解
            if nums[mid] < target:
                # 下一轮搜索区间为
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            res.append(left)
        else:
            res.append(-1)
        
        left = 0
        right = length - 1
        
        while left < right:  # bisect_right确定res[1]
            mid = left + (right - left + 1) // 2  # 有可能进入死循环，所以向上取整
            # 当nums[mid]严格大于target时，不是解
            if nums[mid] > target:
                # 下一轮搜索区间为
                right = mid - 1
            else:
                left = mid
        if nums[left] == target:
            res.append(left)
        else:
            res.append(-1)

        return res


if __name__ == '__main__':
    so = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(so.searchRange(nums, target))
