# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 11:53
# @Author  : Li Sen

"""
// 面试题12：矩阵中的路径
// 题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有
// 字符的路径。路径可以从矩阵中任意一格开始，每一步可以在矩阵中向左、右、
// 上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入
// 该格子。例如在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字
// 母用下划线标出）。但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个
// 字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
// A B T G
// C F C S
// J D E H
"""
import unittest


# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        """
        :param matrix: 输入的矩阵
        :param rows: 矩阵的行数
        :param cols: 矩阵的列数
        :param path: 要寻找的path
        :return: 
        """
        # write code here
        if not matrix or rows < 0 or cols < 0 or path == None:
            return False
        markmatrix = [0] * (rows * cols)
        pathIndex = 0

        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathIndex, markmatrix):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathIndex, markmatrix):
        """
        
        :param matrix: 输入的矩阵
        :param rows: 矩阵行数
        :param cols: 矩阵列数
        :param row: 当前行
        :param col: 当前列
        :param path: 要寻找的path
        :param pathIndex: 查询到第index个字符
        :param markmatrix: mark为已经走过 
        :return: 
        """
        if pathIndex == len(path):  # 如果pathIndex的长度与path一致，则找到对应的路径
            return True
        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] == path[pathIndex] and not \
                markmatrix[row * cols + col]:  # 当矩阵行数，列数符合条件，且矩阵上该点存在且等于路径上的那一点，且未被走过
            pathIndex += 1  # 路径移到下一个点
            markmatrix[row * cols + col] = True  # 将刚刚走过的这点mark一下
            # 判断该点的上下左右是否满足
            hasPath = self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathIndex, markmatrix) or \
                      self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathIndex, markmatrix) or \
                      self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathIndex, markmatrix) or \
                      self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathIndex, markmatrix)
            if not hasPath:  # 如果上下左右仍未找到对应的点
                pathIndex -= 1  # 回到上一步
                markmatrix[row * cols + col] = False  # 回退之后，走过的路mark为false
        return hasPath


class TestSolution(unittest.TestCase):
    def test1(self):
        matrix = 'ABTGCFCSJDEH'
        string = 'BFCE'
        rows = 3
        cols = 4
        solution = Solution()
        expected = True
        self.assertEqual(expected, solution.hasPath(matrix, rows, cols, string))

    def test2(self):
        matrix = 'ABCESFCSADEE'
        string = 'SEE'
        rows = 3
        cols = 4
        solution = Solution()
        expected = True
        self.assertEqual(expected, solution.hasPath(matrix, rows, cols, string))

    def test3(self):
        matrix = 'ABTGCFCSJDEH'
        string = 'ABFB'
        rows = 3
        cols = 4
        solution = Solution()
        expected = False
        self.assertEqual(expected, solution.hasPath(matrix, rows, cols, string))

    def test4(self):
        matrix = 'ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS'
        string = 'SLHECCEIDEJFGGFIE'
        rows = 5
        cols = 8
        solution = Solution()
        expected = True
        self.assertEqual(expected, solution.hasPath(matrix, rows, cols, string))

    def test5(self):
        matrix = 'ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS'
        string = 'SGGFIECVAASABCEHJIGQEM'
        rows = 5
        cols = 8
        solution = Solution()
        expected = True
        self.assertEqual(expected, solution.hasPath(matrix, rows, cols, string))

    def test6(self):
        matrix = 'ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS'
        string = 'SGGFIECVAASABCEEJIGOEM'
        rows = 5
        cols = 8
        solution = Solution()
        expected = False
        self.assertEqual(expected, solution.hasPath(matrix, rows, cols, string))

    def test7(self):
        matrix = 'ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS'
        string = 'SGGFIECVAASABCEHJIGQEMS'
        rows = 5
        cols = 8
        solution = Solution()
        expected = False
        self.assertEqual(expected, solution.hasPath(matrix, rows, cols, string))

    def test8(self):
        matrix = 'AAAAAAAAAAAA'
        string = 'AAAAAAAAAAAA'
        rows = 3
        cols = 4
        solution = Solution()
        expected = True
        self.assertEqual(expected, solution.hasPath(matrix, rows, cols, string))

    def test9(self):
        matrix = 'AAAAAAAAAAAA'
        string = 'AAAAAAAAAAAAA'
        rows = 3
        cols = 4
        solution = Solution()
        expected = False
        self.assertEqual(expected, solution.hasPath(matrix, rows, cols, string))

    def test10(self):
        matrix = 'A'
        string = 'A'
        rows = 1
        cols = 1
        solution = Solution()
        expected = True
        self.assertEqual(expected, solution.hasPath(matrix, rows, cols, string))

    def test11(self):
        matrix = 'A'
        string = 'B'
        rows = 1
        cols = 1
        solution = Solution()
        expected = False
        self.assertEqual(expected, solution.hasPath(matrix, rows, cols, string))

    def test12(self):
        matrix = ''
        string = ''
        rows = 0
        cols = 0
        solution = Solution()
        expected = False
        self.assertEqual(expected, solution.hasPath(matrix, rows, cols, string))


if __name__ == '__main__':
    unittest.main()
