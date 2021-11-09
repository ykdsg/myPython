d = {'mike': 10, 'lucy': 2, 'ben': 30}

queen_list = sorted(d, key=lambda x: x[1], reverse=True)
print(type(queen_list))
print(queen_list)
