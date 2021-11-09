import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

queen_list = collection.find_one({'name': "Mike"})
print(type(queen_list))
print(queen_list)

results = collection.find({'age': 20})
# 返回结果是 Cursor 类型，它相当于一个生成器，我们需要遍历取到所有的结果，其中每个结果都是字典类型。
print(results)
for queen_list in results:
    print(queen_list)

# 查询年龄大于 20 的数据,这里查询的条件键值已经不是单纯的数字了，而是一个字典，其键名为比较符号 $gt，意思是大于，键值为 20
results = collection.find({'age': {'$gt': 20}})
print(results)
# 使用 $regex 来指定正则匹配
results = collection.find({'name': {'$regex': '^M.*'}})
print(results)
count = collection.find().count()
print(count)

# skip() 方法偏移几个位置，比如偏移 2，就忽略前两个元素，得到第三个及以后的元素
# 用 limit() 方法指定要取的结果个数
results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([queen_list['name'] for queen_list in results])

# 在数据库数量非常庞大的时候，如千万、亿级别，最好不要使用大的偏移量来查询数据，因为这样很可能导致内存溢出。此时可以使用类似如下操作来查询
collection.find({'_id': {'$gt': ObjectId('5d8035bdee73e9af8176f8e4')}})
