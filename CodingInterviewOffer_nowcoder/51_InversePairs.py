# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/6 15:30

# 来源：牛客网
count = 0
class Solution:
    def InversePairs(self, data):
        global count
        def MergeSort(lists):
            global count
            if len(lists) <= 1:
                return lists
            num = int( len(lists)/2 )
            left = MergeSort(lists[:num])
            right = MergeSort(lists[num:])
            r, l=0, 0
            result=[]
            while l<len(left) and r<len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left)-l # 剩余的左边的数都大于右边的那个数 所以加len(left)-l
            result += left[l:]
            result += right[r:]
            return result
        MergeSort(data)
        return count%1000000007


if __name__ == '__main__':
    data = [7, 5, 6, 4]
    so = Solution()
    print(so.InversePairs(data))
