import pandas as pd
from pandas import Series, DataFrame, np

df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
df2 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2': range(5)})
# 基于 name 这列进行连接
df3 = pd.merge(df1, df2, on='name')
print(df3)
# inner 内链接是 merge 合并的默认情况，inner 内连接其实也就是键的交集，在这里 df1, df2 相同的键是 name，所以是基于 name 字段做的连接
df3 = pd.merge(df1, df2, how='inner')

# 左连接/右连接
df3 = pd.merge(df1, df2, how='left')
# 外连接相当于求两个 DataFrame 的并集
df3 = pd.merge(df1, df2, how='outer')
print(df3)
