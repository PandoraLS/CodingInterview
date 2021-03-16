# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 14:28
# @Author  : sen


# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
思路：典型的二叉树搜索方案，回溯法，先序遍历+路径记录
"""

import copy
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []
        def dfs(root, tar):
            if not root:
                return None
            path.append(root.val)
            tar -= root.val
            if tar == 0 and root.left is None and root.right is None:
                tmp_path = copy.copy(path)
                res.append(tmp_path) # 如果这里直接append(path),后面path改变的时候append进去的path也会随之改变
            dfs(root.left, tar)
            dfs(root.right, tar)
            path.pop()

        dfs(root, sum)
        return res

def createNodes():
    """
    //            10
    //          /    \
    //         5      12
    //        /\
    //       4  7
    :return:
    """
    p10 = TreeNode(10)
    p5 = TreeNode(5)
    p12 = TreeNode(12)
    p4 = TreeNode(4)
    p7 = TreeNode(7)
    p10.left = p5
    p10.right = p12
    p5.left = p4
    p5.right = p7

    root = p10
    return root

if __name__ == '__main__':
    so = Solution()
    root = createNodes()
    print(so.pathSum(root, 22))