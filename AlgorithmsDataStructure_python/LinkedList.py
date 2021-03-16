# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 16:01
# @Author  : Li Sen

"""
Python数据结构，链表
https://zhaochj.github.io/2016/05/12/2016-05-12-%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84-%E9%93%BE%E8%A1%A8/#
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def iter(self):
        if not self.head:
            return
        cur = self.head
        yield cur.data
        while cur.next:
            cur = cur.next
            yield cur.data

    def insert(self, idx, value):
        cur = self.head
        cur_idx = 0
        if cur is None:  # 判断是否是空链表
            raise Exception('The list is an empty list')
        while cur_idx < idx - 1:  # 遍历链表
            cur = cur.next
            if cur is None:  # 判断是不是最后一个元素
                raise Exception('list length less than index')
            cur_idx += 1
        node = Node(value)
        node.next = cur.next
        cur.next = node
        if node.next is None:
            self.tail = node

    def remove(self, idx):
        cur = self.head
        cur_idx = 0
        if self.head is None:  # 空链表时
            raise Exception('The list is an empty list')
        while cur_idx < idx - 1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        if idx == 0:  # 当删除第一个节点时
            self.head = cur.next
            cur = cur.next
            return
        if self.head is self.tail:  # 当只有一个节点的链表时
            self.head = None
            self.tail = None
            return
        cur.next = cur.next.next
        if cur.next is None:  # 当删除的节点是链表最后一个节点时
            self.tail = cur

    def size(self):
        current = self.head
        count = 0
        if current is None:
            return 'The list is an empty list'
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found


if __name__ == '__main__':
    link_list = LinkedList()
    for i in range(10):
        link_list.append(i)
    print(link_list)
    #    print(link_list.is_empty())
    #    link_list.insert(10, 30)

    #    link_list.remove(0)

    for node in link_list.iter():
        print('node is {0}'.format(node))
    # print(link_list.size())
#    print(link_list.search(20))
