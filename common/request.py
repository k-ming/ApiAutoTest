# -*- coding: utf-8 -*-#
2
3  #------------------------------------
4  # Name:         request
5  # Description:  
6  # Author:       17621158197
7  # Date:         2019/9/10
8  #------------------------------------

import requests, json


class Connect():
    def get(self, url, params, headers):
        r = requests.get(url, params=params, headers=headers)
        # return r
        r = json.loads(r.text)
        print(url, r)
    def post(self, url, params, headers):
        r = requests.post(url, params=params, headers=headers)
        # return r
        r = json.loads(r.text)
        # # print(r.get('value').get('token'))
        print(url, r)


if __name__ == '__main__':
    C1 = Connect()
    C1.post('http://api.robot.aiyunshen.com/robot/login/userLogin', {'userName':'admin', 'password':'admin123456'}, {'Accept': 'application/json, text/plain, */*'})