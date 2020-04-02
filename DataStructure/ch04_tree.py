# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/30 9:30
from collections import deque

# 二叉树定义
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pre_order(r):
    if r:
        print(r.val)
        pre_order(r.left)
        pre_order(r.right)


def in_order(r):
    if r:
        return in_order(r.left) + [r.val] + in_order(r.right)
    else:
        return []


def post_order(r):
    if r:
        return post_order(r.left) + post_order(r.right) + [r.val]
    else:
        return []


def level_order(r):
    # bfs
    # 弹出，输出，处理子树
    levels = []
    queue = deque([r])
    while queue:
        levels.append([])
        level_len = len(queue)
        for i in range(level_len):
            r = queue.popleft()
            levels[-1].append(r.val)
            # levels.append(r.val)
            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)
    return levels


def createTree():
    """
    //            2
    //          /    \
    //         4      5
    //                /\
    //               10  11
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


if __name__ == '__main__':
    root = createTree()
    # pre_order(root)
    # print(in_order(root))
    # print(post_order(root))
    print(level_order(root))
