# -*- coding: utf-8 -*-#
2
3  #------------------------------------
4  # Name:         DDTTest
5  # Description:  
6  # Author:       17621158197
7  # Date:         2019/10/17
8  #------------------------------------

import unittest
from ddt import ddt, data, unpack
from common.readXlsx import ReadXlsx

@ddt
class Deamo(unittest.TestCase):

    # @data(1,2,3)
    # def test_sign(self, value):
    #     print(value)
    #
    # @data((1,2),(2,3))
    # @unpack
    # def test_double(self,value1, value2):
    #     print(value1, value2)
    #
    # @data(['a', 'b', 'c'], [1, 2, 3])
    # @unpack
    # def test_array(self, value1, value2, value3):
    #     print(value1, value2, value3)
    #
    # @data({'name':'king','age':28, 'sex':'F'})
    # @unpack
    # def test_dic(self, name, age, sex):
    #     print(name, age, sex)

    d = ReadXlsx().read('Sheet1')

    @data(*d)
    @unpack
    def test_large(self,value1, value2, value3, value4, value5):
        if value3 == 'post':
            print(value1+value2, value4, value5)


if __name__ == '__main__':
    unittest.main()