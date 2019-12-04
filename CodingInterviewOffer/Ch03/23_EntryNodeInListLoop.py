# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 14:34
# @Author  : Li Sen

"""
// 面试题23：链表中环的入口结点
// 题目：一个链表中包含环，如何找出环的入口结点？例如，在图3.8的链表中，
// 环的入口结点是结点3。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # 链接：https: // www.nowcoder.com / questionTerminal / 253
        # d2c59ec3e4bc68da16833f79a38e4?answerType = 1 & f = discussion
        # 来源：牛客网
        # 
        # 思路2：快慢指针。快指针一次走两步，慢指针一次走一步，设链表起点到入口结点的长度是x1，快慢指针第一次相遇时距离入口结点的长度是x2，此时慢指针走了x1 + x2，快指针走了2x1 + 2
        # x2，也就是说(x1 + x2)[多出来的路程肯定是圈圈的整数倍]的长度正好是环的一圈大小的倍数。
        # 此时让一个指针从起点出发，一个指针从相遇结点出发，都是一次走一步，当两个指针第一次相遇时恰好是在入口结点。
        # write code here
        meetingNode = self.MeetingNode(pHead)
        if meetingNode == None:
            return None

        # 得到环中节点的数目
        nodesInLoop = 1
        pNode1 = meetingNode
        while pNode1.next != meetingNode:
            pNode1 = pNode1.next
            nodesInLoop += 1

        # 先移动pNode1，次数为环中节点数目
        pNode1 = pHead
        for i in range(nodesInLoop):
            pNode1 = pNode1.next

        # 再移动pNode1和pNode2
        pNode2 = pHead
        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        return pNode1

    def MeetingNode(self, pHead):
        if pHead == None:
            return None

        pSlow = pHead.next
        if pSlow == None:
            return None

        pFast = pSlow.next
        while pFast != None and pSlow != None:
            if pFast == pSlow:
                return pFast
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast != None:
                pFast = pFast.next
        return None


    # 链接：https://www.nowcoder.com/questionTerminal/253d2c59ec3e4bc68da16833f79a38e4?answerType=1&f=discussion
    # 来源：牛客网
    def EntryNodeOfLoop2(self, pHead):
        # write code here
        #遍历链表，环的存在，遍历遇见的第一个重复的即为入口节点
        tempList = []
        p = pHead
        while p:
            if p in tempList:
                return p
            else:
                tempList.append(p)
            p = p.next
