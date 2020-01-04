# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/4 16:51

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # 题解：https://www.nowcoder.com/questionTerminal/bd7f978302044eee894445e244c7eee6?toCommentId=1247407
        if n <= 0:
            return 0
        count = 0
        i = 1
        while (i <= n):
            diviver = i * 10
            count += (n // diviver) * i + min(max(n % diviver - i + 1, 0), i)
            i *= 10
        return count


if __name__ == '__main__':
    n = 12
    so = Solution()
    print(so.NumberOf1Between1AndN_Solution(n))
