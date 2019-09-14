# -*- coding: utf-8 -*-
# @Time: 2019/9/13 17:48
# @Author: Li Sen

# 面试题3：数组中重复的数据
# 题目一：在一个长度为n的数组里的所有数字都在0到n-1的范围内。
# 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
# 请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

# 以牛客网写法为主
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate1(self, numbers, duplication):
        # write code here
        if numbers == None or len(numbers) <= 1:
            return False
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
                return False

        numbers.sort()
        for i in range(len(numbers) - 1):
            if numbers[i] == numbers[i + 1]:
                duplication[0] = numbers[i]  #
                print(duplication[0])
                return True
        return False

    def duplicate2(self, numbers, duplication):
        if numbers == None or len(numbers) <= 1:
            return False
        usedDic = set()
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
                return False
            if numbers[i] not in usedDic:
                usedDic.add(numbers[i])
            else:
                duplication[0] = numbers[i]
                print(duplication[0])
                return True
        return False

    def duplicate3(self, numbers, duplication):
        if numbers == None or len(numbers) <= 1:
            return False
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
                return False

        for i in range(len(numbers)):
            while (numbers[i] != i):
                if numbers[i] == numbers[numbers[i]]:  # 如果第i个数等于i
                    duplication[0] = numbers[i]
                    print(duplication[0])
                    return True
                else:
                    temp = numbers[i]
                    numbers[i] = numbers[temp]
                    numbers[temp] = temp
        return False


if __name__ == "__main__":
    print("03_01")
    Array = [2, 3, 1, 0, 2, 5, 3]
    Dup = [0]  # Dup先定义为一个长度为1的数组，用来存储第一个重复的数字
    print("方法1--------------------")
    print(Solution().duplicate1(Array, Dup))

    print("方法2--------------------")
    print(Solution().duplicate2(Array, Dup))

    print("方法3--------------------")
    print(Solution().duplicate3(Array, Dup))
