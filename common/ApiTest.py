# -*- coding: utf-8 -*-#
2
3  #------------------------------------
4  # Name:         ApiTest
5  # Description:  
6  # Author:       17621158197
7  # Date:         2019/9/18
8  #------------------------------------
from common.readConfig import Read
from common import request
import ast

host = ''
class ApiTest():
    global token
    def __init__(self):
        pass
    def test(self):
        R1 = Read()
        global host
        host = R1.getApi('INFO', 'host')
        paths = R1.getApi('INFO', 'path')
        methods = R1.getApi('INFO', 'method')
        params = R1.getApi('INFO', 'params')
        headers = R1.getApi('INFO', 'headers')

        for i in range(0, len(paths)):
            # 此处必须取出来的参数转化为dict
            data = ast.literal_eval(params[i])
            header = ast.literal_eval(headers[i])
            if methods[i] == 'get':
                request.get(str(host[0])+paths[i], data, header)
            elif methods[i] == 'post':
                print(type(host[0]+paths[i]))
                print(type(data))
                print(type(header))

                request.post(str(host[0])+paths[i], data, header)
            else: pass


if __name__ == '__main__':
    A1 = ApiTest()
    A1.test()