# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 22:46
# @Author  : sen


"""
思路：
1 单独一个函数计算每个数位的和
2 dfs对符合条件的进行标记
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def digit_sum(num):
            res = 0
            while num:
                q, r = divmod(num, 10)
                res += r
                num = q
            return res

        digit_sum_cache = {}
        vis = [[False] * n for _ in range(m)]

        def dfs(x, y):
            vis[x][y] = True
            for dx, dy in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if nx not in digit_sum_cache:
                        digit_sum_cache[nx] = digit_sum(nx)
                    if ny not in digit_sum_cache:
                        digit_sum_cache[ny] = digit_sum(ny)
                    if digit_sum_cache[nx] + digit_sum_cache[ny] <= k and not vis[nx][ny]:
                        dfs(nx, ny)

        dfs(0, 0)
        return sum([sum(_) for _ in vis])


if __name__ == '__main__':
    so = Solution()
    print(so.movingCount(2,3,1))


