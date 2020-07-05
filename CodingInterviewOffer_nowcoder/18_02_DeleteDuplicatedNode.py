# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 22:04
# @Author  : Li Sen

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None:
            return None

        pPreNode = None
        pNode = pHead
        while (pNode != None):
            pNext = pNode.next
            needDelete = False
            if pNext != None and pNext.val == pNode.val:
                needDelete = True
            
            if not needDelete:
                pPreNode = pNode
                pNode = pNode.next
            else:
                value = pNode.val
                pToBeDel = pNode
                while pToBeDel != None and pToBeDel.val == value:
                    pNext = pToBeDel.next
                    pToBeDel = pNext
                if pPreNode == None:
                    pHead = pNext
                else:
                    pPreNode.next = pNext
                pNode = pNext
        return pHead


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(4)
    node7 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    print("原链表：")
    nodeTemp = node1
    while True:  # 输出所有链表节点
        if nodeTemp.next != None:
            print(nodeTemp.val)
            nodeTemp = nodeTemp.next
        else:
            print(nodeTemp.val)
            break
    print('删除重复节点后的链表：')
    so = Solution()
    so.deleteDuplication(node1)
    nodeTemp = node1
    while True:  # 输出所有链表节点
        if nodeTemp.next != None:
            print(nodeTemp.val)
            nodeTemp = nodeTemp.next
        else:
            print(nodeTemp.val)
            break
