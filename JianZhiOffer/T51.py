# -*- coding: utf-8 -*-
# @Time : 2020/4/24 10:57
from typing import List

class Solution:
    def merge(self, a, aux, lo, mid, hi):
        inversions = 0
        for k in range(lo, hi + 1):
            aux[k] = a[k]
        i, j = lo, mid + 1
        for k in range(lo, hi+1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:  # a[k]首先赋值的是较小的那个值
                a[k] = a[j]
                j += 1
                inversions += mid - i + 1
            else:
                a[k] = a[i]
                i += 1
        return inversions

    def count(self, a, aux, lo, hi):
        inversions = 0
        if hi <= lo:
            return 0
        mid = lo + (hi - lo) // 2
        inversions += self.count(a, aux, lo, mid)
        inversions += self.count(a, aux, mid + 1, hi)
        inversions += self.merge(a, aux, lo, mid, hi)
        return inversions



    def reversePairs(self, nums):
        aux = [0] * len(nums)
        return self.count(nums, aux, 0, len(nums) - 1)


if __name__ == '__main__':
    so = Solution()
    nums = [7, 5, 6, 4]
    print(so.reversePairs(nums))