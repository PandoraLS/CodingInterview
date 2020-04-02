# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/27 19:45

def sqrt(n):
    x0, x1 = 1, 0
    while True:
        x1 = 0.5 * (x0 + n / x0)
        if abs(x1 - x0) < 1e-6:
            break
        x0 = x1
        print(x0)
    return x1

if __name__ == '__main__':
    sqrt(2)
        