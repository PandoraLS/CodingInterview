# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/8 14:27

class Solution:
    def GetMissingNumber(self, numbers):
        if numbers == [] or len(numbers) <= 0:
            return -1
        left = 0
        right = len(numbers) - 1
        while (left <= right):
            middle = (left + right) // 2
            if numbers[middle] != middle:
                if middle == 0 or numbers[middle - 1] == middle - 1:
                    return middle
                right = middle - 1
            else:
                left = middle + 1

        if left == len(numbers):
            return len(numbers)

        # 无效输入，返回-1
        return -1


if __name__ == '__main__':
    so = Solution()
    numbers = [0, 1, 2, 4, 5]
    print(so.GetMissingNumber(numbers))
