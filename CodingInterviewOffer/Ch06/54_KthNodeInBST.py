# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/8 15:03

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot == None or k <= 0:
            return None
        res = []

        def InOrder(pRoot):
            if not pRoot:
                return []
            InOrder(pRoot.left)
            res.append(pRoot)
            InOrder(pRoot.right)

        InOrder(pRoot)
        if len(res) < k:
            return None
        return res[k - 1]


def createNodes():
    """
    //            5
    //          /    \
    //         3      7
    //        / \     /\ 
    //       2   4   6  8 
    :return: 
    """
    p5 = TreeNode(5)
    p3 = TreeNode(3)
    p7 = TreeNode(7)
    p2 = TreeNode(2)
    p4 = TreeNode(4)
    p6 = TreeNode(6)
    p8 = TreeNode(8)
    p5.left = p3
    p5.right = p7
    p3.left = p2
    p3.right = p4
    p7.left = p6
    p7.right = p8
    root = p5
    return root


if __name__ == '__main__':
    so = Solution()
    root = createNodes()
    print(so.KthNode(root, 3).val)
