# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 20:09
# @Author  : Li Sen

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return None
        if root.left == None and root.right == None:
            return None

        pTemp = root.left
        root.left = root.right
        root.right = pTemp

        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
