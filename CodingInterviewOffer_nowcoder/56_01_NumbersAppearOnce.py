# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/8 17:06

class Solution:
    def FindNumsAppearOnce(self, array):
        return list(self.dc(array, 0, len(array) - 1))

    def dc(self, array, start, end):
        res = set()
        if start > end:
            return res
        if start == end:
            # temp = array[start:end + 1]
            return set(array[start:end + 1])

        spl = (start + end) // 2
        s1 = self.dc(array, start, spl)
        s2 = self.dc(array, spl + 1, end)
        # ss = s1.union(s2).difference(s1.intersection(s2))
        return s1.union(s2).difference(s1.intersection(s2))  # s1,s2的并集 -  s1,s2的交集

    def FindNumsAppearOnce2(self, array):
        # write code here
        from collections import Counter
        res = Counter(array).most_common()[-2:]
        return list(map(lambda x: x[0], res))


if __name__ == '__main__':
    so = Solution()
    array = [2, 4, 3, 6, 3, 2, 5, 5]
    print(so.FindNumsAppearOnce(array))
    print(so.FindNumsAppearOnce2(array))
