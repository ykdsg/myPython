# 极客时间 https://time.geekbang.org/column/article/76307

import pandas as pd
from pandas import DataFrame
import numpy as np

df = DataFrame(pd.read_excel('./accountMessage.xlsx'))
# 列名标注
# df.columns = ['Index', 'Num', 'Name', 'Age', 'Weight']
df.rename(columns={0: 'Num', 1: 'Name', 2: 'Age', 3: 'Weight'}, inplace=True)
# print(df.columns)
# print(df)

# 删除空行
# df.dropna(how='all', inplace=True)
# 下面两种方式都可以按条件删除空行，使用drop 删除和使用loc筛选
df = df.drop(df[(df['Age'].isna()) & (df['Name'].isna())].index)
# df = df.loc[(df['Age'].notna()) & (df['Name'].notna())]
print(df)
print("================================")
# print(type(df['Name']))
# print(df['Age'].isna())

# 统一单位
# 获取 weight 数据列中单位为 lbs 的数据
rows_with_lbs = df['Weight'].str.contains('lbs').fillna(False)
print(df[rows_with_lbs])
# 将 lbs转换为 kgs, 2.2lbs=1kgs
for i, lbs_row in df[rows_with_lbs].iterrows():
    # 截取从头开始到倒数第三个字符之前，即去掉lbs。
    weight = int(float(lbs_row['Weight'][:-3]) / 2.2)
    df.at[i, 'Weight'] = '{}kgs'.format(weight)

# print(df['Weight'])

# 用最高频的数据进行填充，可以先通过 value_counts 获取 Age 字段最高频次 age_maxf，然后再对 Age 字段中缺失的数据用 age_maxf 进行填充
age_maxf = df['Age'].value_counts().index[0]
df['Age'].fillna(age_maxf, inplace=True)
# 对 df[‘Age’]中缺失的数值用平均年龄进行填充
df['Age'].fillna(df['Age'].mean(), inplace=True)

# 切分名字，删除源数据列
df[['first_name', 'last_name']] = df['Name'].str.split(expand=True)
df.drop('Name', axis=1, inplace=True)

# 删除非 ASCII 字符
df['first_name'].replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)
df['last_name'].replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)

# 删除重复数据行
df.drop_duplicates(['first_name', 'last_name'], inplace=True)
print(df)
