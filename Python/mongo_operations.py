from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")


mydb = myclient["Test"]

'''mydict ={
    "name":"kiran",
    "id":"1111111"
}
'''

sa={
  "Name":"vinay",
    "id":"1234"
}
x = mydb["Users"].insert_one(sa)


'''y = mydb["Users"].find_one({"id":"1111111"})
print(y)
'''


