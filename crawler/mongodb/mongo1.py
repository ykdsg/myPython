import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
# 已经不推荐使用，需要使用insert_one
queen_list = collection.insert(student)
print(queen_list)

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
queen_list = collection.insert_many([student1, student2])
print(queen_list)
print(queen_list.inserted_ids)
