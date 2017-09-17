import xlrd

MAX_ROWS = 1625

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


def find_chanhoufangshi(bianhao_find):
    data = xlrd.open_workbook('桃姐表格0603/产后访视.xls')
    table = data.sheets()[0]
    nrows = table.nrows
    print(nrows)
    for i in range(nrows):
        if i > 1:
            row_data = table.row_values(i)
            bianhao = row_data[0]
            yisheng = row_data[3]
            riqi = row_data[2]
            name = row_data[1]

            if str(bianhao) == bianhao_find:
                print(bianhao, bianhao_find, yisheng, riqi, len(row_data))
                return [bianhao, yisheng, riqi, name]
    return None


def write_zongbiao_fangshi():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet0')

    data = xlrd.open_workbook('桃姐表格0603/基本公共卫生服务222_1.xls')
    table = data.sheets()[0]
    header_length = 1
    nrows = table.nrows
    for i in range(nrows):
        if header_length - 1 < i < MAX_ROWS:
            row_data = table.row_values(i)
            bianhao = str(row_data[1])
            finded = find_chanhoufangshi(bianhao)
            print(i, bianhao, finded)
            if not finded:
                finded = ['', '', '', '']
            ws.write(i - header_length, 0, finded[2])
            ws.write(i - header_length, 1, finded[1])
            ws.write(i - header_length, 2, finded[3])

    wb.save('chanhoufangshi.xls')


def find_chanhou42(bianhao_find):
    data = xlrd.open_workbook('桃姐表格0603/产后42天(1).xls')
    table = data.sheets()[0]
    nrows = table.nrows
    print(nrows)
    for i in range(nrows):
        if i > 1:
            row_data = table.row_values(i)
            bianhao = row_data[0]
            yisheng = row_data[3]
            riqi = row_data[2]
            name = row_data[1]

            if str(bianhao) == bianhao_find:
                print(bianhao, bianhao_find, yisheng, riqi, len(row_data))
                return [bianhao, yisheng, riqi, name]
    return None


def write_zongbiao_chanhou42():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet0')

    data = xlrd.open_workbook('桃姐表格0603/基本公共卫生服务222_1.xls')
    table = data.sheets()[0]
    header_length = 1
    nrows = table.nrows
    for i in range(nrows):
        if header_length - 1 < i < MAX_ROWS:
            row_data = table.row_values(i)
            bianhao = str(row_data[1])
            finded = find_chanhou42(bianhao)
            print(i, bianhao, finded)
            if not finded:
                finded = ['', '', '', '']
            ws.write(i - header_length, 0, finded[2])
            ws.write(i - header_length, 1, finded[1])
            ws.write(i - header_length, 2, finded[3])

    wb.save('chanhou42.xls')


def find_wanyun(bianhao_find):
    data = xlrd.open_workbook('桃姐表格0603/综合查询_复诊导出.xls')
    table = data.sheets()[0]
    nrows = table.nrows
    for i in range(nrows):
        if i > 1:
            row_data = table.row_values(i)
            yunzhou = float(row_data[3])
            bianhao = row_data[0]
            yisheng = row_data[4]
            riqi = row_data[2]
            name = row_data[1]

            if 28 < yunzhou and str(bianhao) == bianhao_find:
                print(bianhao, bianhao_find, yunzhou, yisheng, riqi, len(row_data))
                return [bianhao, yunzhou, yisheng, riqi, name]
    return None


def write_zongbiao_wanyun():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet0')

    data = xlrd.open_workbook('桃姐表格0603/基本公共卫生服务222_1.xls')
    table = data.sheets()[0]
    header_length = 1
    nrows = table.nrows
    for i in range(nrows):
        if header_length - 1 < i < MAX_ROWS:
            row_data = table.row_values(i)
            bianhao = str(row_data[1])
            finded = find_wanyun(bianhao)
            print(i, bianhao, finded)
            if not finded:
                finded = ['', '', '', '', '']
            ws.write(i - header_length, 0, finded[2])
            ws.write(i - header_length, 1, finded[3])
            ws.write(i - header_length, 2, finded[4])

    wb.save('wanyun.xls')


