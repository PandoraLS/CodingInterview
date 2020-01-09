# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/9 20:56

"""
https://blog.csdn.net/u013908099/article/details/87807591
题目2：队列的最大值
请定义一个队列并实现函数max得到队列里的最大值，
要求函数max、push_back和pop_front的时间复杂度都是O(1)。
思路
和题目1一样，在队列中维护一个保存最大值的队列，
当pop和push操作的同时也对最大值队列进行维护。
当弹出的时队列中的最大值时，也弹出最大值队列的头，
当压入新值时，对最大值队列从后向前扫描剔除小于该值的元素。

时间复杂度：O(1)
空间复杂度：O(n)
"""


class Queue:
    def __init__(self):
        self.data = []
        self.max_data = []

    def pop(self):
        """
        pop out the head element
        :return: head element
        """
        if not self.data:
            raise Exception('Empty Queue Cannot Pop')
        if self.data[0] == self.max_data[0]:
            self.max_data.pop(0)
        return self.data.pop(0)

    def push(self, x):
        """
        push in the back
        :param x: element
        :return: None
        """
        self.data.append(x)
        while self.max_data and self.max_data[-1] < x:
            self.max_data.pop()
        self.max_data.append(x)
        return

    def max(self):
        """
        get the maximum element
        :return: max element
        """
        return self.max_data[0]


if __name__ == '__main__':
    queue = [2, 3, 4, 2, 6, 2, 5, 1]
    so = Queue()
    so.push(queue[0])
    print(so.max())
    so.push(queue[1])
    print(so.max())
    so.push(queue[2])
    print(so.max())
    so.push(queue[3])
    print(so.max())
    so.push(queue[4])
    print(so.max())
    so.push(queue[5])
    print(so.max())
    so.push(queue[6])
    print(so.max())
    so.push(queue[7])
    print(so.max())
