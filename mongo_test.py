from pymongo import MongoClient

client=MongoClient('127.0.0.1',27017)

db = client.test

students = db.Student.find()

for s in students:
    print(s)
