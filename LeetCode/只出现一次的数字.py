# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/18 16:24
# 编程之美 习题1.5 说明：http://www.voidcn.com/article/p-gasydxbz-es.html
from functools import reduce
import math


class Solution:
    def singleNumber(self, nums):
        res = 0
        for n in nums:
            res ^= n
        return res

    def twoNumber(self, nums):
        # 两个死机（备份的不是同一个文件），思路三
        res = 0
        for n in nums:
            res ^= n  # 先全部异或，其结果是这两个只出现一次的数字的异或 
        num1 = res  # 临时保存res，此时res=A^B,num1=A^B
        k = 0  # k表示的是:a和b在第k位不同
        while ((res & 1) == 0):  # 我们在结果数字中找到第一个为1的位的位置，记为第k位
            res >>= 1
            k += 1
        res = num1  # res=A^B
        for n in nums:
            if (n >> k) & 1:
                # 把num1=A^B与（第k位为1的因子[假设为A]全部亦或，当然也包括A）
                # 得到num1=B
                num1 ^= n
        num2 = num1 ^ res  # 将(num1=B)与(res=A^B)亦或，得到num2=A
        return num1, num2

    def twoNumber2(self, nums, sum_nums, product_nums):
        """
        # 思路四，两个机器同时坏掉（两个ID可以相同也可以不同）
        :param nums: 输入的list
        :param sum_nums: 总输入list的求和（包含缺失项）
        :param product_nums: 总输入list的（包含缺失项）
        :return: 返回所求的两个坏机器的ID
        """
        a = sum_nums - sum(nums)  # a是所有的减去缺失的两个 x + y = a
        b = product_nums / reduce(lambda x, y: x * y, nums)
        # b是缺失的两项的积 x*y = b，使用乘积形式可能会导致数过大，可以将b这个换成各个平方之和，依然可以求解出x,y
        # 联立方程组可以求得num1和num2
        x = (math.sqrt(a * a - 4 * b) + a) / 2
        y = b / x
        return x, y


if __name__ == '__main__':
    so = Solution()
    nums = [2, 2, 1]
    print(so.singleNumber(nums))
    nums2 = [1, 5, 3, 4, 2, 3, 1, 5, 4, 6]
    print(so.twoNumber(nums2))

    # 思路4 
    nums2 = [1, 5, 3, 4, 2, 3, 1, 5, 4, 6]  # 2和6各缺失一项
    nums2_sum_nums = sum(nums2) + 2 + 6
    nums2_product_nums = reduce(lambda x, y: x * y, nums2) * 2 * 6
    print(so.twoNumber2(nums2, nums2_sum_nums, nums2_product_nums))

    nums3 = [1, 5, 3, 4, 3, 1, 5, 4]  # 假设缺失的是两个2，nums3中的编号均为正数
    nums3_sum_nums = sum(nums3) + 2 + 2  # 
    nums3_product_nums = reduce(lambda x, y: x * y, nums3) * 2 * 2
    print(so.twoNumber2(nums3, nums3_sum_nums, nums3_product_nums))
