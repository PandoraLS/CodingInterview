# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/4/5 11:59
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        if nums[r] > nums[0]:  # 最后一个元素大于第一个元素时，说明数组无旋转，此时最小值为nums[0]
            return nums[0]
        
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid+1]:  # 如果中间元素比后面一个大，那后面一个就是最小值
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:  # 如果中间元素比前面一个小，那么当前元素就是最小值
                return nums[mid]
            
            if nums[0] < nums[mid]:  # 左侧升序，说明变换点在右侧
                l = mid + 1
            else: # 左侧存在变化点
                r = mid - 1
            
            

if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    so = Solution()
    print(so.findMin(nums))