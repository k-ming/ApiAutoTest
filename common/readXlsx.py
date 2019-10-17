# -*- coding: utf-8 -*-#
2
3  #------------------------------------
4  # Name:         readXslx
5  # Description:  
6  # Author:       17621158197
7  # Date:         2019/10/17
8  #------------------------------------

import xlrd



class ReadXlsx():

    def read(self,sheet):
        data = []
        file  = xlrd.open_workbook('../cases/apidata.xlsx')
        print(file)
        table =  file.sheet_by_name(sheet)
        if (table.nrows > 1):
            for i in range(1, table.nrows):
                data.append(table.row_values(i))
            return tuple(data)
        else: print('book is empty!')

# if __name__=='__main__':
#     R1 = ReadXlsx()
#     print(R1.read('Sheet1'))