def find_zhongyun(bianhao_find):
    data = xlrd.open_workbook('桃姐表格0603/综合查询_复诊导出.xls')
    table = data.sheets()[0]
    nrows = table.nrows
    for i in range(nrows):
        if i > 1:
            row_data = table.row_values(i)
            yunzhou = float(row_data[3])
            bianhao = row_data[0]
            yisheng = row_data[4]
            riqi = row_data[2]
            name = row_data[1]

            if 13 <= yunzhou <= 28 and str(bianhao) == bianhao_find:
                print(bianhao, bianhao_find, yunzhou, yisheng, riqi, len(row_data))
                return [bianhao, yunzhou, yisheng, riqi, name]
    return None


def write_zongbiao_zhongyun():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet0')

    data = xlrd.open_workbook('桃姐表格0603/基本公共卫生服务222_1.xls')
    table = data.sheets()[0]
    header_length = 1
    nrows = table.nrows
    for i in range(nrows):
        if header_length - 1 < i < MAX_ROWS:
            row_data = table.row_values(i)
            bianhao = str(row_data[1])
            finded = find_zhongyun(bianhao)
            print(i, bianhao, finded)
            if not finded:
                finded = ['', '', '', '', '']
            ws.write(i - header_length, 0, finded[2])
            ws.write(i - header_length, 1, finded[3])
            ws.write(i - header_length, 2, finded[4])

    wb.save('zhongyun.xls')


def find_zaoyun(bianhao_find):
    data = xlrd.open_workbook('桃姐表格0603/初诊记录(1).xls')
    table = data.sheets()[0]
    nrows = table.nrows
    for i in range(nrows):
        if i > 2:
            row_data = table.row_values(i)
            yunzhou = float(row_data[4])
            bianhao = row_data[0]
            yisheng = row_data[5]
            name = row_data[1]
            riqi = row_data[6]
            if yunzhou < 13 and str(bianhao) == bianhao_find:
                print(bianhao, bianhao_find, yunzhou, yisheng, riqi, len(row_data))
                return [bianhao, yunzhou, yisheng, riqi, name]
    return None


def write_zongbiao_zaoyun():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet0')

    header_length = 1
    data = xlrd.open_workbook('桃姐表格0603/基本公共卫生服务222_1.xls')
    table = data.sheets()[0]
    nrows = table.nrows
    for i in range(nrows):
        if header_length - 1 < i < MAX_ROWS:
            row_data = table.row_values(i)
            bianhao = str(row_data[1])
            finded = find_zaoyun(bianhao)
            print(i, bianhao, finded)
            if not finded:
                finded = ['', '', '', '', '']
            ws.write(i - header_length, 0, finded[2])
            ws.write(i - header_length, 1, finded[3])
            ws.write(i - header_length, 2, finded[4])

    wb.save('桃姐表格0603/zaoyun.xls')


def change_zongbiao():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet0')

    header_length = 1
    data = xlrd.open_workbook('桃姐表格0603/基本公共卫生服务222_1.xls')
    table = data.sheets()[0]
    nrows = table.nrows
    for i in range(nrows):
        if header_length - 1 < i < MAX_ROWS:
            row_data = table.row_values(i)
            base_col_length = 9
            for j in range(base_col_length):
                ws.write((5 * (i - header_length)), j, row_data[j])
            for k in range(5):
                ws.write((5 * (i - header_length)) + k, base_col_length + 0, row_data[3 * k + base_col_length + 0])
                ws.write((5 * (i - header_length)) + k, base_col_length + 1, row_data[3 * k + base_col_length + 1])
                ws.write((5 * (i - header_length)) + k, base_col_length + 2, row_data[3 * k + base_col_length + 2])

    wb.save('桃姐表格0603/zong.xls')


if __name__ == "__main__":
    # handle_chuzhe('42112611401901003')
    # write_zongbiao_zaoyun()
    # write_zongbiao_zhongyun()
    # write_zongbiao_wanyun()
    # write_zongbiao_chanhou42()
    # write_zongbiao_fangshi()
    change_zongbiao()
