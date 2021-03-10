# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/9 19:48

class Solution:
    def ReverseSentence(self, s):
        # write code here
        l = s.split(' ')
        return ' '.join(l[::-1])
