[toc]
# ApiAutoTest
python 接口自动化 ddt数据驱动
## 目录说明
### `case`  测试用例目录  
#### xls格式的测试用例
![用例模板apidata.xlsx](http://b-ssl.duitang.com/uploads/item/201604/14/20160414132207_5Fvjs.jpeg)
### `common`    脚本目录  
    color.txt   单元格颜色码  
    configRW.py 读写.ini文件  
    readXlsx.py 读.xls文件  
    request.py  接口请求  
    Run.py  运行测试用例  
    writeXlsx   写.xls文件  
### `config`  配置文件目录  
![配置文件模板defaul.ini]()
### `report`    测试报告目录
![测试报告模板report-2019-11-05-1.xls]()
## 脚本说明
`request.py`  
```python  
# -*- coding: utf-8 -*-#
2
3  # ------------------------------------
4  # Name:         request
5  # Description:  
6  # Author:       lenvo
7  # Date:         2019/9/10
8  # ------------------------------------
import requests, json
''' request.py 使用python3的requests类封装了get和post方法，并返回请求结果
'''

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

# if __name__ == '__main__':
    # post('http://api.robot.aiyunshen.com/robot/login/userLogin', {'Accept': 'application/json, text/plain, */*'}, {'userName':'admin', 'password':'admin123456'})
    # get('http://52.80.169.157:8090/ask', '', {'q':'带我去梦境','mall_code':'1000000001'})  
```
`readXlsx.py`
```python
# -*- coding: utf-8 -*-#
2
3  #------------------------------------
4  # Name:         readXslx
5  # Description:  
6  # Author:       lenvo
7  # Date:         2019/10/17
8  #------------------------------------

import xlrd

class ReadXlsx():

    def read(self,sheet):
        data = []
        file  = xlrd.open_workbook('../cases/apidata.xlsx')
        table =  file.sheet_by_name(sheet)
        if (table.nrows > 1):
            for i in range(1, table.nrows):
                data.append(table.row_values(i))  # 将每一行的数据都存入list
            return tuple(data)  # 将list 转化为元组后返回
        else: print('book is empty!')

# if __name__=='__main__':
#     R1 = ReadXlsx()
#     print(R1.read('Sheet1'))
```
`writeXlsx.py`  
```python 
# -*- coding: utf-8 -*-#
2
3  #------------------------------------
4  # Name:         writeXlsx
5  # Description:  
6  # Author:       lenvo
7  # Date:         2019/10/26
8  #------------------------------------

import xlwt, xlrd
from xlutils.copy import copy

# 创建title style
style1 = xlwt.easyxf("""
       font:
           name '等线',
           height 450 ,
           bold on;
       align:
           vert center,
           horiz center;
   """)

# 创建total style
style2 = xlwt.easyxf('''
       font:
           name '等线',
           height 220;
       pattern:
           pattern solid,
           fore-colour 0x17; 
       align:
           vert center;
   ''')

# 创建success style
style3 = xlwt.easyxf('''
       font:
           name '等线',
           height 220;
       pattern:
           pattern solid,
           fore-colour 0x0C;
       align:
           vert center;
   ''')

# 创建Fail style
style4 = xlwt.easyxf('''
       font:
           name '等线',
           height 220;
       pattern:
           pattern solid,
           fore-colour 0x0A;
        align:
            vert center;
   ''')

# 创建字段名 style
style5 = xlwt.easyxf('''
       font:
           name '等线',
           height 220;
       align:
           vert center;
   ''')

# 创建时间 style
style6 = xlwt.easyxf('''
       font:
           name '等线',
           height 220;
       align:
           horiz right;
   ''')

def writeBook(bookName, title, time):
    '''
    :param bookName: 工作薄名称
    :param title: 标题
    :param time: 创建时间
    :return: 无返回值
    '''
    # 创建工作薄，工作表对象
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('Sheet1', cell_overwrite_ok=True)  # 第二个参数意思是单元格内容可以复写

    # 合并单元格
    sheet.write_merge(0, 1, 0, 6, title, style1)
    sheet.write_merge(2, 2, 0, 6, time, style6)
    sheet.write(3, 0, 'total', style2)
    sheet.write(3, 1, '', style2)
    sheet.write(3, 2, 'success', style3)
    sheet.write(3, 3, '', style3)
    sheet.write(3, 4, 'fail', style4)
    sheet.write(3, 5, '', style4)
    sheet.write(4, 0, 'name', style5)
    sheet.write(4, 2, 'response', style5)
    sheet.write(4, 4, 'expect', style5)
    sheet.write(4, 6, 'status', style5)

    # 设置行高
    sheet.row(0).set_style(xlwt.easyxf('font:height 720'))  # 36pt
    sheet.row(2).set_style(xlwt.easyxf('font:height 450'))
    sheet.row(3).set_style(xlwt.easyxf('font:height 450'))
    sheet.row(4).set_style(xlwt.easyxf('font:height 450'))

    # 设置列宽
    sheet.col(0).width = 256 * 14  # 256为衡量单位，20表示20个字符宽度
    sheet.col(2).width = 256 * 14

    # 创建工作薄
    workbook.save(bookName + '.xls')


def writeContent(bookName, num, apiName, response, expect, status, total, success, failure):
    rbook = xlrd.open_workbook(bookName+'.xls', formatting_info=True)  # 打开文件，并且保留原格式
    workbook = copy(rbook)  # 使用xlutils的copy方法使用打开的excel文档创建一个副本
    sheet = workbook.get_sheet(0)  # 使用get_sheet方法获取副本要操作的sheet
    '''写入接口请求情况
    '''
    sheet.write_merge(num, num, 0, 1)
    sheet.write(num, 0, apiName)
    sheet.write_merge(num, num, 2, 3)
    sheet.write(num, 2, response)
    sheet.write_merge(num, num, 4, 5)
    sheet.write(num, 4, expect)

    ''' 根据请求结果，设置单元格颜色
    '''
    if status == 'pass':
        sheet.write(num, 6, status)
    elif status == 'fail':
        sheet.write(num, 6, status, style4)
    else:
        sheet.write(num, 6, status, style4)
    sheet.row(num).set_style(xlwt.easyxf('font:height 350'))  # 设置结果单元的行高

    ''' 写入用例执行总数，成功，失败的条数
    '''
    sheet.write(3, 1, total, style2)
    sheet.write(3, 3, success, style3)
    sheet.write(3, 5, failure, style4)
    workbook.save(bookName + '.xls')

# if __name__ == '__main__':
    # writeBook('report', '机器人接口自动化测试报告', '\'2019-10-26 16:58:20')
    # writeContent('report', 6, '管理员登陆失败', '{"status":403007,"message":"密码不正确","timestamp":1572178740846}', 403007.0, 'pass',1,1,0)
```
`configRW.py`
```python
# -*- coding: utf-8 -*-#
2
3  #------------------------------------
4  # Name:         self.configRW
5  # Description:
6  # Author:       lenvo
7  # Date:         2019/11/1
8  #------------------------------------

import datetime as dt
import configparser

'''本脚本用于读取和修改配置文件
'''

config = configparser.ConfigParser()  # 创建对象
class DefaultCfg():
    def __init__(self):
        global config
        config.read('../config/default.ini', encoding='utf-8')  # 读取配置文件

    def getSecs(self):  # 获取所有节点
        return config.sections()

    def getOption(self, section):  # 获取指定节点的所有key
        return config.options(section)


    def getItem(self, item):  # 获取指定节点的所有key & value
        return config.items(item)

    def getKeyVal(self, section, key):  # 获取指定节点指定key 的 value
        return config.get(section, key)

    def getProperty(self, section, key):  # 获取指定节点指定key 的属性，必须是int型
        return config.getint(section, key)

    def hasSection(self, section):   # 检查指定节点是否存在，返回True或False
        return config.has_section(section)

    def hasKey(self, section, key):  # 检测指定节点是否存在key， 返回True或False
        return config.has_option(section, key)

    def addSection(self, section):  # 增加节点
        config.add_section(section)   # 添加一个节点名section, 此时添加的节点section尚未写入文件
        config.write(open('../config/default.ini', 'w'))  # 将添加的节点section写入配置文件

    def delSection(self, section):  # 删除节点
        config.remove_section(section)  # 删除一个节点名section, 此时section尚未删除
        config.write(open('../config/default.ini', 'w'))  # 保存删除

    def addKeyVal(self, section, key, val):  # 在已经存在的节点中添加键值对
        config.set(section, key, val)
        config.write(open('../config/default.ini', 'w'))




# if __name__ == '__main__':
#     today = dt.datetime.now().strftime('%Y-%m-%d')
#     D1 = DefaultCfg()
#     if D1.hasSection('build'):
#         if D1.hasKey('build', today):
#             tv = D1.getKeyVal('build', today)
#             D1.addKeyVal('build', today, str(int(tv)+1))
#         else:
#             D1.addKeyVal('build', today, '1')
#     else:
#         D1.addSection('build')
#         D1.addKeyVal('build', today, '1')
```
`Run.py`
```python
# -*- coding: utf-8 -*-#
2
3  # ------------------------------------
4  # Name:         Run
5  # Description:  
6  # Author:       lenvo
7  # Date:         2019/10/17
8  # ------------------------------------

import unittest
from ddt import ddt, data, unpack
from common.readXlsx import ReadXlsx
from common import request, writeXlsx
import ast, json
import datetime as dt
from common.configRW import DefaultCfg


total = 0
success = 0
failure = 0
e = ''



@ddt
class Run(unittest.TestCase):
    d = ReadXlsx().read('Sheet1')

    @data(*d)
    @unpack
    def test_run(self, value1, value2, value3, value4, value5, value6, value7, value8, value9):
        """  headers 和 parameters 必须使用 ast.literal_eval(value)函数转化为dict才能使用，为空的时候转化会报错，所以要做判断
        :param value1: title
        :param value2: host
        :param value3: path
        :param value4: method
        :param value5: headers
        :param value6: parameters
        :param value7: expect
        """
        '''
        将参数转化为字典时，需要加判断，如果不为空在转化，否则会抛出异常
        '''
        if value5 and value6:
            value5 = ast.literal_eval(value5)
            value6 = ast.literal_eval(value6)
        elif value5:
            value5 = ast.literal_eval(value5)
        elif value6:
            value6 = ast.literal_eval(value6)
        else:
            pass

        '''
        判断请求方法,统计用例执行情况
        '''
        global total
        global success
        global failure

        if value4 == 'post':
            r = request.post(value2 + value3, value5, value6)
            total = total+1
            try:
                self.assertEqual(int(value7), eval(value8), msg='校验失败！')  #做assertEqual验证时，需要加上try expect,否则出错后，后面的用例无法执行
                result = 'pass'      # 用例验证通过，用例状态设为pass, 成功次数加1
                success = success + 1
                writeXlsx.writeContent('../reports/report-' + today + '-' + D1.getKeyVal('build', today), int(value9)+4, value1, '', value7, result, total, success, failure)
            except AssertionError as e:
                result = 'fail'   # 用例验证失败，用例状态设为fail, 失败次数加1
                failure = failure + 1
                writeXlsx.writeContent('../reports/report-' + today + '-' + D1.getKeyVal('build', today), int(value9)+4, value1, str(e), value7, result, total, success, failure)
        elif value4 == 'get':
            r = request.get(value2 + value3, value5, value6)
            total = total + 1
            try:
                self.assertEqual(int(value7), eval(value8), msg='校验失败！')
                result = 'pass'
                success = success + 1
                writeXlsx.writeContent('../reports/report-' + today + '-' + D1.getKeyVal('build', today), int(value9)+4, value1, '', value7, result,total, success, failure)
            except AssertionError as e:
                result = 'fail'
                failure = failure + 1
                writeXlsx.writeContent('../reports/report-' + today + '-' + D1.getKeyVal('build', today), int(value9)+4, value1, str(e), value7, result,total, success, failure)
        else:
            pass

if __name__ == '__main__':
    currentTime = dt.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
    
''' 调用DefaultCfg类，来创建和读取今日执行用例次数，并对测试报告命名
'''
    today = dt.datetime.now().strfming'mingtime('%Y-%m-%d')
    D1 = DefaultCfg()
    if D1.hasSection('build'):
        if D1.hasKey('build', today):
            tv = D1.getKeyVal('build', today)
            D1.addKeyVal('build', today, str(int(tv) + 1))
        else:
            D1.addKeyVal('build', today, '1')
    else:
        D1.addSection('build')
        D1.addKeyVal('build', today, '1')
    
''' writeXlsx.writeBook()方法须在此处调用，才能首次创建文件
'''
    writeXlsx.writeBook('../reports/report-' + today + '-' + D1.getKeyVal('build', today), '机器人接口自动化测试报告', currentTime)
    unittest.main(verbosity=1)
```



