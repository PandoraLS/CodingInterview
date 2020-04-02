# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/4/2 14:15

class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def find(root, val):
    if not root:
        return None
    if val < root.val:
        return find(root.left, val)
    elif val > root.val:
        return find(root.right, val)
    else:
        return root
    

def find_min(root):
    if root:
        while root.left:
            root = root.left
    return root
        

def find_max(root):
    if root:
        while root.right:
            root = root.right
    return root

def insert(root, val):
    if not root:
        root = TreeNode(val)
    elif val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    else:
        pass  # val==root.val   val已经在树中，什么都不做
    return root


def delete(root, val):
    if not root:
        return None
    elif val < root.val:
        root.left = delete(root.left, val)  # 返回左子树的根
    elif val > root.val:
        root.right = delete(root.right, val)
    else:  # 执行删除操作
        if root.left and root.right:  # 两个孩子节点的情况
            tmp = find_min(root.right)
            root.val = tmp.val
            root.right = delete(root.right, tmp.val)
        else:  # 0个或1个
            root = root.left if root.left else root.right
    return root

def height(root):
    if root is None:
        return -1
    else:
        return 1 + max(height(root.left), height(root.right))

if __name__ == '__main__':
    vals = [1, 2, 3, 4, 5, 6, 7, 8]
    root = None
    from DataStructure.ch04_tree import in_order
    for v in vals:
        root = insert(root, v)
    tree_in_order = in_order(root)
    assert vals == tree_in_order, "构建树出错"
    # vals.append(9)
    # root = insert(root, 9)
    # tree_in_order = in_order(root)
    # assert vals == tree_in_order, "插入出错"
    # 
    # vals.remove(6)
    # root = delete(root, 6)
    # tree_in_order = in_order(root)
    # assert vals == tree_in_order, "删除出错"
    
    print(height(root))
    