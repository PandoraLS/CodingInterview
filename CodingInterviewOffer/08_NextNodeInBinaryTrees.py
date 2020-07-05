# -*- coding: utf-8 -*-
# @Time: 2019/9/28 15:47
# @Author: Li Sen

"""
面试题8：二叉树的下一个节点
题目描述：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None  # 父节点


class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode: # 判断非空
            return None

        # 1. 有右子树，下一结点是右子树中的最左结点，例如 B，下一结点是 H
        if pNode.right:
            res = pNode.right
            while res.left:
                res = res.left
            return res

        # 2.  无右子树，则向上回溯其父节点
        # 2.1 该节点是其父节点的左子树，则该节点的父节点即为所求，例如 H，下一结点是 E
        # 2.2 该节点不是其父节点的左子树（换句话说就是其父节点的右子树），则持续回溯其
        #     父节点，直到找到一个节点满足其为其父节点的左子树，则其父节点即为所求，比如 I
        #     的下一个节点为 A，如果找不到满足条件的这样一节点，比如 G 节点，那么 G 节点
        #     就是最后一个节点，他没有下一个节点。
        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp
            pNode = tmp
        return None




if __name__ == '__main__':
    # 根据书本上图2.8构建一个二叉树
    n_a = TreeLinkNode('a')
    n_b = TreeLinkNode('b')
    n_c = TreeLinkNode('c')
    n_d = TreeLinkNode('d')
    n_e = TreeLinkNode('e')
    n_f = TreeLinkNode('f')
    n_g = TreeLinkNode('g')
    n_h = TreeLinkNode('h')
    n_i = TreeLinkNode('i')
    n_a.left = n_b; n_a.right = n_c
    n_b.left = n_d; n_b.right = n_e; n_b.next = n_a
    n_c.left = n_f; n_c.right = n_g; n_c.next = n_a
    n_d.next = n_b
    n_e.left = n_h; n_e.right = n_i; n_e.next = n_b
    n_f.next = n_c
    n_g.next = n_c
    n_h.next = n_e
    n_i.next = n_e

    # 中序遍历 [d, b, h, e, i, a, f, c, g]
    testNode = n_g
    result = Solution().GetNext(testNode)
    if result != None:
        print(result.val)
    else:
        # 如果result为空，说明该node是中序遍历最后一个节点，没有下一个节点
        # ，直接输出该节点的val即可
        print(testNode.val)

