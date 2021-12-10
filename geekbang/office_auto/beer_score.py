import re
from pathlib import PurePath
from re import Pattern
from typing import List

import xlrd
import xlwt
from xlrd import sheet
from xlrd.sheet import Sheet
from xlwt import Worksheet


class Beer:
    def __init__(self, name: str, beer_type: str, price: float, score: float):
        self.name = name
        self.beer_type = beer_type
        self.price = round(price, 2)
        self.score = score
        self.unit_score = calc_unit_score(price, score)

    def get_unit_score(self) -> float:
        return self.unit_score

    def __repr__(self):
        return 'name:' + self.name + " price:" + str(self.price) + " score:" + str(self.score) + " unit_score:" + str(
            self.unit_score) + ";"


def calc_unit_score(price: float, score: float) -> float:
    if price <= 0:
        return -999999
    # 4分是分水岭，用来筛掉价格很低的3.x 对结果的影响
    result_pre = round(score * 100 - 400, 0)

    weighted_score = result_pre

    if result_pre > 0:
        # 取小数点后的数字进行权重计算，比如分数是4.21 ，这里的权重就是2.1
        weighted = round(result_pre / 10, 2)
        # 2的 "权重"次方，这样高价和高分之间能够相互平衡，因为在4分之后每提升0.1分都是更加艰难的。
        weighted_score = pow(2, weighted)

    return round(weighted_score / price * 100, 2)


def read_file(file_source: str):
    work_book = xlrd.open_workbook(file_source, formatting_info=True)
    table: Sheet = work_book.sheet_by_index(0)

    re_score_pattern1 = re.compile(r'Untappd.*?([0-9]*\.[0-9]+|[0-9]+)')
    re_score_pattern2 = re.compile(r'Un评分.*?([0-9]*\.[0-9]+|[0-9]+)')
    re_score_pattern3 = re.compile(r'UT.*?([0-9]*\.[0-9]+|[0-9]+)')
    re_patterns: List[Pattern] = []
    re_patterns.append(re_score_pattern1)
    re_patterns.append(re_score_pattern2)
    re_patterns.append(re_score_pattern3)

    beers: List[Beer] = []
    for line in range(3, table.nrows):
        hidden = table.rowinfo_map[line].hidden
        if hidden:
            continue

        name = table.cell(line, 2).value
        beer_type = table.cell(line, 1).value
        price_str = table.cell(line, 6).value
        try:
            price = float(price_str) if price_str else 0.0
        except:
            price = 0.0

        score = 0.0
        score_str = table.cell(line, 8).value

        for pattern in re_patterns:
            if pattern.match(score_str):
                score = float(pattern.match(score_str).group(1))
            else:
                continue

        # 这里过滤下拿不到价格的，以及低于4分的
        if price != 0:
            beer = Beer(name, beer_type, price, score)
            beers.append(beer)

    return beers


def write_to_file(beers: List[Beer]):
    workbook = xlwt.Workbook(encoding='utf-8')
    xlsheet: Worksheet = workbook.add_sheet("排名")
    table_heads = ('名称', '类型', '价格', '分数', '单价分数',)
    col = 0
    for head in table_heads:
        xlsheet.write(0, col, head)
        col += 1

    row = 1
    for beer in beers:
        xlsheet.write(row, 0, beer.name)
        xlsheet.write(row, 1, beer.beer_type)
        xlsheet.write(row, 2, beer.price)
        xlsheet.write(row, 3, beer.score)
        xlsheet.write(row, 4, beer.unit_score)
        row += 1

    workbook.save(PurePath(original_file).with_name('beer-sort').with_suffix('.xls'))


# 识别行是否隐藏，只支持xls
original_file = "/Users/ykdsg/Downloads/beer-12.06.xls"
if __name__ == '__main__':
    beers = read_file(original_file)
    beers.sort(key=lambda beer: beer.unit_score, reverse=True)
    # print(beers)
    write_to_file(beers)
    print('done')
