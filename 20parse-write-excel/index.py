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


def handle_chuzhe():
    data = xlrd.open_workbook('初诊记录(1).xls')
    table = data.sheets()[0]
    nrows = table.nrows
    for i in range(nrows):
        row_data = table.row_values(i)
        yunzhou = float(row_data[50])
        bianhao = int(row_data[0])
        yisheng = row_data[148]
        riqi = row_data[149]
        if yunzhou <= 12:
            print(bianhao, yunzhou, yisheng, riqi, len(row_data))
            print(row_data)
        for j, data in enumerate(row_data):
            if str(data).find('尿H') > -1:
                pass
        print()


if __name__ == "__main__":
    handle_chuzhe()
