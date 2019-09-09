# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 19:56
# @Author  : Li Sen

def story(**kwds):
    return 'Once upon a time, there was a %(job)s called %(name)s.' % kwds

def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)

def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor

    

if __name__ == "__main__":
    print(story(job='king', name='Gumby'))
    print(story(name='Sir Robin', job='brave knight'))
    params = {'job':'language', 'name':'Python'}
    print(story(**params))
    del params['job']
    print(params)
    print(story(job='stroke of genius', **params))
    
    print("-------------------------------------")
    print(power(2,3))
    print(power(3,2))
    print(power(y=3,x=2))
    params2 = (5, )*2 # 元组(5,5)
    print(params2)
    print(power(*params2)) # 5^5=3125
    print(power(3,3,'hello'))
    print("-------------------------------------")
    print(interval(10))
    print(interval(1,5))
    print(interval(3,12,4))
    print(power(*interval(3,7))) # 输入四个参数: 3,4,5,6  实际只接收两个参数，3,4  后面的5,6是多余的，最终计算3^4=81

    print("-------------------------------------")
    x = 1
    scope = vars()
    print(scope['x'])
    scope['x'] += 1
    print(scope['x'])
    print("-------------------------------------")
    double = multiplier(2) # 根据multiplier的返回，double是一个函数，有输入的参数
    print(double(5)) # double的输入参数是number=5


    