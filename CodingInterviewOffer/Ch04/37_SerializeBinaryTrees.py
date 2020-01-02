# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/2 16:08

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.index = -1

    def Serialize(self, root):
        # write code here
        if root == None:
            return '#,'
        return str(root.val) + ',' + self.Serialize(root.left) + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        # print(len(s))
        self.index += 1
        l = s.split(',')

        root = None
        index = self.index
        if l[self.index] != '#':
            root = TreeNode(int(l[self.index]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root


def createNodes():
    """
    //            1
    //          /   \
    //         2     3
    //        /      /\ 
    //       4      5  6 
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
    serialize = so.Serialize(root)
    print(serialize)
    deserialize = so.Deserialize(serialize)
    print(deserialize)
    