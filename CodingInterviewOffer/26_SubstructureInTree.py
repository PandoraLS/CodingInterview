# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 19:38
# @Author  : Li Sen

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 != None and pRoot2 != None:
            if self.Equal(pRoot1.val, pRoot2.val):
                result = self.DoesTree1HaveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def DoesTree1HaveTree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False

        if not self.Equal(pRoot1.val, pRoot2.val):
            return False

        return self.DoesTree1HaveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HaveTree2(pRoot1.right, pRoot2.right)

    def Equal(self, num1, num2):
        if num1 == num2:
            return True
        else:
            return False
