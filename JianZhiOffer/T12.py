# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/4/9 20:53
from typing import List
from pprint import pprint


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False
        row, col = len(board), len(board[0])
        n = len(word)
        vis = [[False] * col for _ in range(row)]

        def dfs(x, y, i, row, col):
            # pprint(vis)
            vis[x][y] = True
            if i == n:
                return True
            for dx, dy in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == word[i] and not vis[nx][ny]:
                    res = dfs(nx, ny, i + 1, row, col)
                    if res:
                        return True
            vis[x][y] = False
            return False

        for i in range(row):
            for j in range(col):
                if word[0] == board[i][j]:
                    # print("新入口：", 'i:', i, 'j:', j, '*' * 50)
                    vis = [[False] * col for _ in range(row)]
                    res = dfs(i, j, 1, row, col)
                    if res:
                        return True
        return False


if __name__ == "__main__":
    so = Solution()
    board = [["A", "B", "C", "E"],
             ["S", "F", "E", "S"],
             ["A", "D", "E", "E"]]
    word = 'ABCESEEEFS'
    print(so.exist(board, word))
