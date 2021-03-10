# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/9 10:59


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        ls = []
        if not isinstance(array, list):
            return ls
        for i, v in enumerate(array):
            for v1 in array[i:]:
                if (v + v1) == tsum:
                    ls.append([v, v1])
        if ls:
            return ls[0]
        else:
            return ls


if __name__ == '__main__':
    so = Solution()
    array = [1, 2, 4, 7, 11, 15]
    print(so.FindNumbersWithSum(array, 15))
