# -*- coding: utf-8 -*-
from typing import List
from itertools import permutations
"""
思路：全排列(需要会默写)+剪枝条件(不重复排列)
在python函数库中也有这种排列
"""


class Solution:

    def permutation(self, s: str) -> List[str]:
        s_list = list(s)
        res = []
        def dfs(pos):
            if pos == len(s_list) - 1:
                res.append(''.join(s_list))
            fixed = set()
            for i in range(pos, len(s_list)):
                if s_list[i] in fixed:  # 每种字符在pos只会被固定一次，对重复方案进行剪枝
                    continue
                fixed.add(s_list[i])
                s_list[i], s_list[pos] = s_list[pos], s_list[i]
                dfs(pos+1)
                s_list[i], s_list[pos] = s_list[pos], s_list[i] # 回溯
        dfs(0)
        return res

    def permutation2(self, s: str):
        # 单纯的全排列
        s_list = list(s)
        res = []
        def dfs(pos):
            if pos == len(s_list) - 1:
                res.append(''.join(s_list))
            for i in range(pos, len(s_list)):
                s_list[i], s_list[pos] = s_list[pos], s_list[i]
                dfs(pos + 1)
                s_list[i], s_list[pos] = s_list[pos], s_list[i]
        dfs(0)
        return res


if __name__ == '__main__':
    so = Solution()
    s = 'abcdef'
    # s = 'abb'
    res = so.permutation(s)
    print(len(s), len(res)) # 阶乘是指数复杂度
    # print(so.permutation2(s))