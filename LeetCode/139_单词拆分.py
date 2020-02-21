# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/20 20:58
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
"""
from functools import lru_cache


class Solution:
    # 深度优先搜索
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)

        @lru_cache(None)  # lru_cache对于参数相同的结果会直接保存，不会重新计算
        def dfs(rest):
            if not rest:
                return True
            for i in range(1, len(rest) + 1):
                if rest[:i] in wordDict:
                    res = dfs(rest[i:])
                    if res:
                        return True
            return False

        return dfs(s)


class Solution2:
    # 记忆化搜索
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [0 for i in range(len(s))]  # 0未访问，1不可拆分，2可拆分
        wordDict = set(wordDict)

        def dfs(s, begin):
            if begin == len(s):
                return True
            if dp[begin] != 0:
                return dp[begin] == 2
            for l in range(1, len(s) - begin + 1):
                if s[begin:begin + l] in wordDict:
                    if dfs(s, begin + l):
                        dp[begin] = 2
                        return True
            dp[begin] = 1
            return False

        return dfs(s, 0)


class Solution3:
    # 深度优先搜索+动态规划
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]


if __name__ == '__main__':
    so = Solution()
    so2 = Solution2()
    s = "leetcode"
    wordDict = ["leet", "code"]
    s1 = "applepenapple"
    wordDict1 = ["apple", "pen"]
    s2 = "catsandog"
    wordDict2 = ["cats", "dog", "sand", "and", "cat"]
    # print(so.wordBreak(s, wordDict))
    # print(so.wordBreak(s1, wordDict1))
    # print(so.wordBreak(s2, wordDict2))
    print("---------------------------")
    print(so2.wordBreak(s, wordDict))
    print(so2.wordBreak(s1, wordDict1))
    print(so2.wordBreak(s2, wordDict2))
