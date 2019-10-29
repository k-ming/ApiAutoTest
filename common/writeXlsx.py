# -*- coding: utf-8 -*-#
2
3  #------------------------------------
4  # Name:         writeXlsx
5  # Description:  
6  # Author:       17621158197
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
