# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/29 18:20
class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        L, R, ans = [0] * length, [0] * length, [0] * length
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
            print('i', i, ':L[i]', L[i])
        R[length - 1] = 1
        for i in range(length - 2, -1, -1):
            R[i] = nums[i + 1] * R[i + 1]
            print('i', i, ':R[i]', R[i])

        for i in range(length):
            ans[i] = L[i] * R[i]
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    so = Solution()
    print(so.productExceptSelf(nums))
