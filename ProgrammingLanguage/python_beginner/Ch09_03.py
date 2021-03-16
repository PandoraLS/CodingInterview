# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 13:32
# @Author  : Li Sen

def flatten(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new


if __name__ == '__main__':
    # nested = [[1, 2], [3, 4], [5]]
    # nested2 = [[[1], 2], 3, 4, [5, [6, 7]], 8]
    # nested3 = ['foo', ['bar', ['baz']]]
    # for num in flatten(nested):
    #     print(num, end=" ")
    # print()
    # for num in flatten(nested2):
    #     print(num, end=" ")
    # print()
    # for string in flatten(nested3):
    #     print(string, end=" ")
    
    r = repeater(42)
    print(r.__next__())
    r.send("hello,world")
    print(r.__next__())