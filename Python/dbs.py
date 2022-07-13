from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")

mydb = myclient["pydbs"]
'''
ka ={
    "Name":"vinay.1",
    "id":"123456"
}'''

'''a = mydb["py"].insert_one(ka)'''

y = mydb["py"].find_one({"id":"1234"})
print(y)
