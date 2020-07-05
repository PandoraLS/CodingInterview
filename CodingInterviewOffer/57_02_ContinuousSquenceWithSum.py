# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/9 11:38

# 链接：https://www.nowcoder.com/questionTerminal/c451a3fd84b64cb19485dad758a55ebe
# 来源：牛客网

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        l, r, sum, res = 1, 2, 3, []
        while l < (1 + tsum) // 2:
            if sum > tsum:
                sum -= l
                l += 1
            else:
                if sum == tsum:
                    res.append([i for i in range(l, r + 1)])
                r += 1
                sum += r
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.FindContinuousSequence(15))
