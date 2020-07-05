# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 13:56
# @Author  : Li Sen

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k == 0:
            return None
        pAhead = head
        pBehind = None

        for i in range(k - 1):
            if pAhead.next != None:
                pAhead = pAhead.next
            else:
                return None

        pBehind = head
        while pAhead.next != None:
            pAhead = pAhead.next
            pBehind = pBehind.next

        return pBehind
