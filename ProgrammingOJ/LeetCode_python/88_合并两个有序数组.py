# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/19 16:44

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        dest = m + n - 1
        p1, p2 = m - 1, n - 1  # 定义两个指针分别指向nums1,nums2最后一个

        while p1 >= 0 or p2 >= 0:
            if p1 < 0:
                nums1[dest] = nums2[p2]
                dest -= 1
                p2 -= 1
                continue
            if p2 < 0:
                nums1[dest] = nums1[p1]
                dest -= 1
                p1 -= 1
                continue
            if nums1[p1] > nums2[p2]:
                nums1[dest] = nums1[p1]
                dest -= 1
                p1 -= 1
            else:
                nums1[dest] = nums2[p2]
                dest -= 1
                p2 -= 1

        print(nums1, nums2)


if __name__ == '__main__':
    a = [2, 0]
    b = [1]
    so = Solution()
    so.merge(a, 1, b, 1)
