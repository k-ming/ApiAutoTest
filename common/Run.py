# -*- coding: utf-8 -*-#
2
3  # ------------------------------------
4  # Name:         Run
5  # Description:  
6  # Author:       17621158197
7  # Date:         2019/10/17
8  # ------------------------------------

import unittest
from ddt import ddt, data, unpack
from common.readXlsx import ReadXlsx
from common import request
import ast


@ddt
class Run(unittest.TestCase):
    d = ReadXlsx().read('Sheet1')

    @data(*d)
    @unpack
    def test_run(self, value1, value2, value3, value4, value5):
        if value3 == 'get' and value4 and value5:
            request.get(value1 + value2, ast.literal_eval(value4), ast.literal_eval(value5))
        elif value3 == 'get' and value4:
            request.get(value1 + value2, ast.literal_eval(value4), value5)
        elif value3 == 'get' and value5:
            request.get(value1 + value2, value4, ast.literal_eval(value5))
        elif value3 == 'get':
            request.get(value1 + value2, value4, value5)

        elif value3 == 'post' and value4 and value5:
            request.post(value1 + value2, ast.literal_eval(value4), ast.literal_eval(value5))
        elif value3 == 'post' and value4:
            request.post(value1 + value2, ast.literal_eval(value4), value5)
        elif value3 == 'post' and value5:
            request.post(value1 + value2, value4, ast.literal_eval(value5))
        elif value3 == 'post':
            request.post(value1 + value2, value4, value5)
        else:
            pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
