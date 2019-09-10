# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 15:36
# @Author  : Li Sen

__metaclass__ = type # 确定使用新类

class Person:
    def setName(self, name):
        self.name = name
    def getName(self):    
        return self.name
    def greet(self):
        print("hello, world! I'm %s."%self.name)
        
class Class:
    def method(self):
        print('I have a self')
        
def function():
    print("I'dont...")

class Bird:
    song = 'Squaawk'
    def sing(self):
        print(self.song)

class Secretive:
    def __inaccess(self):
        print('bet you cannot see me...')
    
    def accessible(self):
        print('the secret message is:')
        self.__inaccess()

class C:
    '类在定义的时候本身就是执行代码块'
    print("Class C being defined...")
    
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1

class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print("Hi, my value is ", self.value)

class TalkingCalculator(Calculator, Talker):
    pass

if __name__ == "__main__":
    print('-------------------------')
    # foo = Person()
    # bar = Person()
    # foo.setName('Luke')
    # bar.setName('Anak')
    # foo.greet()
    # bar.greet()
    # print(foo.name)
    # bar.name = "Yoda"
    # bar.greet()
    # print('-------------------------')
    # instance = Class()
    # instance.method()
    # instance.method = function
    # instance.method()
    # print('-------------------------')
    # bird = Bird()
    # bird.sing()
    # birdsong = bird.sing
    # birdsong()
    # print('-------------------------')
    # s = Secretive()
    # # s.__inaccessible()
    # s.accessible()
    # # s._Secretive__inaccessible()
    print("7.2.4-----------------------")
    m1 = MemberCounter()
    m1.init()
    print(MemberCounter.members)
    
    m2 = MemberCounter()
    m2.init()
    print(MemberCounter.members)
    print(m1.members)
    print(m2.members)
    
    m1.members = 'Two'
    print(m1.members)
    print(m2.members)

    print("7.2.5-----------------------")
    f = Filter()
    f.init()
    print(f.filter([1,2,3]))
    s = SPAMFilter()
    s.init()
    print(s.filter(['SPAM', 'SPAm', 'SPAM', 'eggs', 'SPAM']))

    print("7.2.6-----------------------")
    print(issubclass(SPAMFilter, Filter))
    print(issubclass(Filter, SPAMFilter))
    print(SPAMFilter.__bases__)
    print(Filter.__bases__)
    s = SPAMFilter()
    print(isinstance(s, SPAMFilter))
    print(isinstance(s, Filter))
    print(isinstance(s, str))
    print(s.__class__)

    print("7.2.7-----------------------")
    tc = TalkingCalculator()
    tc.calculate('1+2*3')
    tc.talk()

    print("7.2.8-----------------------")
    print(hasattr(tc, 'talk'))
    print(hasattr(tc, 'fnord'))
    print(callable(getattr(tc, 'talk', None))) # callable在python3.0中已经不再使用，不知这里为何可以继续使用
    print(callable(getattr(tc, 'fnord', None)))
    
    
    
