# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/6 11:39

# 题解：https://www.nowcoder.com/profile/806133/codeBookDetail?submissionId=12114507
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        uglyList = [1]
        indexTwo = 0
        indexThree = 0
        indexFive = 0

        for i in range(index - 1):
            newUgly = min(uglyList[indexTwo] * 2, uglyList[indexThree] * 3, uglyList[indexFive] * 5)
            uglyList.append(newUgly)  # 将三个uglyList[index]中的最小值append上来，保证uglyList.append是有序增加的
            
            # 如果当前newUgly能被2/3/5整除，那么将对应的index+1，向后推进
            if newUgly % 2 == 0: indexTwo += 1
            if newUgly % 3 == 0: indexThree += 1
            if newUgly % 5 == 0: indexFive += 1
        return uglyList[-1]


if __name__ == '__main__':
    index = 10
    so = Solution()
    print(so.GetUglyNumber_Solution(index))
