# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 18:41
# @Author  : Li Sen

class Solution:
    def cutRope(self, number):
        # write code here
        # 动态规划
        if (number < 2):
            return 0
        if (number == 2):
            return 1
        if (number == 3):
            return 2

        products = [0] * (number + 1)
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3

        max = 0
        for i in range(4, number + 1):
            max = 0
            for j in range(1, i // 2 + 1):
                product = products[j] * products[i - j]
                if (max < product):
                    max = product
                products[i] = max

        max = products[number]
        return max

    def cutRope2(self, number):
        # 贪心算法
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2

        timesOf3 = number // 3
        if number - timesOf3 * 3 == 1:
            timesOf3 -= 1
        timesOf2 = (number - timesOf3 * 3) // 2
        return int(pow(3, timesOf3)) * int(pow(2, timesOf2))


if __name__ == '__main__':
    length = 8
    so = Solution()
    print(so.cutRope(length))
    print(so.cutRope2(length))
