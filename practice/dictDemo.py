dict1 = {"1": 1, "2": 2}
dict2 = {"3": 3, "4": 4}

dictAll3 = dict1 + dict2

dictAll = dict(list(dict1.items()) + list(dict2.items()))
dictAll2 = {**dict1, **dict2}

print(dictAll)
print(dictAll2)
