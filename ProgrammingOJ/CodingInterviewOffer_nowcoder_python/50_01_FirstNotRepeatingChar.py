# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/6 14:55


# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
# 题解：https://www.nowcoder.com/questionTerminal/1c82e8cf713b4bbeb2a5b31cf5b0417c
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) <= 0 or len(s) > 10000:
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
                break

    def FirstNotRepeatingChar2(self, s):
        # write code here
        if len(s) <= 0 or len(s) > 10000:
            return -1
        # 建立哈希表,字符长度为8的数据类型,共有256种可能,于是创建一个长度为256的列表
        ls = [0] * 256
        
        # 遍历字符串,下标为ASCII值,值为次数
        for i in s:
            ls[ord(i)] += 1
            
        # 遍历列表,找到出现次数为1的字符并输出位置
        for j in s:
            if ls[ord(j)] == 1:
                return s.index(j)
                break


if __name__ == '__main__':
    ss = 'abaccdeff'
    so = Solution()
    print(so.FirstNotRepeatingChar(ss))
    print(so.FirstNotRepeatingChar2(ss))
