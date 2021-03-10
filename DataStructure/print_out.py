# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/4/1 20:11

def print_out(N):
    if N >= 10:
        print_out(N // 10)
    print( N % 10)
    
if __name__ == '__main__':
    print_out(10000)