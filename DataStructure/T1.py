# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/31 9:58


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
       @param: root: The root of the binary search tree.
       @param: A: A TreeNode in a Binary.
       @param: B: A TreeNode in a Binary.
       @return: Return the least common ancestor(LCA) of the two nodes.
       """

    def lowestCommonAncestor(self, root, A, B):
        if (root is None or root == A or root == B):
            return root  # 若root为空或者root为A或者root为B，说明找到了A和B其中一个
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        if (left is not None and right is not None):
            return root  # 若左子树找到了A，右子树找到了B，说明此时的root就是公共祖先
        if (left is None):  # 若左子树是none右子树不是，说明右子树找到了A或B
            return right
        if (right is None):  # 同理
            return left
        return None



