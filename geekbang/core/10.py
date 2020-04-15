d = {'mike': 10, 'lucy': 2, 'ben': 30}

result = sorted(d, key=lambda x: x[1], reverse=True)
print(type(result))
print(result)
