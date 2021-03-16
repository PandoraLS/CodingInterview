# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 10:39
# @Author  : Li Sen

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l


if __name__ == '__main__':
    # node1 -> node2 -> node3
    # node1,node2,node3的val分别为1,2,3
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    result = Solution().printListFromTailToHead(node1)
    print(result)
