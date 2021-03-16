# -*- coding: utf-8 -*-
# @Time: 2019/9/9 23:09
# @Author: Li Sen

from functools import reduce # 在Python 3里，reduce() 函数已经被从全局名字空间里移除了，它现在被放置在fucntools 模块里
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

def func(x):
    return x.isalnum() # 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False


if __name__ == "__main__":
    print(factorial(5))
    print(power(2, 3))
    seq = [34, 67, 8, 123, 4, 100, 95]
    seq.sort()
    print(seq)
    print(search(seq, 34))
    print(search(seq, 100))
    print('----------------------------------------')
    result = map(str, range(10))
    print(list(result))
    seq = ["foo", "x41", "?!", "***"]
    result2 = filter(func, seq)
    print(list(result2))
    print(list([x for x in seq if x.isalnum()])) # 列表推导式子
    result3 = filter(lambda x:x.isalnum(), seq)
    print(list(result3))
    print('----------------------------------------')
    numbers = [1,2,3,4,5]
    print(reduce(lambda x, y:x+y,numbers))
