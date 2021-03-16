# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/3 17:56

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        lookup = {}

        def dfs(node):
            if not node:
                return None
            if node in lookup:
                return lookup[node]
            clone = Node(node.val)
            lookup[node] = clone
            clone.next = dfs(node.next)
            clone.random = dfs(node.random)
            return clone

        return dfs(head)


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.next = n2
    n1.random = None
    n2.next = n3
    n2.random = n1
    n3.next = None
    n3.random = Node

    head = n1
    so = Solution()
    clone = so.copyRandomList(head)
    pass
