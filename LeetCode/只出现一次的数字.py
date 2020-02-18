# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/18 16:24
# 编程之美 习题1.5 说明：http://www.voidcn.com/article/p-gasydxbz-es.html

class Solution:
    def singleNumber(self, nums):
        res = 0
        for n in nums:
            res ^= n
        return res

    def twoNumber(self, nums):
        # 两个死机（备份的不是同一个文件）
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


if __name__ == '__main__':
    so = Solution()
    nums = [2, 2, 1]
    print(so.singleNumber(nums))
    nums2 = [1, 5, 3, 4, 2, 3, 1, 5, 4, 6]
    print(so.twoNumber(nums2))
