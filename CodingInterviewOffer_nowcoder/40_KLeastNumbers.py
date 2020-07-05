# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/2 21:24

# 题解参考：https://www.nowcoder.com/questionTerminal/6a296eb82cf844ca8539b57c23e6e9bf?f=discussion
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # 蒂姆排序
        if tinput == [] or k > len(tinput):
            return []
        tinput.sort()
        return tinput[:k]

    def GetLeastNumbers_Solution2(self, tinput, k):
        # 快速排序
        def quick_sort(lst):
            if not lst:
                return []
            pivot = lst[0]
            left = quick_sort([x for x in lst[1:] if x < pivot])
            right = quick_sort([x for x in lst[1:] if x >= pivot])
            return left + [pivot] + right

        if tinput == [] or k > len(tinput):
            return []
        tinput = quick_sort(tinput)
        return tinput[:k]

    def GetLeastNumbers_Solution3(self, tinput, k):
        # 归并排序
        def merge_sort(lst):
            if len(lst) <= 1:
                return lst
            mid = len(lst) // 2
            left = merge_sort(lst[:mid])
            right = merge_sort(lst[mid:])
            return merge(left, right)

        def merge(left, right):
            l, r, res = 0, 0, []
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            res += left[l:]
            res += right[r:]
            return res

        if tinput == [] or k > len(tinput):
            return []
        tinput = merge_sort(tinput)
        return tinput[:k]
    

if __name__ == '__main__':
    array = [4, 5, 1, 6, 2, 7, 3, 8]
    so = Solution()
    print(so.GetLeastNumbers_Solution(array, 4))
    print(so.GetLeastNumbers_Solution2(array, 4))
    print(so.GetLeastNumbers_Solution3(array, 4))
