Details =[
    {"Name":"G kiran Kumar","DOB":"18-Dec-1994","Gender":"Male",
"Qulification":"B.Tech",
"Address":{
    "Door Number":"2-256-4-H1",
    "Street Name":"Soceity Colony ring road",
    "City Name":"Madanapalle",
     "District":"Chittoor",
     "State":"Andhra Pradesh",
     "Pincode":"517325"
},
"Hobbies":{
    "Indoor":{"chess",
              "carron"},
    "Outdoor":{"Cricket",
               "kabbadi",
               "shettle"},
},
"Phone Numbers":[8106882928,6301717489]
}
]



print(Details[0].get("Name"))
print(Details.get("Address").get("Street Name"))
print(Details.get("Hobbies").get("Outdoor"))
# for ind,each in enumerate(Details.get("Hobbies").get("Outdoor")):
#     print(each)
#     if ind == 1:
#         break
#
# for each in (Details.get("Hobbies").get("Outdoor")):
#     print(each)
#     break
#
#
#
#

# list1 = [
#     {'subject1': "java", 'marks': 98},
#     {'subject2': "PHP", 'marks': 89},
#     1,
#     2,
#     "a",
#     "b",
#     [1, 2, 3],
#     ["8", 9, "7"],
#     {34, 87, 90},
#     (1, 2)
# ]
#
#
# for i in list1:
#     if type(i)==str:
#         print(i)
#     elif type(i)==dict:
#         print(i)
#     else:
#         print("")
#



# for x in list1:
#     print(x)
#     if type(x) == dict:
#         print(x.get('subject1'))
#         print(x.get("subject2"))

# x=[12,1,3,4,5,"hello"]
# for i in x:
#     print(i)
#     if type(i)==str:
#         print(i)