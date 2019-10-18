# -*- coding: utf-8 -*-#
2
3  #------------------------------------
4  # Name:         readConfig
5  # Description:  
6  # Author:       17621158197
7  # Date:         2019/9/16
8  #------------------------------------

import os
import configparser, codecs
import re

pd = os.path.join(os.path.split(os.path.realpath(__file__))[0], os.path.pardir)
cp = os.path.join(pd, "config\cfg.ini")


class Read():
    def __init__(self):
        fd = open(cp, 'rb+')
        data = fd.read()

        #  使用codecs模块进行文件操作及消除文件中的BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(cp, "rb+")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(cp)

    def getApi (self, module, name):
        v = self.cf.get(module, name)
        v = re.split('\n', v)
        s = []
        for i in v:
            r = i.lstrip('123456789')
            s.append(r)
        return s


if __name__ == '__main__':
    R1 = Read()
    print (R1.getApi('INFO', 'headers'))
