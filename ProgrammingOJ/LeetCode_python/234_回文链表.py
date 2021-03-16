# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/4 19:09

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def buildListNodeA():
    n0 = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(2)
    n4 = ListNode(1)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = None
    return n0


def buildListNodeB():
    n0 = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n2_2 = ListNode(3)
    n3 = ListNode(2)
    n4 = ListNode(1)
    n0.next = n1
    n1.next = n2
    n2.next = n2_2
    n2_2.next = n3
    n3.next = n4
    n4.next = None
    return n0


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        if head.next is None:
            return True

        mid = self.get_mid(head)
        part2 = mid.next
        reverse_part2 = self.reverseList(part2)
        p1, p2 = head, reverse_part2
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

    def reverseList(self, head: ListNode) -> ListNode:
        # 反转链表
        prev, curr = None, head
        while curr:
            temp = curr.next  # temp变为下一个节点
            curr.next = prev  # 指向前个节点，此时链表断裂
            prev = curr  # prev变为当前节点
            curr = temp  # curr变为temp节点
        return prev

    def get_mid(self, head):
        # 获取链表中间
        if head is None:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    so = Solution()
    headA = buildListNodeA()
    headB = buildListNodeB()
    print(so.isPalindrome(headA))
    print(so.isPalindrome(headB))
