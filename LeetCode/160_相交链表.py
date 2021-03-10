# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/4 17:13
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def buildListNodeA():
    n0 = ListNode(4)
    n1 = ListNode(1)
    n2 = ListNode(8)
    n3 = ListNode(4)
    n4 = ListNode(5)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = None
    return n0


def buildListNodeB():
    n_1 = ListNode(5)
    n0 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(8)
    n3 = ListNode(4)
    n4 = ListNode(5)
    n_1.next = n0
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = None
    return n_1


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengthA, lengthB = 0, 0
        pA, pB = headA, headB
        while pA:
            lengthA += 1
            pA = pA.next
        while pB:
            lengthB += 1
            pB = pB.next
        if lengthA < lengthB:
            for i in range(lengthB - lengthA):
                headB = headB.next
        else:
            for i in range(lengthA - lengthB):
                headA = headA.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA.val


if __name__ == '__main__':
    so = Solution()
    headA = buildListNodeA()
    headB = buildListNodeB()
    print(so.getIntersectionNode(headA, headB))
