# -*- coding: utf-8 -*-#
2
3  #------------------------------------
4  # Name:         Run
5  # Description:  
6  # Author:       17621158197
7  # Date:         2019/10/17
8  #------------------------------------

import unittest
from ddt import ddt, data, unpack
from common.readXlsx import ReadXlsx
from common import request

r = request.Connect()


@ddt
class Run(unittest.TestCase, request):

    d = ReadXlsx.read('Sheet1')
    @data(*d)
    @unpack
    def run(self, value1, value2, value3, value4, value5):
        if (value3 == 'get'):
            # r.get(value1+value2, value4, value5)
            print(value1+value2, value4, value5)
        elif (value3 == 'post'):
            # r.post(value1+value2, value4, value5)
            print(value1 + value2, value4, value5)
        else:pass

if __name__=='__main__':
    Run.run()
