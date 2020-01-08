# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/8 13:03

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        list1 = []
        list2 = []
        node1 = pHead1
        node2 = pHead2
        while node1:
            list1.append(node1.val)
            node1 = node1.next
        while node2:
            if node2.val in list1:
                return node2
            else:
                node2 = node2.next


def creatNode():
    n1_1 = ListNode(1)
    n1_2 = ListNode(2)
    n1_3 = ListNode(3)
    n1_4 = ListNode(6)
    n1_5 = ListNode(7)
    n1_1.next = n1_2
    n1_2.next = n1_3
    n1_3.next = n1_4
    n1_4.next = n1_5

    n2_1 = ListNode(4)
    n2_2 = ListNode(5)
    n2_3 = ListNode(6)
    n2_4 = ListNode(7)
    n2_1.next = n2_2
    n2_2.next = n2_3
    n2_3.next = n2_4
    return n1_1, n2_1


if __name__ == '__main__':
    node1, node2 = creatNode()
    so = Solution()
    print(so.FindFirstCommonNode(node1, node2).val)
