# -*- coding: utf-8 -*-
# @Time: 2019/9/9 23:09
# @Author: Li Sen

def factorial(n):
    '阶乘的递归计算'
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def power(x, n):
    '幂的递归计算'
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


def search(sequence, number, lower=0, upper=None):
    if upper is None: upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


if __name__ == "__main__":
    print(factorial(5))
    print(power(2, 3))
    seq = [34, 67, 8, 123, 4, 100, 95]
    seq.sort()
    print(seq)
    print(search(seq, 34))
    print(search(seq, 100))
