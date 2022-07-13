# # # # # # # class Parent(object):
# # # # # # #     x = 1
# # # # # # # class Child1(Parent):
# # # # # # #     pass
# # # # # # # class Child2(Child1):
# # # # # # #     pass
# # # # # # # print(Parent.x, Child1.x, Child2.x)
# # # # # # # # 1,1,1
# # # # # # # Child1.x = 2
# # # # # # # print(Parent.x, Child1.x, Child2.x)
# # # # # # # # 1,2,2
# # # # # # # Parent.x = 3
# # # # # # # # 1,3,3
# # # # # # # print(Parent.x, Child1.x, Child2.x)
# # # # # #
# # # # # # inp="aaaabbbccc"
# # # # # # js = {}
# # # # # # for each in inp:
# # # # # #     if each not in js:
# # # # # #         js[each]=inp.count(each)
# # # # # # st = ""
# # # # # # for each in js:
# # # # # #     st +=each+str(js[each])
# # # # # # print(st)
# # # # #
# # # # # def prime_num(num):
# # # # #     factor = False
# # # # #     if num > 1:
# # # # #         for i in range(2,num):
# # # # #             if (num%i) == 0:
# # # # #                 factor = True
# # # # #                 break
# # # # #     print("prime")
# # # # #     return factor
# # # # #
# # # # # def dec_fun(func):
# # # # #     response = func(10)
# # # # #     print(response,"decorator")
# # # # #
# # # # # dec_fun(func=prime_num())
# # # # # # def list_primes(range):
# # # # # #     ls = []
# # # # # #     i = 2
# # # # # #     while(len(ls)!=range):
# # # # # #         if not prime_num(i):
# # # # # #             ls.append(i)
# # # # # #         i+=1
# # # # # #     print(ls)
# # # # # # list_primes(10)
# # # # #
# # # # # # inp ="numIsPrime"
# # # # # # op ="num_is_prime"
# # # # # # x = "numIsPrime"
# # # # # # inds = []
# # # # # # for ind,each in enumerate(inp):
# # # # # #     if each.isupper():
# # # # # #         inds.append(ind)
# # # # # # for ind,each in inp:
# # # # # #     if ind in inds:
# # # # # #
# # # # #
# # # #
# # # # #db.collection.find({condition}).sort({"_id":-1}).skip(10).limit(10)
# # # #
# # # #
# # # #
# # # # query =[
# # # # {
# # # #         "$lookup":{
# # # #             "from":"src_collection",
# # # #             "localField":"name",
# # # #             "foriegnField":"Name",
# # # #             "as":"output"
# # # #         }
# # # #     },
# # # #     {
# # # #     "$match":{"name":"kiran"}
# # # # },
# # # # {
# # # #     "$group":{
# # # #         "marks":"$marks",
# # # #         "total":{
# # # #             "$sum":"$total"
# # # #         }
# # # #     }
# # # # },
# # # #     {
# # # #         "$sort":{
# # # #             "name":"1"
# # # #         }
# # # #     },
# # # #     {
# # # #         "$limit":10
# # # #     }
# # # # ]
# # #
# # # ls = [1,2,3]
# # #
# # # class Node:
# # #     def __init__(self,dataval):
# # #         value = ""
# #
# # # Input1=[(21,5),(31,1),(4,4)]
# # # output = [(31,1),(4,4),(21,5)]
# # #
# # # def fun1(inp):
# # #     for i in range(0,len(inp)):
# # #         for j in range(0,len(inp)-i-1):
# # #             if (inp[j][1] > inp[j+1][1]):
# # #                 temp = inp[j]
# # #                 inp[j]=inp[j+1]
# # #                 inp[j+1]=temp
# # #     print(inp)
# # # fun1((Input1))
# #
# #
# # # inpu = "ab"
# # # def fun1(inp):
# # #     b_occurance = False
# # #     state = True
# # #     for each in inp:
# # #         if each == "b":
# # #             b_occurance=True
# # #         elif each == "a" and b_occurance:
# # #             state = False
# # #     print(state)
# # #     return state
# # # fun1(inpu)
# # var = "Online Python - IDE, Editor, Compiler, Interpreter"
# #
# #
# # js = {each: len(each) for each in var.replace(",","").split(" ") if each.isalnum()}
#
# # ls = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# # count =10
# # print(ls[-count:])
# #
# # for each in ls:
# #     if each%2==0:
# #         print(each)
# #
# # ls1 = [each for each in ls if each%2==0]
# # print(ls1)
# #
# # files_location = {
# #     "basepath_details":{"logs_path":"","src_path":"","tests_path":""},
# #     "files":{
# #         "testing_file1":{
# #             "basepath":"logs_path",
# #         }
# #     }
# # }
# #
# # sr = "Anand"
# #
# # print(sr.swapcase())
#
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/getSlots")
# def get_slots():
#     return {"s1":"details"}
#
# # if __name__ == "__main__":
# app.run()

# st = "My Name is XyZ"
#
# x = lambda s : [z for z in st if z.isupper()]
#
# # y = [z for z in st if z.isupper()]
#
# print(x(st))

r = 4
c = 4
matrix= [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15,16]
]

# def fun1(rows,cols,mat):
#     st_row_index = 0
#     st_col_index = 0
#     while (st_row_index<rows) and (st_col_index<cols):
#         for ele in range(st_col_index,cols):
#             print(mat[st_row_index][ele])
#         st_row_index += 1
#         for ele in range(st_row_index,rows):
#             print(mat[ele][cols-1])
#         cols -= 1
#         if st_row_index < rows:
#             for each in range(cols,st_col_index):
#                 print(mat[rows][each])
#             rows -= 1



# fun1(r,c,matrix)


ls = [89 , 67 , 34, 2, 4 , 1 , 100 , 99 , 1000 , 788]

for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        if ls[i] > ls[j]:
            ls[i],ls[j]=ls[j],ls[i]
print(ls)