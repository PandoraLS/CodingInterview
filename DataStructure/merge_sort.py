# -*- coding: utf-8 -*-
# @Time : 2020/4/24 10:57

"""
参考算法第4版
https://algs4.cs.princeton.edu/22mergesort/Merge.java.html
"""
from typing import List
class Solution:
    def merge(self, a, aux, lo, mid, hi):
        inversions = 0
        for k in range(lo, hi + 1):
            aux[k] = a[k]
        i, j = lo, mid + 1
        for k in range(lo, hi + 1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                a[k] = aux[j]
                j += 1
            else:
                a[k] = aux[i]
                i += 1
        return inversions

    def mergeSort(self, a, aux, lo, hi):
        if hi <= lo:
            return 0
        mid = lo + (hi - lo) // 2
        self.mergeSort(a, aux, lo, mid)
        self.mergeSort(a, aux, mid+1, hi)
        self.merge(a, aux, lo, mid, hi)

if __name__ == '__main__':
    so = Solution()
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    aux =[0] * len(nums)
    so.mergeSort(nums, aux, 0, len(nums) - 1)
    print(nums)
