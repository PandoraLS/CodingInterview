# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/9 10:33

# -*- coding:utf-8 -*-
class Solution:
    def FindNumsAppearingOnce(self, array):
        # write code here
        from collections import Counter
        res = Counter(array).most_common()[-1:]
        return list(map(lambda x: x[0], res))


if __name__ == '__main__':
    so = Solution()
    array = [4, 3, 3, 2, 2, 2, 3]
    print(so.FindNumsAppearingOnce(array))
