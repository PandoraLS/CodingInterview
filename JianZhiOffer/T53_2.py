from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        left = 0
        right = length - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid == nums[mid]: # 此时[left,mid]一定无缺失值
                # 下一轮搜索空间[mid+1,right]
                left = mid + 1
            else:
                right = mid
        print(left)
        return nums[left]+1 if nums[left] == left else nums[left]-1

if __name__ == '__main__':
    nums = [0,1,2,3,4,6,7,8, 9]
    so = Solution()
    so.missingNumber(nums)