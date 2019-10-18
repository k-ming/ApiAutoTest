# -*- coding: utf-8 -*-#
2
3  #------------------------------------
4  # Name:         request
5  # Description:  
6  # Author:       17621158197
7  # Date:         2019/9/10
8  #------------------------------------

import requests, json


def get(url, headers, params):
    r = requests.get(url, headers=headers, params=params)
    # return r
    r = json.loads(r.text)
    print(url, r)


def post(url, headers, params):
    r = requests.post(url, headers=headers, params=params)
    # return r
    r = json.loads(r.text)
    # # print(r.get('value').get('token'))
    print(url, r)





# if __name__ == '__main__':
#     post('http://api.robot.aiyunshen.com/robot/login/userLogin', {'Accept': 'application/json, text/plain, */*'}, {'userName':'admin', 'password':'admin123456'})