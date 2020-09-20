# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/4 13:30

class MinHeap():
    def __init__(self, maxSize=None):
        self.maxSize = maxSize
        self.li = [None] * maxSize
        self.count = 0

    def length(self):
        # 求目前数组的长度
        return self.count

    def show(self):
        if self.count <= 0:
            print('null')
        else:
            print(self.li[:self.count])

    def add(self, value):
        if self.count >= self.maxSize:  # 判断数组是否越界
            raise Exception('full')

        self.li[self.count] = value  # 将新节点增加到最后
        self._shift_up(self.count)  # 递归构建大堆
        self.count += 1

    def _shift_up(self, index):
        # 往最小堆中添加元素，并保证根节点是最小的值
        # 1. 增加新的值到最后一个节点，在add()实现
        # 2. 与父节点比较，如果比父节点值小，则交换
        if index > 0:
            parent = (index - 1) // 2  # 找到跟节点
            if self.li[index] < self.li[parent]:  # 如果叶子节点比parent小，则交换
                self.li[index], self.li[parent] = self.li[parent], self.li[index]
                self._shift_up(parent)

    def extract(self):
        # 弹出最小堆的根节点，即最小值
        # 1. 删除根节点，将最后一个节点作为跟节点
        # 2. 判断根节点与左右节点的大小，交换左右节点较小的
        if not self.count:
            raise Exception('null')
        value = self.li[0]
        self.count -= 1
        self.li[0] = self.li[self.count]  # 将最后一个值变为第一个
        self._shift_down(0)
        return value

    def _shift_down(self, index):
        # 1. 判断是否有左子节点，左是否小于跟，做是否小于右
        # 2. 判断是否有右子节点，右小于跟
        left = 2 * index + 1
        right = 2 * index + 2
        minimum = index

        # 先判断左(left)是否小于根(minimum)，再判断右(right)是否小于minimum
        if left < self.length() and self.li[left] < self.li[minimum]:
            minimum = left
        if right < self.length() and self.li[right] < self.li[minimum]:
            minimum = right

        if minimum != index:
            self.li[index], self.li[minimum] = self.li[minimum], self.li[index]
            self._shift_down(minimum)


if __name__ == '__main__':
    m = MinHeap(10)
    import numpy as np

    np.random.seed(100)
    num = np.random.randint(100, size=10)  # 创建随机的10个数
    print("m.length(): ", m.length())
    for i in num:
        m.add(i)
    m.show()
    print("m.length(): ", m.length())
    for i in range(5):
        print(m.extract(), end=', ')
