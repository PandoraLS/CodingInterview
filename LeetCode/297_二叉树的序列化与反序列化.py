# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/9 10:39
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createTree():
    """
    //            2
    //          /   \
    //         4     5
    //               /\
    //             10  11
    :return: 
    """
    p2 = TreeNode(2)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p10 = TreeNode(10)
    p11 = TreeNode(11)
    p2.left = p4
    p2.right = p5
    p5.left = p10
    p5.right = p11

    root = p2
    return root


class Codec:
    # 使用前序遍历:leetcode测试通过
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append('N')
            else:
                res.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        res = deque(data.split(','))
        def dfs(res):
            if res[0] == 'N':
                res.popleft()
                return None
            root = TreeNode(int(res[0]))
            res.popleft()
            root.left = dfs(res)
            root.right = dfs(res)
            return root
        return dfs(res)


class Codec2:
    # 使用后续遍历:leetcode测试通过
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append('N')
            else:
                dfs(root.left)
                dfs(root.right)
                res.append(str(root.val))
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        res = deque(data.split(','))
        def dfs(res):
            if res[-1] == 'N':
                res.pop()
                return None
            root = TreeNode(int(res[-1]))
            res.pop()
            root.right = dfs(res)
            root.left = dfs(res)
            return root
        return dfs(res)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == '__main__':
    codec = Codec()
    root = createTree()
    print("使用前序遍历的序列化与反序列化")
    res = codec.serialize(root)
    print(res)
    re_root = codec.deserialize(res)


    print("使用后续遍历的序列化与反序列化")
    codec2 = Codec2()
    res = codec2.serialize(root)
    print(res)
    re_root = codec2.deserialize(res)
    pass
