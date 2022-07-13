from pymongo import MongoClient

client = MongoClient(host="localhost",port=27017)

# syntax client[db][collection_name].insert_fun({object to insert})

record_to_insert = {
    "name":"anand",
    "age":30
}

client["Application_production_db1"]["users"].insert_one(record_to_insert)

client["Application_production_db1"]["users"].find_one(record_to_insert)
#
# client["Application_production_db1"]["users"].update_one({})


# client["Application_production_db1"]["users"].delete_one(delete_condition)