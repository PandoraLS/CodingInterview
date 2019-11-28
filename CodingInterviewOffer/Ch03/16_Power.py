# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 11:05
# @Author  : Li Sen
# https://oi-wiki.org/math/quick-pow/
# https://www.nowcoder.com/questionTerminal/1a834e5e3e1a4b7ba251417554e07c00?answerType=1&f=discussion
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0.0:
            return 0.0
        result = 1.0

        if exponent > 0:
            e = exponent
        else:
            e = -exponent

        for i in range(1, e + 1):
            result *= base

        if exponent > 0:
            return result
        else:
            return 1 / result

    def Power2(self, base, exponent):
        # 快速幂的递归方式
        flag = exponent < 0
        if flag:
            exponent = -exponent
        result = self.getPower(base, exponent)
        if flag:
            return 1 / result
        else:
            return result

    def getPower(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        ans = self.getPower(base, exponent // 2)
        ans *= ans
        if exponent & 1 == 1:
            ans *= base
        return ans

    def Power3(self, base, exponent):
        # 快速幂的递推写法
        flag = False
        if exponent < 0:
            flag = True
            exponent = -exponent
        ans = 1
        while (exponent > 0):
            if exponent & 1 == 1:  # 如果是奇数
                ans *= base
            exponent //= 2
            base *= base

        if flag:
            return 1 / ans
        else:
            return ans


if __name__ == '__main__':
    so = Solution()
    print(so.Power(2, 3))
    print(so.Power2(2, 3))
    print(so.Power3(2, 3))
