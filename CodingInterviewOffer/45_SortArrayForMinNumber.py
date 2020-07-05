# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/5 14:22

class Solution:
    def PrintMinNumber(self, numbers):
        if numbers == []:
            return ""
        else:
            PermutationList = self.Permutation(numbers)
            return min(PermutationList)

    def Permutation(self, numbers):
        # write code here
        if not numbers:
            return ""
        if len(numbers) == 1:
            return numbers
        new_numbers = []
        numbers.sort()
        Min = numbers[0]

        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left = numbers[:i]
            right = numbers[i + 1:]
            lr = left + right
            temp = self.Permutation(lr)
            for j in temp:
                new_numbers.append(int(str(numbers[i]) + str(j)))
        return new_numbers


if __name__ == '__main__':
    numbers = [1, 23, 456]
    so = Solution()
    print(so.PrintMinNumber(numbers))
