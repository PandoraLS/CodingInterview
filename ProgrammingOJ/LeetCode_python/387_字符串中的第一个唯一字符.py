# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/23 11:46

class Solution:
    def firstUniqChar(self, s: str) -> int:

        import collections
        cont = collections.Counter(s)
        for k in cont:
            if cont[k] == 1:
                return s.find(k)
        return -1


if __name__ == '__main__':
    so = Solution()
    s = "loveleetcode"
    print(so.firstUniqChar(s))
