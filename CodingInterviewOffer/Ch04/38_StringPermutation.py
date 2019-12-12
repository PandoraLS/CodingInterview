# -*- coding: utf-8 -*-
# @Time    : 2019/12/12 18:34
# @Author  : Li Sen

# 
# 链接：https://www.nowcoder.com/questionTerminal/fe6b651b66ae47d7acce78ffdd9a96c7
# 来源：牛客网

import itertools


class Solution:
    def Permutation(self, ss):
        # TODO 该方法较为复杂，不是很理解
        if len(ss) <= 1:
            return ss
        res = set()
        # 遍历字符串，固定第一个元素，第一个元素可以取a,b,c...，然后递归求解
        for i in range(len(ss)):
            # a = ss[:i]
            # aa = ss[i + 1:]
            # aaa = a + aa
            # print(a, '+', aa, '=', aaa)
            for j in self.Permutation(ss[:i] + ss[i + 1:]):  # 依次固定了元素，其他的全排列（递归求解）
                # print('ss[i]:', ss[i], '+', 'j:', j, ' = ', ss[i] + j, '....')
                res.add(ss[i] + j)  # 集合添加元素的方法add(),集合添加去重（若存在重复字符，排列后会存在相同，如baa,baa）
        return sorted(res)  # sorted()能对可迭代对象进行排序,结果返回一个新的list

    def Permutation2(self, ss):
        # write code here
        result = []
        if not ss:
            return []
        else:
            res = itertools.permutations(ss)
            for i in res:
                if "".join(i) not in result:
                    result.append("".join(i))
        return result

    def Permutation3(self, ss):
        """
        解题思路：把字符串看成两部分：第一部分是它的第一个字符；第二部分是后面的所有字符。 递归
        :param ss: 
        :return: 
        """
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return list(ss)
        pStr = []
        charlist = list(ss)
        charlist.sort()

        for i in range(len(charlist)):
            if i > 0 and charlist[i] == charlist[i - 1]:
                continue
            temp = self.Permutation(''.join(charlist[:i]) + ''.join(charlist[i + 1:]))
            for j in temp:
                pStr.append(charlist[i] + j)
        return pStr


if __name__ == '__main__':
    string = 'abcd'
    so = Solution()
    print(so.Permutation(string))
    print(so.Permutation2(string))
    print(so.Permutation3(string))
