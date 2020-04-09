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


def print_pre_order(r):
    if r:
        print(r.val)
        pre_order(r.left)
        pre_order(r.right)


def pre_order(r):
    if r:
        return [r.val] + pre_order(r.left) + pre_order(r.right)
    else:
        return []


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
    # 弹出，输出，处理子树， 层次遍历
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
    //            3
    //          /    \
    //         9      20
    //        /       /\
    //       8       15  7
    //      / \
    //     5   6
    //    /
    //   4
    :return: 
    """
    p3 = TreeNode(3)
    p9 = TreeNode(9)
    p20 = TreeNode(20)
    p8 = TreeNode(8)
    p15 = TreeNode(15)
    p7 = TreeNode(7)
    p5 = TreeNode(5)
    p6 = TreeNode(6)
    p4 = TreeNode(4)
    p3.left = p9
    p3.right = p20
    p9.left = p8
    p8.left = p5
    p8.right = p6
    p5.left = p4
    p20.left = p15
    p20.right = p7

    root = p3

    return root


def build_tree_pre_in(preorder, inorder):
    # 前序中序;建树
    if not inorder:
        return None
    root = TreeNode(preorder[0])
    idx = inorder.index(root.val)
    root.left = build_tree_pre_in(preorder[1:idx + 1], inorder[:idx])
    root.right = build_tree_pre_in(preorder[idx + 1:], inorder[idx + 1:])
    return root


def build_tree_in_post(inorder, postorder):
    # 中序后序; 建树
    if not inorder:
        return None
    root = TreeNode(postorder[-1])
    idx = inorder.index(root.val)
    root.left = build_tree_in_post(inorder[:idx], postorder[:idx])
    root.right = build_tree_in_post(inorder[idx + 1:], postorder[idx:-1])
    return root


if __name__ == '__main__':
    root = createTree()
    preorder = pre_order(root)
    inorder = in_order(root)
    postorder = post_order(root)
    print('pre_order:  ', preorder)
    print('in_order:  ', inorder)
    print('post_order:  ', postorder)

    print('前序中序;建树')
    pre_in_root = build_tree_pre_in(preorder, inorder)
    print('前序中序建树后的中序', in_order(pre_in_root))

    print('中序后序;建树')
    in_post_root = build_tree_in_post(inorder, postorder)
    print('中序后序建树后的中序', in_order(in_post_root))
