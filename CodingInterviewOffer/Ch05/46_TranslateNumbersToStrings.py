# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/5 16:02

# leetcode题目：https://leetcode.com/problems/decode-ways/
# leetcode题解：https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming
"""
A->1,B->2,...,Z->26
dp[i]为解析字符串s[1:i+1]的方法
dp[i]由dp[i-1]与dp[i-2]决定的
"""


class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        dp = [0 for x in range(len(s) + 1)]
        # base case initialization
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1  # (1) 处理从'0'开始的s。替代方法:我建议将其作为错误条件处理，并立即返回0。
        # 它更容易跟踪，而且是一种优化。
        for i in range(2, len(s) + 1):
            # One step jump
            if 0 < int(s[i - 1:i]) <= 9:  # (2) 
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i - 2:i]) <= 26:  # (3)
                dp[i] += dp[i - 2]
        return dp[len(s)]


if __name__ == '__main__':
    import string
    letter_list = string.ascii_letters
    for i in range(26):
        print(str(i)+'-'+letter_list[i],end=' ')
    print()
    so = Solution()
    stri = '12258'
    print(so.numDecodings(stri))
