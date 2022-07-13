# # a =5
# # b =6
# # a,b = b,a
# #
# #
# #
# # tem = a
# # a = b
# # b = tem
#
# # num = 321
# # reversed_num = 0
# # while num != 0:
# #     digit = num % 10
# #     reversed_num  = reversed_num * 10 + digit
# #     num //= 10
# # print(reversed_num)
#
# # a = '1234'
# # print(str(a)[::-1])
#
# a= "kiran, kumar, hari, Ravi,Jayanth, Vinay, Rajesh, Anand, Ramu"
# print(str(a)[::-1])
#
#
# # import the turtle modules
# import turtle
#
#
# # define the function
# # for triangle
# # def form_tri(side):
# #     for i in range(3):
# #         my_pen.fd(side)
# #         my_pen.left(120)
# #         side -= 10
#
#
# # Forming the window screen
# # tut = turtle.Screen()
# # tut.bgcolor("green")
# # tut.title("Turtle")
# #
# # my_pen = turtle.Turtle()
# # my_pen.color("orange")
# #
# # tut = turtle.Screen()
# #
# # # for different shapes
# # side = 300
# # for i in range(10):
# #     form_tri(side)
# #     side -= 30
#
# # import turtle
# # star = turtle.Turtle()
# # star.right(75)
# # star.forward(100)
# #
# # for i in range(4):
# #     star.right(144)
# #     star.forward(100)
# #
# # turtle.done()

# from pymongo import MongoClient
#
# client = MongoClient(host="localhost",port=27017)
# record = {
#     "name":"anand",
#     "age":40,
#     "percantage":98
# }
# client["db"]["c1"].insert_one(record)

x = [1,2,10,20,30,35]
ls = []
while True:
    val = int(input("Enter a Num: "))
    if val >= 0:
        ls.append(val)
    min_val = 0
    x_val = 0
    y_val = 0
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if ls[i]>ls[j]:
                temp_min_val = ls[i] - ls[j]
            else:
                temp_min_val = ls[j] - ls[i]
            if not min_val:
                min_val = temp_min_val
                x_val,y_val = ls[i],ls[j]
            else:
                if min_val >= temp_min_val:
                    min_val = temp_min_val
                    x_val,y_val = ls[i],ls[j]
    print(ls)
    print(min_val,x_val,y_val)
#[1, 5, 3, 6, 0, 1]
