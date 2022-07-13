# JSON/OBJECT/DICT are same
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")

mydb = myclient["Project_X"]

details ={
    "Name":"giri",
    "Age":20,
    "address":{
        "street":"Kuravanka",
        "DoorNo":"2-2"
    },
    "Hobbies":{
        "indoor":["chess","carron"],
        "outdoor":["cricket","kabadi"]
    },
    "phone_numbers":[8106882928,9949399999]
}
# database[collection].insert_one(custom_data)
if not mydb["users"].find_one({"Name":details.get("Name")}):
    mydb["users"].insert_one(details)
    print(details.get("Name"), "successfully created")
else:
    print(details.get("Name")," is already available in DB")
