# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/9 12:14
from typing import List
from heapq import *
from queue import PriorityQueue as PQ


# https://zhuanlan.zhihu.com/p/48403793
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 思路：最大堆，每次在判断关键点的时候，移除所有右端点≤当前点的堆顶。
        if not buildings: return []
        points = []
        heap = [[0, float('inf')]]  # 最大堆用来存储的是当前的楼层高度
        res = [[0, 0]]  # 用于存储关键点[最大高度发生改变的点]

        # 1.将所有端点加入到点集中(每个建筑物的左右端点)
        for l, r, h in buildings:
            points.append((l, -h, r))  # 这里负号将最小堆变成了最大堆
            points.append((r, h, 0))  # r的右端点为0

        # 2.将端点从小到大排序
        points.sort()  # 如果当前点相等，则按照高度升序

        # 3.遍历每一个点，分别判断出堆、入堆、添加关键点操作。
        for l, h, r in points:
            while l >= heap[0][1]:  # 出堆：保证当前堆顶为去除之前建筑物右端点的最大值。
                heappop(heap)
            if h < 0:  # 入堆：所有左端点都要入堆
                heappush(heap, [h, r])
            if res[-1][1] != -heap[0][0]:  # 关键点：必然是左端点，堆顶，因此需要加负号
                res.append([l, -heap[0][0]])
        return res[1:]

    def getSkyline2(self, buildings: List[List[int]]) -> List[List[int]]:
        # `position` 存储那些最大高度可能会变的坐标
        # `alive` 存储所有覆盖当前坐标的建筑
        position = sorted(set([building[0] for building in buildings] + [building[1] for building in buildings]))
        ptr, prevH = 0, 0
        alive, ret = [], []

        for curPos in position:
            # pop buildings that end at or before `curPos` out of the priority queue
            # they are no longer "alive"
            while alive and alive[0][1] <= curPos:
                heappop(alive)

            # push [negative_height, end_point] of all buildings that start before `curPos` onto the priority queue
            # they are candidates for the current highest building
            while ptr < len(buildings) and buildings[ptr][0] <= curPos:
                heappush(alive, [-buildings[ptr][2], buildings[ptr][1]])
                ptr += 1

            # now alive[0] must be the largest height at the current position
            if alive:
                curH = -alive[0][0]
                if curH != prevH:
                    ret.append([curPos, curH])
                    prevH = curH
            else:  # no building -> horizon
                ret.append([curPos, 0])

        return ret


if __name__ == '__main__':
    ipt = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    # 预期结果：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    so = Solution()
    print(so.getSkyline2(ipt))
