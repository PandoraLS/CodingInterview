# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 23:14
# @Author  : Li Sen

class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        # stack中存入pushV中取出的数据
        stack = []
        while popV:
            # 如果第一个元素相等，那么直接都弹出，根本不用压入栈后再判断
            if pushV and popV[0] == pushV[0]:
                popV.pop(0)
                pushV.pop(0)
            # 如果stack的最后一个元素与popV中第一个元素相等，将两个元素都弹出
            elif stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)

            # 如果pushV中有数据，压入Stack
            elif pushV:
                stack.append(pushV.pop(0))

            # 上面情况都不满足，直接返回False
            else:
                return False
        return True


if __name__ == '__main__':
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    so = Solution()
    print(so.IsPopOrder(pushV, popV))
