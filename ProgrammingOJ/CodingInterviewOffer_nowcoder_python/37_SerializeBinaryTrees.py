# -*- coding: utf-8 -*-
# @Time    : 2019/12/12 16:43
# @Author  : Li Sen

"""
// 面试题37：序列化二叉树
// 题目：请实现两个函数，分别用来序列化和反序列化二叉树。
链接：https://www.nowcoder.com/questionTerminal/cf7e25aa97c04cc1a68c8f040e71fb84
来源：牛客网
请实现两个函数，分别用来序列化和反序列化二叉树
二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，
从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，
序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#）。
二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.flag = -1

    def Serialize(self, root):
        # write code here
        if root == None:
            return '#,'
        return str(root.val) + ',' + self.Serialize(root.left) + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        # print(len(s))
        self.flag += 1
        l = s.split(',')
        root = None
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

def createNodes():
    """
    //           1
    //          /  \
    //         2    3
    //        /     /\ 
    //       4     5  6 
    :return: 
    """
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p6 = TreeNode(6)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p3.left = p5
    p3.right = p6

    root = p1
    return root


if __name__ == '__main__':
    root = createNodes()
    so = Solution()
    string = so.Serialize(root)
    Tree = so.Deserialize(string)
    print(string)
    print(Tree)
