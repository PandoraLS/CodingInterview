# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/8 16:16

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        nLeft = self.TreeDepth(pRoot.left)
        nRight = self.TreeDepth(pRoot.right)

        if nLeft > nRight:
            return nLeft + 1
        else:
            return nRight + 1
