# -*- coding: utf-8 -*-
# @Time: 2019/9/14 11:12
# @Author: Li Sen

'''
拓展：不修改数组找出重复的数字。
在一个长度为n+1的数组里的所有数字都在1~n的范围内，所以数组中至少有一个数字是重复的。请找出数组中任意一个重复的数字，
但不能修改输入的数组，例如输入长度为8的数组[2,3,5,4,3,2,6,7]，那么对应的输出是重复的数字为2或3。
'''


# 方法一：利用哈希表，时间复杂度O(n)，空间复杂度O(n)
# 方法二：二分查找的变形，如下，时间复杂度O(nlogn)，空间复杂度为O(1)

class Solution:
    def duplicate1(self, numbers):
        '方法一：利用哈希表，时间复杂度O(n)，空间复杂度O(n)'
        if not numbers or len(numbers) <= 0:
            return -1
        usedDic = set()
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
                return -1
            if numbers[i] not in usedDic:
                usedDic.add(numbers[i])
            else:
                return numbers[i]
        return -1

    def duplicate2(self, numbers):
        '方法二：二分查找的变形，如下，时间复杂度O(nlogn)，空间复杂度为O(1)'
        if not numbers or len(numbers) <= 0:
            return -1
        start =1 

        return -1

    def countRange(self, numbers, length, start, end):
        '''
        计算数组中的元素大于等于start，小于等于end的元素个数
        统计start（含）到end（含）之间的元素个数
        :param numbers:
        :param length:
        :param start:
        :param end:
        :return:
        '''
        

        return count


if __name__ == '__main__':
    Array = [2, 3, 1, 0, 2, 5, 3]

    print(Solution().duplicate1(Array))
    print(Solution().duplicate2(Array))
