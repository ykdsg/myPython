import numpy as np

# 定义结构数组
persontype = np.dtype({
    'names': ['name', 'age', 'chinese', 'math', 'english', 'total'],
    'formats': ['S32', 'i', 'i', 'i', 'f', 'f']})
# 在定义数组的时候，用 array 中指定了结构数组的类型 dtype=persontype
peoples = np.array([("ZhangFei", 32, 75, 100, 90, 0), ("GuanYu", 24, 85, 96, 88.5, 0),
                    ("ZhaoYun", 28, 85, 92, 96.5, 0), ("HuangZhong", 29, 65, 85, 100, 0)],
                   dtype=persontype)
peoples[:]['total'] = peoples[:]['chinese'] + peoples[:]['english'] + peoples[:]['math']
ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))
print(peoples[:]['total'])

# 用sorted函数进行排序
ranking = sorted(peoples, key=lambda x: x['total'], reverse=True)
print(ranking)
