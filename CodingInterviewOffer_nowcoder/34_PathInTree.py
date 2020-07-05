# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 16:05
# @Author  : Li Sen

"""
// 面试题34：二叉树中和为某一值的路径
// 题目：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所
// 有路径。从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
参考：https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root, sum, ls, res):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        if root.left: # 如果左子树存在
            self.dfs(root.left, sum - root.val, ls + [root.val], res)
        if root.right:
            self.dfs(root.right, sum - root.val, ls + [root.val], res)

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
    root = createNodes()
    so = Solution()
    print(so.pathSum(root, 22))
