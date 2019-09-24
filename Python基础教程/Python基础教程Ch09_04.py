# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 14:40
# @Author  : Li Sen
# 八皇后问题
import random


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


if __name__ == '__main__':
    print(list(queens(3)))
    print(list(queens(4)))
    # for solution in queens(8):
    #     print(solution)
    print(len(list(queens(8))))
    prettyprint(random.choice(list(queens(8))))
