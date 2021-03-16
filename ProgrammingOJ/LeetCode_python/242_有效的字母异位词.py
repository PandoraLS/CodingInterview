# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/23 11:01

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        s_cnt = Counter(s_list)
        t_cnt = Counter(t_list)
        if sorted(list(s_cnt.items())) == sorted(list(t_cnt.items())):
            return True
        return False


if __name__ == '__main__':
    s = "aa"
    t = "a"
    so = Solution()
    print(so.isAnagram(s, t))
