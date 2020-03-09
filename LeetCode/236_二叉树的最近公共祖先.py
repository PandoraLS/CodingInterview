# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/9 10:02

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createTree():
    """
    //            2
    //          /    \
    //         4      5
    //        /\      /\
    //       8  9    10  11
    :return: 
    """
    p2 = TreeNode(2)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p8 = TreeNode(8)
    p9 = TreeNode(9)
    p10 = TreeNode(10)
    p11 = TreeNode(11)
    p2.left = p4
    p2.right = p5
    p4.left = p8
    p4.right = p9
    p5.left = p10
    p5.right = p11

    root = p2
    return root, p9, p10


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


if __name__ == '__main__':
    so = Solution()
    root, p9, p10 = createTree()
    res = so.lowestCommonAncestor(root, p9, p10)
    print(res)
