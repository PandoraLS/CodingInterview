# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/8 14:54

class Solution:
    def GetNumberSameAsIndex(self, numbers):
        if numbers == [] or len(numbers) <= 0:
            return -1
        left = 0
        right = len(numbers) - 1
        while left <= right:
            # middle = left + (right - left) // 2
            middle = left + (right - left) // 2
            if numbers[middle] == middle:
                return middle
            if numbers[middle] > middle:
                right = middle - 1
            else:
                left = middle + 1
        return -1


if __name__ == '__main__':
    so = Solution()
    numbers = [-3, -1, 1, 3, 5]
    print(so.GetNumberSameAsIndex(numbers))
