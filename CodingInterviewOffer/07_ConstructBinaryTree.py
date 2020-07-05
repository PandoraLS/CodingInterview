# -*- coding: utf-8 -*-
# @Time: 2019/9/28 11:04
# @Author: Li Sen

"""
面试题7：重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        """
        :param pre: 前序序列
        :param tin: 中序序列
        :return: 返回树的根root
        """
        # write code here
        if not pre or not tin:  # 如果pre或tin为空则返回None
            return None

        root = TreeNode(pre[0])  # 前序序列的第一个为根
        index = tin.index(pre[0])  # index是判断根在tin中的位置

        root.left = self.reConstructBinaryTree(pre[1:index + 1], tin[:index])
        root.right = self.reConstructBinaryTree(pre[index + 1:], tin[index + 1:])
        return root


if __name__ == '__main__':
    # 根据书本上图2.6构建一个二叉树
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n3.left = n5
    n3.right = n6
    n4.right = n7
    n6.left = n8

    pre = [n1, n2, n4, n7, n3, n5, n6, n8]  # 前序序列
    tin = [n4, n7, n2, n1, n5, n3, n8, n6]  # 中序序列

    result = Solution().reConstructBinaryTree(pre, tin)
    # result实际上是一个树，result.val则是一个树根，依然是TreeNode对象，
    # result.val.val才是树根的值
    print(result.val.val)
