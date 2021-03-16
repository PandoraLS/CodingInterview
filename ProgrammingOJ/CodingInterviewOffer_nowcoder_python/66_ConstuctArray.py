# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/13 10:07

class Solution:
    def multiply(self, A):
        # write code here
        head = [1]
        tail = [1]
        for i in range(len(A) - 1):
            head.append(A[i] * head[i])
            tail.append(A[-i - 1] * tail[i])
            
        # print(head)
        # print(tail)
        return [head[j] * tail[-j - 1] for j in range(len(head))]


if __name__ == '__main__':
    A = [1,2,3,4,5]
    so = Solution()
    print(so.multiply(A))