# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/6 10:54

class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0 # 当前不含重复字符字串的起点
        maxLength = 0
        usedChar = {}
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]: # 如果s[i]之前出现过且当前s[i]出现的位置在当前不重复子串起点后，那么把start从上个s[i]的位置后移一个
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i # usedChar中字符最后一次出现的位置
        return maxLength


if __name__ == '__main__':
    so = Solution()
    ss = "arabcacfr"
    print(so.lengthOfLongestSubstring(ss))
