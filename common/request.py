# -*- coding: utf-8 -*-#
2
3  # ------------------------------------
4  # Name:         request
5  # Description:  
6  # Author:       17621158197
7  # Date:         2019/9/10
8  # ------------------------------------

import requests, json

def get(url, headers, params):
    r = requests.get(url, headers=headers, params=params)
    # print(json.loads(r.text).get('flag'))
    return r
    r.close()


def post(url, headers, params):
    r = requests.post(url, headers=headers, params=params)
    # print(json.loads(r.text).get('status'))
    return r
    r.close()

if __name__ == '__main__':
    # post('http://api.robot.aiyunshen.com/robot/login/userLogin', {'Accept': 'application/json, text/plain, */*'}, {'userName':'admin', 'password':'admin123456'})
    get('http://52.80.169.157:8090/ask', '', {'q':'带我去梦境','mall_code':'1000000001'})