# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 15:07
# @Author  : Li Sen

"""
09题扩展，两个队列实现栈
"""
'''
<分析>：
入栈：将元素进队列A
出栈：判断队列A中元素的个数是否为0，0说明队列A中最后一个元素已经pop
当队列A的长度不为1时，将队列A中的元素依次输送到队列B中，直到队列A只剩1个元素
此时将队列A与队列B互换，则队列B为只有一个元素的队列，该元素即为要出栈的元素
pop该元素即可。
'''

class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, node):
        self.queue1.insert(0, node)

    def pop(self):
        if not self.queue1: # 如果A空，队列A中无元素，此时return None
            return None

        while len(self.queue1) != 1:
            self.queue2.insert(0, self.queue1.pop())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.pop()


if __name__ == '__main__':
    node1 = 'a'
    node2 = 'b'
    node3 = 'c'
    CStack = Solution()
    CStack.push(node1)
    CStack.push(node2)
    CStack.push(node3)
    print(CStack.pop())
    print(CStack.pop())
    print(CStack.pop())
