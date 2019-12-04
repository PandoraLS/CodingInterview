# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 20:17
# @Author  : Li Sen

"""
// 面试题28：对称的二叉树
// 题目：请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和
// 它的镜像一样，那么它是对称的。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.isSymmetrical2(pRoot, pRoot)

    def isSymmetrical2(self, pRoot1, pRoot2):
        if pRoot1 == None and pRoot2 == None:
            return True
        if pRoot1 == None or pRoot2 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSymmetrical2(pRoot1.left, pRoot2.right) and self.isSymmetrical2(pRoot1.right, pRoot2.left)
