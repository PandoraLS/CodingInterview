# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/10 18:51

class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        new_list = [i for i in numbers if i > 0]
        new_list.sort()

        n = 0
        for j in range(len(new_list) - 1):
            if (new_list[j + 1] - new_list[j]) > 0:  # 如果后面一个均大于前面一个(连续的)
                n += (new_list[j + 1] - new_list[j])
            else:  # 如果排序后出现了重复的(出现了对子)
                return False

        if n <= 4:  # 因为最多只有4个王
            return True
        else:
            return False
