# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/4/9 20:53
from typing import List

"""
思路：使用dfs+一个变量统计当前走过多少个字母了
如果本题使用deque,走过一个弹出一个的话，会存在一个问题,当前入口走完了没有弹出完，但是下个入口把deque中的字母全部弹出了的话
就不符合题意了,使用变量技术依然是比较好的方法
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False
        row, col = len(board), len(board[0])
        n = len(word)
        # vis = [[False] * cols] * rows # !!!这种初始化方法是错误的!!!,这样初始化后的vis在修改vis[x][y]时会把整列都修改了,这是python的bug
        vis = [[False] * col for _ in range(row)]
        # pprint(vis)
        def dfs(x, y, i):
            # pprint(vis)
            vis[x][y] = True
            if i == n:
                return True
            for dx, dy in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == word[i] and not vis[nx][ny]:
                    res = dfs(nx, ny, i + 1)
                    if res:
                        return True
            vis[x][y] = False
            return False

        for i in range(row):
            for j in range(col):
                if word[0] == board[i][j]:
                    # print("新入口：", 'i:', i, 'j:', j, '*' * 50)
                    res = dfs(i, j, 1)
                    if res:
                        return True
        return False

class Solution2:
    # 这种方法存在问题!!!
    def exist(self, board: List[List[str]], word: str) -> bool:
        from collections import deque
        if not word:
            return False
        rows, cols = len(board), len(board[0])
        # vis = [[False] * cols] * rows # python的bug
        vis = [[False] * cols for _ in range(rows)]  # vis这样初始化才正确
        def dfs(x, y, vis, word_deque):
            # pprint(vis)
            vis[x][y] = True
            # word_deque.popleft()
            word_deque = word_deque[1:]
            if not word_deque:
                return True
            for dx, dy in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and vis[nx][ny] == False and board[nx][ny] == word_deque[0]:
                    res = dfs(nx, ny, vis, word_deque)
                    if res:
                        return True
            vis[x][y] = False
            return False
        word_deque = deque(word)
        for i in range(rows):
            for j in range(cols):
                if word[0] == board[i][j]: # 随便找一个初始入口
                    res = dfs(i, j, vis, word_deque)
                    if res:
                        return True
        return False


if __name__ == "__main__":
    so = Solution()
    # board = [["A", "B", "C", "E"],
    #          ["S", "F", "C", "S"],
    #          ["A", "D", "E", "E"]]
    # word = 'ABCCED'
    board = [['a', 'a']]
    word = 'aaa'
    print(so.exist(board, word))
    # so2 = Solution2()
    # print(so2.exist(board, word))
