from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bisect_left(arr, x, lo=0, hi=None):
            if lo < 0:
                raise ValueError('lo must be non-negative')
            if hi is None:
                hi = len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        length = len(nums)
        if length == 0:
            return 0
        i = bisect_left(nums, target, 0, length)
        res = 0
        if i != length and nums[i] == target:
            while i != length and nums[i] == target:
                i += 1
                res += 1
            return res
        else:  # nums中没有target
            return 0



if __name__ == '__main__':
    so = Solution()
    nums = [1]
    target = 1
    print(so.search(nums, target))