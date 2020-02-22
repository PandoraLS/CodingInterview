# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/22 17:59

class Solution:
    def findWords(self, board, words):
        # 字典树+搜索
        row, col = len(board), len(board[0])  # row行，col列
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True
        res = set()

        def dfs(r, c, node, prefix, visited):
            """
            :param r: 行
            :param c: 列
            :param node: word组成的字典树
            :param prefix: 前缀
            :param visited: 是否visited过
            :return: 
            """
            if '#' in node:
                res.add(prefix)
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 网格上下左右的表示方法
                new_r, new_c = r + dx, c + dy
                if 0 <= new_r < row and 0 <= new_c < col and board[new_r][new_c] in node \
                        and (new_r, new_c) not in visited:
                    dfs(new_r, new_c, node[board[new_r][new_c]], prefix + board[new_r][new_c],
                        visited | {(new_r, new_c)})

        for r in range(row):
            for c in range(col):
                if board[r][c] in trie:
                    dfs(r, c, trie[board[r][c]], board[r][c], {(r, c)})
        return list(res)


class Solution2:
    def findWords(self, board, words):
        # 字典树+搜索
        rows, cols = len(board), len(board[0])
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True
        res = set()

        def dfs(r, c, node, prefix, visited):
            if '#' in node:
                res.add(prefix)
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_r, new_c = r + dx, c + dy
                if 0 <= new_r < rows and 0 <= new_c < cols and board[new_r][new_c] in node \
                        and (new_r, new_c) not in visited:
                    dfs(new_r, new_c,
                        node[board[new_r][new_c]],
                        prefix + board[new_r][new_c],
                        visited | {(new_r, new_c)})

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r, c, trie[board[r][c]], board[r][c], {(r, c)})
        return list(res)


if __name__ == '__main__':
    so = Solution()
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    print(so.findWords(board, words))
