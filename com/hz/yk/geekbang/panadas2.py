import pandas as pd
from pandas import Series, DataFrame, np

data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])

print(df1)
print(df2)
# 删除列
df2 = df2.drop(columns=['Chinese'])
print(df2)
# 删除行
df2 = df2.drop(index=['ZhangFei'])
print(df2)
# 重命名列名
df2.rename(columns={'Chinese': 'YuWen', 'English': 'Yingyu'}, inplace=True)
print(df2)
# 更改数据格式
df2['Chinese'].astype(np.int64)

# 全部大写
df2.columns = df2.columns.str.upper()
# 全部小写
df2.columns = df2.columns.str.lower()
# 首字母大写
df2.columns = df2.columns.str.title()

df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
# 一次性输出多个指标
print(df1.describe())
