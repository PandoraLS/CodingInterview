# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 19:34
# @Author  : Li Sen

"""
// 面试题35：复杂链表的复制
// 题目：请实现函数ComplexListNode* Clone(ComplexListNode* pHead)，复
// 制一个复杂链表。在复杂链表中，每个结点除了有一个m_pNext指针指向下一个
// 结点外，还有一个m_pSibling 指向链表中的任意结点或者nullptr。
参考链接：https://www.cnblogs.com/yanmk/p/9220525.html
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
        
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        newNode = RandomListNode(pHead.label)
        newNode.random = pHead.random
        newNode.next = self.Clone(pHead.next)
        return newNode


def createListNodes():
    """
    :return: 书上图4.11的复杂链表 
    """
    p1 = RandomListNode(1)
    p2 = RandomListNode(2)
    p3 = RandomListNode(3)
    p4 = RandomListNode(4)
    p5 = RandomListNode(5)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p1.random = p3
    p2.random = p5
    p4.random = p2
    head = p1
    return head


if __name__ == '__main__':
    head = createListNodes()
    so = Solution()
    print(so.Clone(head))

