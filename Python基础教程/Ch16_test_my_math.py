# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 17:48
# @Author  : Li Sen

import unittest, ch16_my_math
from subprocess import Popen, PIPE


class ProducTestCase(unittest.TestCase):
    def testIntegers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = ch16_my_math.product(x, y)
                self.failUnless(p == x * y, 'Integer multiplication failed')

    def testFloats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x / 10.0
                y = y / 10.0
                p = ch16_my_math.product(x, y)
                self.failUnless(p == x * y, 'Float multiplication failed')

    def testWithPyLint(self):
        cmd = 'pylint', '-rn', 'Ch16_my_math'
        pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pylint.stdout.read(), '')


if __name__ == '__main__':
    unittest.main()
