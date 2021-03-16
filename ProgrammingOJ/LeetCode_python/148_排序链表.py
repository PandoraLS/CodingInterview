# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/3 20:22

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next


class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        mid = self.get_mid(head)
        l = head
        r = mid.next
        mid.next = None
        return self.merge(self.sortList(l), self.sortList(r))

    def merge(self, p, q):
        tmp = ListNode(0)
        h = tmp  # h相当于一个临时的result
        while p and q:  # p相当于left，q相当于right
            # 将p或q中较小的一个赋值给h，同时将h.next指向较大的那个
            if p.val < q.val:
                h.next = p  # 将h指向p
                p = p.next
            else:
                h.next = q
                q = q.next
            h = h.next
        if p:
            h.next = p
        if q:
            h.next = q
        return tmp.next

    def get_mid(self, node):
        if node is None:
            return node
        fast = slow = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def buildListNode():
    n0 = ListNode(3)
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(6)
    n4 = ListNode(5)
    n5 = ListNode(1)
    n6 = ListNode(7)
    n7 = ListNode(8)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = None

    return n0


if __name__ == '__main__':
    head = buildListNode()
    # so = Solution()
    # result = so.sortList(head)
    # 
    # p = result
    # while p != None:
    #     # print(p.val)
    #     p = p.next

    print('------------------------')
    so2 = Solution2()
    result2 = so2.sortList(head)
    p2 = result2
    while p2 != None:
        print(p2.val)
        p2 = p2.next
