import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

condition = {'name': 'Mike'}
student = collection.find_one(condition)
student['age'] = 25
queen_list = collection.update(condition, student)
print(queen_list)

# 这样可以只更新 student 字典内存在的字段。如果原先还有其他字段，则不会更新，也不会删除。而如果不用 $set 的话，则会把之前的数据全部用 student 字典替换；如果原本存在其他字段，则会被删除。
queen_list = collection.update(condition, {'$set': student})
print(queen_list)

# update() 方法其实也是官方不推荐使用的方法。这里也分为 update_one() 方法和 update_many() 方法，用法更加严格，它们的第二个参数需要使用 $ 类型操作符作为字典的键名
condition = {'name': 'Mike'}
student = collection.find_one(condition)
student['age'] = 26
queen_list = collection.update_one(condition, {'$set': student})
print(queen_list)
print(queen_list.matched_count, queen_list.modified_count)

# 第一条符合条件的数据年龄加 1
condition = {'age': {'$gt': 20}}
queen_list = collection.update_one(condition, {'$inc': {'age': 1}})
print(queen_list)
print(queen_list.matched_count, queen_list.modified_count)
# 将所有符合条件的数据都更新
condition = {'age': {'$gt': 20}}
queen_list = collection.update_many(condition, {'$inc': {'age': 1}})
print(queen_list)
print(queen_list.matched_count, queen_list.modified_count)

# 删除
queen_list = collection.delete_one({'name': 'Kevin'})
print(queen_list)
print(queen_list.deleted_count)
queen_list = collection.delete_many({'age': {'$lt': 25}})
print(queen_list.deleted_count)
