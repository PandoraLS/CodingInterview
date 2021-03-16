# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/28 22:29
import random
# 洗牌法
class Solution:

    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original
        self.original = list(self.original) # 变动original和array则另一个也会跟着变
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array

if __name__ == '__main__':
    nums = [1,2,3]
    obj = Solution(nums)
    print(obj.reset())
    print(obj.shuffle())
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()