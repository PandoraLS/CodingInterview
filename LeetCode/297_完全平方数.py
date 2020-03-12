# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/12 10:34

from collections import deque


# https://leetcode-cn.com/problems/perfect-squares/solution/dong-tai-gui-hua-bfs-zhu-xing-jie-shi-python3-by-2/
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        # print(dp)
        for i in range(2, n + 1):
            for j in range(1, int(i ** (0.5)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[-1]


class Solution2:
    def numSquares(self, n: int) -> int:
        # 广度优先搜索
        if n == 0:
            return 0
        queue = deque([n])
        step = 0
        visit = set()
        while queue:
            step += 1
            for i in range(len(queue)):
                tmp = queue.popleft()
                j = 1
                while j * j <= tmp:
                    rest = tmp - j * j
                    if rest == 0:
                        return step
                    if rest not in visit:
                        queue.append(rest)
                        visit.add(rest)
                    j += 1
        return step


if __name__ == '__main__':
    so = Solution()
    print(so.numSquares(12))
    so2 = Solution2()
    print(so2.numSquares(12))
