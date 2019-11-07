# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 11:04
# @Author  : Li Sen

"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""
"""
解题思路：
https://www.nowcoder.com/profile/4991846/codeBookDetail?submissionId=9811452
<分析>：
入队：将元素进栈A
出队：判断栈B是否为空，如果为空，则将栈A中所有元素pop，并push进栈B，栈B出栈；
如果不为空，栈B直接出栈。
"""


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1[len(self.stack1) - 1])
                self.stack1.pop()
        pop = self.stack2[len(self.stack2) - 1]
        self.stack2.pop()
        return pop


if __name__ == '__main__':
    node1 = 'a'
    node2 = 'b'
    node3 = 'c'
    CQueue = Solution()
    CQueue.push(node1)
    CQueue.push(node2)
    CQueue.push(node3)
    print(CQueue.pop())
    print(CQueue.pop())
    print(CQueue.pop())
