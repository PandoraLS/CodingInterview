# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 21:13
# @Author  : Li Sen

class MuffledCalculator:
    muffled = False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Division by zero is illegal")
            else:
                raise 


if __name__ == "__main__":
    print("Python基础教程Ch08")
    print("-----------------------------------------")
    while True:
        try:
            x = input('Enter the first number: ')
            y = input('Enter the second number: ')
            value = int(x) / int(y)
            print(value)
        except :
            print('invalid input. try again!')
        else:
            break

    # print("-----------------------------------------")
    # caculator = MuffledCalculator()
    # print(caculator.calc('10/2'))
    # # print(caculator.calc('10/0'))
    # caculator.muffled = True
    # print(caculator.calc('10/0'))
    
    
    