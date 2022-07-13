import random
import string
from pymongo import MongoClient

client = MongoClient(host="localhost",port=27017)

def insert_multiple_docs(count):
    docs = []
    for i in range(count):
        string1 = ''.join(random.choices(string.ascii_uppercase +
                                         string.digits, k=7))
        doc = {
            "id":random.randint(1,10000000),
            "name":string1,
            "age":random.randint(1,100),
            "phone_num":random.randint(6000000000,9999999999)
        }
        docs.append(doc)
    client["Application_production_db1"]["users"].insert_many(docs)
    print("Inserted Successfully")
    return True
insert_multiple_docs(100)
