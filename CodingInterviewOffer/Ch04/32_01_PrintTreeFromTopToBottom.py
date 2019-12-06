# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 9:12
# @Author  : Li Sen
"""
// 面试题32（一）：不分行从上往下打印二叉树
// 题目：从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):  # 无需使用队列，只是循环左右子树，然后将左右子树添加到[nextStack]
        if not root:
            return []
        currentStack = [root]
        res = []
        while currentStack:
            nextStack = []
            for i in currentStack:
                if i.left: nextStack.append(i.left)
                if i.right: nextStack.append(i.right)
                res.append(i.val)
            currentStack = nextStack
        return res


def createNodes():
    """
    //            8
    //          /    \
    //         6      10
    //        /\      /\
    //       5  7    9  11
    :return: 
    """
    p8 = TreeNode(8)
    p6 = TreeNode(6)
    p10 = TreeNode(10)
    p5 = TreeNode(5)
    p7 = TreeNode(7)
    p9 = TreeNode(9)
    p11 = TreeNode(11)
    p8.left = p6
    p8.right = p10
    p6.left = p5
    p6.right = p7
    p10.left = p9
    p10.right = p11

    root = p8
    return root


if __name__ == '__main__':
    root = createNodes()
    so = Solution()
    print(so.PrintFromTopToBottom(root))
