# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/6 15:30

# 链接：https://www.nowcoder.com/questionTerminal/96bd6684e04a44eb80e6a68efc0ec6c5
# 来源：牛客网
# TODO 这题还没看原理
class Solution:
    def InversePairs(self, data):
        # 发现可以用归并排序，归并拼接后用计算排序时元素的index变动了多少
        # 两个有序序列，每个元素移动index数（严格来说不是移动，这里不知怎么表达）之和好像刚好等于逆序对的个数
        # 我也不知为什么，找了半天发现了这个规律
        _, s = self.MergeSort(data)
        return s % 1000000007

    def MergeSort(self, data):
        n = len(data)
        # 递归基
        if n == 1: return data, 0
        # 分两半来排序
        part1, part2 = data[:n // 2], data[n // 2:]
        sorted_part1, s1 = self.MergeSort(part1)
        sorted_part2, s2 = self.MergeSort(part2)
        # 排序后拼接这两半，拼接后先计数，然后将两个有序序列合并
        s, sorted_temp = 0, sorted_part1 + sorted_part2
        # 用p、q两个指针指向两段，计算q中每个元素离插入点的index差
        p, q, len1, len_all = 0, sorted_temp.index(sorted_part2[0]), len(sorted_part1), len(sorted_temp)
        while p < len1 and q < len_all:
            # 移动p使p成为插入排序的插入点，计算要移动多少个位置
            while p < len1:
                if sorted_temp[q] < sorted_temp[p]:
                    s += len1 - p
                    break
                p += 1
            q += 1
        # 完成排序，并把排序后的内容回溯给上一级做准备
        l = []
        p, q = 0, sorted_temp.index(sorted_part2[0])
        while p < len1 and q < len_all:
            if sorted_temp[p] < sorted_temp[q]:
                l.append(sorted_temp[p])
                p += 1
            else:
                l.append(sorted_temp[q])
                q += 1
        if p == len1: l += sorted_temp[q:]
        if q == len_all: l += sorted_part1[p:]
        return l, s + s1 + s2


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 0]
    so = Solution()
    print(so.InversePairs(data))
