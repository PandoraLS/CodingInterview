"""

前序中序重建树
后续中序重建树
"""


from DataStructure.tree import TreeNode, in_order

def build_tree_pre_in(preorder, inorder):
    if not inorder:
        return None
    root = TreeNode(preorder[0])
    idx = inorder.index(root.val)
    root.left = build_tree_pre_in(preorder[1:idx + 1], inorder[:idx])
    root.right = build_tree_pre_in(preorder[idx + 1:], inorder[idx+1:])
    return root


def build_tree_in_post(inorder, postorder):
    if not inorder:
        return None
    root = TreeNode(postorder[-1])
    idx = inorder.index(root.val)
    root.left = build_tree_in_post(inorder[:idx], postorder[:idx])
    root.right = build_tree_in_post(inorder[idx + 1:], postorder[idx:-1])
    return root

pre_order_list = [3, 9, 8, 5, 4, 6, 20, 15, 7]
in_order_list = [4, 5, 8, 6, 9, 3, 15, 20, 7]
post_order_list = [4, 5, 6, 8, 9, 15, 7, 20, 3]
print(in_order(build_tree_pre_in(pre_order_list, in_order_list)))
print(in_order(build_tree_in_post(in_order_list, post_order_list)))