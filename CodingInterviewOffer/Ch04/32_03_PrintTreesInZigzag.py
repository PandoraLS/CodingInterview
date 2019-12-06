# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 12:04
# @Author  : Li Sen

"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
32_2 之字形打印二叉树
解法：https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/33833/Simple-and-clear-python-solution-with-explain
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        res, level, count = [], [root], 0

        while level:
            # if count % 2 == 0:
            #     res.append([node.val for node in level])
            # else:
            #     res.append([node.val for node in level[::-1]])
            res.append([node.val for node in level]) if count % 2 == 0 else res.append(
                [node.val for node in level[::-1]])

            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [newnode for newnode in temp if newnode]
            count += 1
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
    print(so.zigzagLevelOrder(root))
