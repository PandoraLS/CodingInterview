# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 17:51
# @Author  : Li Sen

import math

"""
A simple math module.
"""

__revision__ = 0.1


def square(x):
    '''
    Squares a number and returns the result.
    :param x: input x
    :return: result
    >>> square(2)
    4
    >>> square(3)
    9

    '''
    return x ** x


def product(factory1, factory2):
    'The product of two numbers'
    return factory1 * factory1
