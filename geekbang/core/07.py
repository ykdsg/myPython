d = {'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}
# 迭代的是键
for k in d:
    print("key:" + k)

for v in d.values():
    print("value:", v)

for it in d.items():
    print("item:", it)

l = [1, 2, 3, 4, 5, 6, 7]
for index in range(0, len(l)):
    if index < 5:
        print(l[index])

text = ' Today, is, Sunday'
text_list = [s.strip() for s in text.split(",") if len(s.strip()) > 3]
print(text_list)

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
          ['mike', '1999-01-01', 'male'],
          ['nancy', '2001-02-01', 'female']
          ]

result = []
for va in values:
    dic = {}
    for i in range(0, len(attributes)):
        dic[attributes[i]] = va[i]
    result.append(dic)

print(result)

result2 = [{attributes[i]: va[i] for i in range(len(attributes))} for va in values]
print(result2)
