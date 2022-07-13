#
# # import speedtest
# # import datetime
# # st = speedtest.Speedtest()
# #
# # print("Checking Download Speed")
# # download_speed = st.download()
# # t = datetime.datetime.now()
# # print(round(download_speed/1024/1024))
# # time = "{hh}:{mm}:{ss}".format(hh=t.hour,mm=t.minute,ss=t.second)
# # # str(t.hour) + str(t.minute) + str(t.second)
# # with open("speed.log","w") as file_var:
# #     file_var.write(str(round(download_speed/1024/1024)) + " , "+ time)
#     # file_var.write(str(round(download_speed/1024/1024)) + " , "+ time)
#
#
# # a=.1
# # b=.1
# # c=.1
# # print(a+b ==.2)
# # print(a+b+c == .3)
# # p=(round(a+b+c, 2))
# # print(p==.3)
#
#
# # for i in range (10):
# #     print(i+1,"Kiran kumar")
# #
# # i=0
# # while i<10:
# #     print(i,"kiran")
# #     i+=1
#
#
# # i=0
# # while i<10:
# #     print(i,"kiran")
# #     if i==5:
# #         break
# #     i+=1
#
#
# # for i in range(10):
# #     print(i,"kiran")
# #     if i==5:
# #         break
# #     print("55555")
#
#
# # i=0
# # while i <= 10:
# #     print(i)
# #     i = i + 1
# #     if i == 5:
# #         continue
# #     print("3456789")
#
#
# # for i in range(10):
# #     print(i,"kiran")
# #     if i==5:
# #         continue
#
# # x=10
# # y=10
# # x = [1,2,3]
# # y = [1,2,3]
# # print(id(x))
# # print(id(y))
# # if x == y:
# #     print("x is equal to y")
# # if x is y:
# #     print("x and y are same obj reference")
# #
#
# # x=10
# # y=10
# # print(id(x))
# # print(id(y))
# from logging import exception
#
#
# #   (Exception Handling Topic) Navin reddy
#
# a=5
# b=2
# k = int(input("Enter a Number"))
# print(k)
# try:
#     print("resource open")
#     print(a/b)
#     k = int(input("Enter a Number"))
#     print(k)
#     # print("resource closed")
# except ZeroDivisionError as e:
#     print("hello,we can't divided a number by zero", e)
# except Exception as e:
#     print("Invali Input")
# except Exception as e:
#     print("Something went wrong")
# finally:
#     print("resource closed")
#
#
#
#
# # (Vinay)
# def div(a,b):
#     try:
#         if a==0 or b==0:
#             print("can't divided by zero")
#         else:
#             print(a/b)
#     except Exception as e:
#         # write error in to log file
#         print("unable to perform division operation")
#     finally:
#         print("This is finally block")
# div(10,0)
#
#
# import xlsxreader
#
# # import multiprocessing
# #
# #
# # def fun(val):
# #     return val ** val
# #
# # with multiprocessing.Pool(3) as process:
# #     print(process.map(fun,[10,20]))
#
#
# # def check_leapyear(year):
# #     if year%4 == 0:
# #         print(year," is a Leap Year")
# #     else:
# #         print(year,"is not a Leap Year")
# #
# # inp = int(input("Enter an Year"))
# # check_leapyear(inp)
#
# dic = {
#     "hobbies":["cricket","chess","football"],
#     "name":"kiran"
# }
#
# # dict["hobbies"]
#
# # for each in dic:
# #     if type(dic.get(each)) == list:
# #         print(dic[each])
#
# # sentence = "My name is Kiran"
# sentence = "aMy name is Kiran"
# out = ""
# for each in sentence:
#     if sentence.count(each)==1:
#         out= each
#         break
# print(out)








#
# def fun1(a,b):
#     try:
#         p = "kiran"
#         x = a + b
#         print(x)
#         y = a - b
#         print(y)
#         z = a * b
#         print(z)
#         d = a / b
#         print(d)
#         f = a + p
#         print(f)
#     except Exception as e:
#         return e
# fun1(20, 10)
#
#
#
# def add_sub(a,b):
#     x=a+b
#     y=a-b
#     return x,y
# result1,result2=add_sub(10,5)
# print(result1,result2)
#
# def add(a,b):
#     x=a+b
#     print(x)
# add(10,20)
#
#
# def fun1(a,b):
#     x=a+b
#     print(x)
# fun1(10,20)
#


# a = 0.1
# b = 0.1
# c = 0.1
# def sum_acc_vals(ac1_val,ac2_val,ac3_val=0):
#
#     return round(ac1_val + ac2_val + ac3_val,2)
#
# print(sum_acc_vals(a,b))
# print(sum_acc_vals(a,b,c))
# print(type(sum_acc_vals(a,b,c)))
# a = 0.1
# b = 0.1
# c = 0.1
#
# x = a+b+c
#
# if x==0.3:
#     print("yes")
# else:
#     print("rashmi")
# admins = ["vinay","rashmi","kiran"] # sequence block
# st = {"rashmi","kiran","vinay"}   #hash data structure
# if "kiran" in admins:
#     print("allow access")
# if "kiran" in st:
#     print("allow access")




import logging

logging.basicConfig(level=logging.DEBUG,filename="test.log",filemode="a",format="%(asctime)s :: %(filename)s :: %(asctime)s :: %(lineno)d :: %(message)s")

logger = logging.getLogger()
def test1():
    logger.debug("This is a debug Message in F1")
    logger.info("This is an Info Message in F1")
    logger.warning("This is a warning Message in F1")
    logger.error("this is an Error Message in F1")
    logger.critical("This is a Highly Critical Message in F1")
# test1()








