# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 20:54
# @Author  : Li Sen

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, NodeHead, NodeToDeleted):
        # write code here
        if NodeToDeleted.next != None:  # 如果NodeToDeleted不是尾节点
            NodeToDeleted.val = NodeToDeleted.next.val  # 1->2->3->4
            NodeToDeleted.next = NodeToDeleted.next.next  # 1->2->4
        elif NodeHead == NodeToDeleted:  # 只有一个节点(是头节点也是尾节点)的链表
            NodeToDeleted.val = None
            NodeToDeleted.next = None
        else:  # 链表中不止一个节点，删除尾部节点
            pNode = NodeHead
            while pNode.next != NodeToDeleted:
                pNode = pNode.next
            pNode.next = None


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print("原链表：")
    nodeTemp = node1
    while True:  # 输出所有链表节点
        if nodeTemp.next != None:
            print(nodeTemp.val)
            nodeTemp = nodeTemp.next
        else:
            print(nodeTemp.val)
            break
    print('删除节点后的链表：')
    so = Solution()
    so.deleteNode(node1, node4)
    nodeTemp = node1
    while True:  # 输出所有链表节点
        if nodeTemp.next != None:
            print(nodeTemp.val)
            nodeTemp = nodeTemp.next
        else:
            print(nodeTemp.val)
            break
