# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/4/7 9:36

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return self.size


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size = mountain_arr.length()
        if size < 3:
            return -1
        # 步骤1：先找到山顶元素所在的索引
        mountaintop = self._find_mountaintop(mountain_arr, 0, size - 1)

        # 步骤2：在前升序数组中找target所在的索引(含山顶)
        res = self._find_increase_arr(mountain_arr, 0, mountaintop, target)
        if res != -1:
            return res

        # 步骤3：如果步骤2找不到，就在后有序降序数组中找target所在的索引
        return self._find_decrease_arr(mountain_arr, mountaintop + 1, size - 1, target)

    def _find_mountaintop(self, mountain_arr: 'MountainArray', l: int, r: int):
        # 返回山顶元素
        while l < r:
            mid = l + (r - l) // 2
            # 当前数get(mid)比右边的小，那么它一定不是山顶元素
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                # 下一轮搜索区间为
                l = mid + 1
            else:
                r = mid
        return l  # 山顶元素一定存在，退出while的时候，不需要再次判断

    def _find_increase_arr(self, mountain_arr: 'MountainArray', l: int, r: int, target: int):
        # 在前半部分升序数组中找target
        while l < r:
            mid = l + (r - l) // 2
            # 当get(mid)<target时，一定没有解
            if mountain_arr.get(mid) < target:
                # 下一轮搜索空间为
                l = mid + 1
            else:
                r = mid
        # 不确定最后的get(l)是不是target，所以要单独判断
        if mountain_arr.get(l) == target:
            return l
        return -1

    def _find_decrease_arr(self, mountain_arr: 'MountainArray', l: int, r: int, target: int):
        # 在后半部分降序数组中找target
        while l < r:
            mid = l + (r - l) // 2
            # 与_find_increase_arr不同的地方仅仅是由原来的<改为>（大于号）
            # 实际上，这也是降序数组与升序数组的二分查找不同的地方
            if mountain_arr.get(mid) > target:
                # 下一轮搜索空间
                l = mid + 1
            else:
                r = mid
        if mountain_arr.get(l) == target:
            return l
        return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 3, 1]
    mountain_array = MountainArray(arr)
    target = 3
    so = Solution()
    res = so.findInMountainArray(target, mountain_array)
    print(res)