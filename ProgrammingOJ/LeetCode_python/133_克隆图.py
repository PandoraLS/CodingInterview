# -*- coding: utf-8 -*-
# @Time : 2020/4/25 10:49

"""
leetcode:133_克隆图
遍历整个图，所以遍历时候要记录已经访问点，用一个字典记录
题解参考：https://leetcode-cn.com/problems/clone-graph/solution/dfs-he-bfs-by-powcai/
"""
# Definition for a Node.


class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

    def __repr__(self):
        val = str(self.val)
        neighbors = [str(node.val) for node in self.neighbors]
        return "当前节点值 " + val + " 邻居节点值 " + " ".join(neighbors)


class Solution:

    def cloneGraph_dfs(self, node: 'Node') -> 'Node':
        lookup = {}

        def dfs(node):
            # print(node.val)
            if not node: return
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        return dfs(node)

    def cloneGraph_bfs(self, node: 'Node') -> 'Node':
        from collections import deque
        lookup = {}

        def bfs(node):
            if not node: return
            clone = Node(node.val, [])
            lookup[node] = clone
            queue = deque()
            queue.appendleft(node)
            while queue:
                tmp = queue.pop()
                for n in tmp.neighbors:
                    if n not in lookup:
                        lookup[n] = Node(n.val, [])
                        queue.appendleft(n)
                    lookup[tmp].neighbors.append(lookup[n])
            return clone

        return bfs(node)


def create_graph():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    return node1


if __name__ == '__main__':
    nums = [[2,4],[1,3],[2,4],[1,3]]
    so = Solution()
    node1 = create_graph()
    node1_copy = so.cloneGraph_dfs(node1)
    print(node1_copy.val, str(node1_copy.neighbors))
    print(str(node1_copy))

    s = " a\ta   "
    print(s)
    print(repr(s))
