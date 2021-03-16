# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/21 14:28

class Solution:
    def wordBreak(self, s: str, wordDict):
        wordDict = set(wordDict)
        cache = {}

        def dfs(s, begin):
            if begin == len(s):
                return [[]]
            if begin in cache:
                return cache[begin]
            sentences = []
            for e in range(begin + 1, len(s) + 1):
                if s[begin:e] in wordDict:
                    res = dfs(s, e)
                    for _ in res:
                        sentences.append([s[begin:e]] + _)
            cache[begin] = sentences
            return cache[begin]

        res = dfs(s, 0)
        return [''.join(_) for _ in res]


if __name__ == '__main__':
    so = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(so.wordBreak(s, wordDict))
