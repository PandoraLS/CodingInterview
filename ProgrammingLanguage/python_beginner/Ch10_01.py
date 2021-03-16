# -*- coding: utf-8 -*-
# @Time: 2019/9/24 21:24
# @Author: Li Sen

if __name__ == '__main__':
    a = set([1, 2, 3])
    b = set([2, 3, 4])
    print(a.union(b))
    print(a | b)

    mySets = []
    for i in range(10):
        mySets.append(set(range(i, i + 5)))

    
