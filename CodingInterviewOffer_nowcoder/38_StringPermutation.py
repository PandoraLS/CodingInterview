# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/2 17:39

class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return list(ss)
        pStr = []
        charlist = list(ss)
        charlist.sort()

        for i in range(len(charlist)):
            if i > 0 and charlist[i] == charlist[i - 1]:
                continue
            left = ''.join(charlist[:i])
            right = ''.join(charlist[i+1:])
            lr = left + right
            temp = self.Permutation(''.join(charlist[:i]) + ''.join(charlist[i + 1:]))
            for j in temp:
                pStr.append(charlist[i] + j)
        return pStr

if __name__ == '__main__':
    s = "aab"
    so = Solution()
    print(so.Permutation(s))
    