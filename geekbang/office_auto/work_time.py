import datetime
import time
from pathlib import PurePath

import xlrd
import xlwt


# 时间处理
# s1 = '09:59'
# s2 = '21:27'  # for example
# FMT = '%H:%M'
# tdelta = datetime.datetime.strptime(s2, FMT) - datetime.datetime.strptime(s1, FMT)
# print(tdelta)

class Worker:
    def __init__(self, name: str, wno: str, c_date: str):
        '''

        :param name:
        :param wno: 工号
        :param c_date:  考勤日期
        :param start_time: 上班时间
        :param end_time: 下班时间
        '''
        self.name = name
        self.wno = wno
        self.c_date = c_date
        self.start_time = None
        self.end_time = None

    def getKey(self) -> str:
        return self.wno + "-" + self.c_date

    def __repr__(self):
        return ' '.join('%s' % item for item in self.__dict__.values())

    def getCntList(self):
        '''
        convert to list
        :return:
        '''
        return [self.name, self.wno, self.c_date, self.start_time, self.end_time]


original_file = "/Users/ykdsg/Downloads/work_house-202107.xlsx"


def read_file():
    data = xlrd.open_workbook(original_file)

    table = data.sheets()[0]
    # 取得表头
    # salary_header = table.row_values(rowx=1, start_colx=0, end_colx=None)
    # print(type(salary_header))
    # print(salary_header)
    worker_dict = {}
    for line in range(2, table.nrows):
        name = table.cell(line, 0).value
        wno = table.cell(line, 1).value
        c_date = table.cell(line, 14).value
        worker = Worker(name, wno, c_date)

        c_time = table.cell(line, 15).value
        info = table.cell(line, 20).value
        if worker.getKey() in worker_dict.keys():
            old_worker = worker_dict.get(worker.getKey())
            if info == "签退":
                old_worker.end_time = c_time
            else:
                old_worker.start_time = c_time
        else:
            if info == "签退":
                worker.end_time = c_time
            else:
                worker.start_time = c_time

            worker_dict[worker.getKey()] = worker

    return list(worker_dict.values())


def write_to_file(contents: [str]):
    workbook = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook.add_sheet("考勤")
    row = 0
    for line in contents:
        col = 0
        for cell in line:
            xlsheet.write(row, col, cell)
            col += 1
        row += 1

    workbook.save(PurePath(original_file).with_name('work_houst-formate').with_suffix('.xls'))


if __name__ == '__main__':
    workers = read_file()
    new_content = []
    # 表头
    new_content.append(['姓名', '工号', '考勤日期', '上班时间', '下班时间'])
    for worker in workers:
        new_content.append(worker.getCntList())

    write_to_file(new_content)
    # print(workers)
    # worker = Worker("无争", "45", "2015-06-19")
    # print(worker.getKey())
    # worker.start_time = "2015-05-19"
    # print(worker.start_time)
