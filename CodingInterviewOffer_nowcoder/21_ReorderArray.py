# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 18:48
# @Author  : Li Sen

# class Solution:
class Solution:
    def reOrderArray(self, array):
        # write code here
        oddl = list(filter(lambda x: x % 2, array))
        evenl = list(filter(lambda x: not x % 2, array))
        array = oddl + evenl
        return array

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7]
    so = Solution()
    print(so.reOrderArray(array))
