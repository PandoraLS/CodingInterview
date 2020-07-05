# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 19:56
# @Author  : Li Sen


# Python的int没有长度限制
def print_n(n: int): # 确定n是int型的
    n = 10 ** (n) # 确定位数
    for i in range(1, n):
        print(i)
        
if __name__ == '__main__':
    print_n(3)

