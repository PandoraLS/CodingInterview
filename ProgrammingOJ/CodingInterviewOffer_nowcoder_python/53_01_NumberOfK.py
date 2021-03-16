# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/8 13:31

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)

    def GetNumberOfK2(self, data, k):
        number = 0
        if data != [] and len(data) > 0:
            if k < data[0] or k > data[-1]: # 如果数组中根本没有k，直接返回0
                return 0
            length = len(data)
            first = self.GetFirstK(data, length, k, 0, length - 1)
            last = self.GetLastK(data, length, k, 0, length)
            if first > -1 and last > -1:
                number = last - first + 1
        return number

    def GetFirstK(self, data, length, k, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if data[middle] == k:
            if (middle > 0 and data[middle - 1] != k) or middle == 0:
                return middle
            else:
                end = middle - 1
        elif data[middle] > k:
            end = middle - 1
        else:
            start = middle + 1

        return self.GetFirstK(data, length, k, start, end)

    def GetLastK(self, data, length, k, start, end):
        if start > end:
            return -1

        middle = (start + end) // 2
        if data[middle] == k:
            if (middle < length - 1 and data[middle + 1] != k) or middle == length - 1:
                return middle
            else:
                start = middle + 1
        elif data[middle] < k:
            start = middle + 1
        else:
            end = middle - 1

        return self.GetLastK(data, length, k, start, end)


if __name__ == '__main__':
    data = [1, 2, 3, 3, 3, 3, 4, 5]
    so = Solution()
    print(so.GetNumberOfK(data, 3))
    print(so.GetNumberOfK2(data, 3))

    data2 = [1, 3, 3, 3, 3, 4, 5]
    k2 = 6
    print(so.GetNumberOfK2(data2, k2))
