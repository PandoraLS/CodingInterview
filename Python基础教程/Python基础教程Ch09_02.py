# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 12:58
# @Author  : Li Sen

class MyClass:

    @staticmethod
    def smeth():
        print('this is a static method')

    @classmethod
    def cmeth(cls):
        print('this is a class method of', cls)


class Rectangle:
    def __init__(self):
        self.width = 0
        self.heigth = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.heigth = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.heigth
        else:
            raise AttributeError


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value

    def __iter__(self):
        return self


if __name__ == '__main__':
    # MyClass.smeth()
    # MyClass.cmeth()
    fibs = Fibs()
    # for f in fibs:
    #     if f > 1000:
    #         print(f)
    #         break
    
    ti = TestIterator()
    print(list(ti))
    