# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/1 12:51
class Solution:
    def increasingTriplet(self, nums) -> bool:
        if len(nums) < 3:
            return False
        n = len(nums)
        dp_min = [nums[0] for i in range(n)]
        dp_max = [nums[-1] for i in range(n)]
        for i in range(1, n):
            dp_min[i] = min(dp_min[i - 1], nums[i])
            print('i: ', i, 'dp_min[i]:', dp_min[i])
        for i in range(n - 2, -1, -1):
            dp_max[i] = max(dp_max[i + 1], nums[i])
            print('i: ', i, 'dp_max[i]:', dp_max[i])
        for i in range(n):
            if dp_min[i] < nums[i] < dp_max[i]:
                return True
        return False


if __name__ == '__main__':
    so = Solution()
    nums = [1, 2, 3, 4, 5]
    print(so.increasingTriplet(nums))
