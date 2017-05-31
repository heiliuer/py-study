import xlrd


def getZhongYun(id):
    print(id)
    pass


import xlwt
from datetime import datetime


def write():
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                         num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    ws.write(0, 0, 1234.56, style0)
    ws.write(1, 0, datetime.now(), style1)
    ws.write(2, 0, 1)
    ws.write(2, 1, 1)
    ws.write(2, 2, xlwt.Formula("A3+B3"))

    wb.save('example.xls')


def find_fuzhen():
    data = xlrd.open_workbook('基本公共卫生服务(1).xls')
    table = data.sheets()[0]
    nrows = table.nrows


if __name__ == "__main__":
    data = xlrd.open_workbook('基本公共卫生服务(1).xls')
    table = data.sheets()[0]
    nrows = table.nrows
    write()
    for i in range(nrows):
        row_data = table.row_values(i)
        getZhongYun(row_data[1])
        print()
