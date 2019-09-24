# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 10:33
# @Author  : Li Sen


def checkIndex(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        checkIndex(key)

        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value


class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)


if __name__ == '__main__':
    # print("成员访问-------------------------")
    # s = ArithmeticSequence(1, 2)
    # print(s[4])
    # s[4] = 2
    # print(s[4])
    # print(s[5])
    # print("访问计数-------------------------")
    # c1 = CounterList(range(10))
    # print(c1)
    # c1.reverse()
    # print(c1)
    # del c1[3:6]
    # print(c1)
    # print(c1.counter)
    # print(c1[4]+c1[2])
    # print(c1.counter)
    print("property-------------------------")
    r = Rectangle()
    r.width = 10
    r.height = 5
    print(r.size)
    r.size = 150, 100
    print(r.width)
