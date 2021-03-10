# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 10:28
# @Author  : Li Sen

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        else:
            return min(rotateArray)

    def minNumberInRotateArray2(self, rotateArray):
        if not rotateArray:
            return 0
        else:
            rotateArray.sort()
            return rotateArray[0]

    def minNumberInRotateArray3(self, rotateArray):
        # write code here
        """
        解题思路：> 数组旋转后，分为两部分，前半部分大于等于后半部分（考虑非严格递增的情况）
        > 将index1初始化为第一个数字，index2初始化为最后一个数字，mid初始化为第一个数字（应对旋转0个元素的情况）
        > 如果index1与index2相邻，此时index2即为所求
        > 如果遇到的index1、index2以及indexMid指向的三个数字相等，就无法二分查找，只能遍历数组了
        > 如果mid指向的数字大于等于index1指向的数字，那么mid 在数组一中，下一步，将index1往mid挪，指向mid
        > 如果mid指向的数字小于等于index2指向的数字，那么mid 在数组二中，下一步，将index2往mid挪，指向mid
        :param rotateArray: 
        :return: 
        """
        if not rotateArray:
            return 0
        if len(rotateArray) == 0:
            return 0
        index1 = 0
        index2 = len(rotateArray) - 1
        indexMid = index1
        while (rotateArray[index1] >= rotateArray[index2]):
            if (index2 - index1 == 1):  # 如果index2与index1相邻，则index2对应的即为所求
                indexMid = index2
                break
            indexMid = (index1 + index2) // 2
            # 如果下标index1、index2以及index3的数值相等，就只能遍历了
            if (rotateArray[index1] == rotateArray[index2] and rotateArray[index1] == rotateArray[indexMid]):
                return self.minValue(rotateArray, index1, index2)
            if (rotateArray[indexMid] >= rotateArray[index1]):
                index1 = indexMid
            elif (rotateArray[indexMid] <= rotateArray[index2]):
                index2 = indexMid
        return rotateArray[indexMid]

    def minValue(self, rotateArray, index1, index2):
        result = rotateArray[index1]
        for i in range(index1 + 1, index2 + 1):
            if result > rotateArray[i]:
                result = rotateArray[i]
        return result


if __name__ == '__main__':
    array = [3, 4, 5, 1, 2]
    a = Solution()
    print(a.minNumberInRotateArray(array))
    print(a.minNumberInRotateArray2(array))
    print(a.minNumberInRotateArray3(array))
