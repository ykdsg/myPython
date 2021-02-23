import pandas as pd
from pandas import DataFrame

df = DataFrame(pd.read_excel('./foodInformation.xlsx'))
# 干掉有问题的行
df.drop(df[df['ounces'] < 0].index, inplace=True)
# print(df)

# 填充空值
df['ounces'].fillna(df['ounces'].mean(), inplace=True)
# print(df)

print('-------------------')
df['food'] = df['food'].str.lower()
# 删除重复数据行
# df.drop_duplicates(['food', 'animal'], inplace=True)

# 查找food重复的记录，分组求其平均值
d_rows = df[df['food'].duplicated(keep=False)]
print(d_rows)
g_items = d_rows.groupby('food').mean()
print(g_items.index)
g_items['food'] = g_items.index
print(g_items)
#
# # 遍历将重复food的平均值赋值给df
# for i, row in g_items.iterrows():
#     df.loc[df.food == row.food, 'ounces'] = row.ounces
# print(df)
