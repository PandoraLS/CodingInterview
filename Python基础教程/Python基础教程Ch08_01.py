# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 21:13
# @Author  : Li Sen

class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Division by zero is illegal")
            else:
                raise


def describePerson(person):
    print('Description of ', person['name'])
    print('Age: ', person['age'])
    try:
        print('Occupation: ', person['occupation'])
    except KeyError:
        pass


if __name__ == "__main__":
    print("Python基础教程Ch08")
    print("-----------------------------------------")

    person1 = {'name': "lalala", 'age': 42}
    person2 = {'name': 'dududu', 'age': 24, 'occupation': 'camper'}
    describePerson(person1)
    describePerson(person2)

    # while True:
    #     try:
    #         x = input('Enter the first number: ')
    #         y = input('Enter the second number: ')
    #         value = int(x) / int(y)
    #         print(value)
    #     except :
    #         print('invalid input. try again!')
    #     else:
    #         break

    # x = None
    # try:
    #     x = 1/0
    # finally:
    #     print("cleaning up...")
    #     del x

    # print("-----------------------------------------")
    # caculator = MuffledCalculator()
    # print(caculator.calc('10/2'))
    # # print(caculator.calc('10/0'))
    # caculator.muffled = True
    # print(caculator.calc('10/0'))

    # try:
    #     1 / 0
    # except NameError:
    #     print("unknow variable")
    # else:
    #     print("that went well")
    # finally:
    #     print("cleaning up...")
