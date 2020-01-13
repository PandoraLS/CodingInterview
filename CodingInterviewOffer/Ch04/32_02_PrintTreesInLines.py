# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 10:07
# @Author  : Li Sen

"""
// 面试题32（二）：分行从上到下打印二叉树
// 题目：从上到下按层打印二叉树，同一层的结点按从左到右的顺序打印，每一层
// 打印到一行。
https://leetcode.com/problems/binary-tree-level-order-traversal/solution/
解答：https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def Print(self, root):
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf] # 对于temp中的每个叶子，如果leaf存在，那么level变成那个叶子，接着进行下一步操作
        return ans


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
    print(so.Print(root))
