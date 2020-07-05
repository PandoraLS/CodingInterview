# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/2 19:24

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        from collections import Counter
        count = Counter(numbers).most_common()
        if count[0][1] > len(numbers) / 2.0:
            return count[0][0]
        return 0

    def MoreThanHalfNum_Solution2(self, numbers):
        # 利用中位数
        numbers.sort()
        theone = numbers[len(numbers) // 2]
        if numbers.count(theone) > len(numbers) // 2:
            return theone
        return 0


if __name__ == '__main__':
    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    so = Solution()
    print(so.MoreThanHalfNum_Solution(numbers))
    print(so.MoreThanHalfNum_Solution2(numbers))
