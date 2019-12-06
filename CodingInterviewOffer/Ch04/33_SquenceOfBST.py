# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 14:41
# @Author  : Li Sen

"""
// 面试题33：二叉搜索树的后序遍历序列
// 题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
// 如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。
python:后序遍历 的序列中，最后一个数字是树的根节点 ，数组中前面的数字可以分为两部分：
第一部分是左子树节点 的值，都比根节点的值小；
第二部分 是右子树 节点的值，都比 根 节点 的值大，后面用递归分别判断前后两部分 是否 符合以上原则
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == None or len(sequence) == 0:
            return False
        length = len(sequence)
        root = sequence[length - 1]
        # 二叉树中左子树节点小于根节点
        for i in range(length):
            if sequence[i] > root:
                break
        # 二叉树中右子树节点大于根节点
        for j in range(i, length):
            if sequence[j] < root:
                return False
        # 判断左子树是否是二叉树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])

        # 判断右子树是否是二叉树
        right = True
        if i < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right
