import pandas as pd

data = {'Chinese': [66, 95, 93, 90, 80, 80], 'English': [65, 85, 92, 88, 90, 90],
        'Math': [None, 98, 96, 77, 90, 90]}
df = pd.DataFrame(data, index=['张飞', '关羽', '赵云', '黄忠', '典韦', '典韦'],
                  columns=['English', 'Math', 'Chinese'])

df = df.drop_duplicates()
print(df)
# 列名重新排序
cols = ['Chinese', 'English', 'Math']
df = df.filter(cols, axis=1)
print(df)

df['Total'] = df.sum(axis=1)
print(df.describe())

# 对空值的数据进行补全，这里是用的平均值
df['Math'].fillna(df['Math'].mean(), inplace=True)
print(df)
