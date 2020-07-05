# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 10:49
# @Author  : Li Sen

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        # 将左子树构建成双链表，返回链表头
        left = self.Convert(pRootOfTree.left)
        p = left

        # 定位至左子树最右边的一个节点
        while left and p.right:
            p = p.right

        # 如果左子树不为空，将当前pRootOfTree加到左子树链表
        if left:
            p.right = pRootOfTree
            pRootOfTree.left = p

        # 将右子树变成双向链表，返回链表头
        right = self.Convert(pRootOfTree.right)
        if right:
            right.left = pRootOfTree
            pRootOfTree.right = right

        return left if left else pRootOfTree


def createNodes():
    """
    //            10
    //          /    \
    //         6       14
    //        /\       /\ 
    //       4  8    12  16 
    :return: 
    """
    p10 = TreeNode(10)
    p6 = TreeNode(6)
    p14 = TreeNode(14)
    p4 = TreeNode(4)
    p8 = TreeNode(8)
    p12 = TreeNode(12)
    p16 = TreeNode(16)
    p10.left = p6
    p10.right = p14
    p6.left = p4
    p6.right = p8
    p14.left = p12
    p14.right = p16

    root = p10
    return root


if __name__ == '__main__':
    root = createNodes()
    so = Solution()
    print(so.Convert(root))
