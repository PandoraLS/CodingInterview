# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 11:02
# @Author  : sen

# 快速幂: https://oi-wiki.org/math/quick-pow/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag = False
        if n < 0:
            n = -n
            flag = True

        def binpow(x, n):
            """
            快速幂：递归实现
            :param x: 底数
            :param n: 幂指数
            :return:
            """
            if n == 0:
                return 1
            if n == 1:
                return x
            res = binpow(x, n // 2)
            if n & 1:
                return res * res * x
            else:
                return res * res

        p = binpow(x, n)
        return 1/p if flag else p

    def myPow_iter(self, x: float, n: int) -> float:
        flag = False
        if n < 0:
            n = -n
            flag = True

        def binpow_iter(x, n):
            """
            快速幂: 迭代实现
            :param x: 底数
            :param n: 幂指数
            :return:
            """
            if n == 0:
                return 1
            if n == 1:
                return x
            res = 1
            while n > 0:
                if n & 1:
                    res = res * x
                x = x * x
                n >>= 1
            return res

        p = binpow_iter(x, n)
        return 1/p if flag else p


if __name__ == '__main__':
    so = Solution()
    print(so.myPow(2, 3))
    print(so.myPow_iter(2, 3))