# -*- coding: utf-8 -*-#
2
3  #------------------------------------
4  # Name:         configRW
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