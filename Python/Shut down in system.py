# import os
# from trail import fun1
#
#
# def get_input_time():
#     v = input("enter time:")
#     c = v.split(":")
#     if len(c) != 3:
#         print("Please Enter Time in HH:MM:SS format")
#         get_input_time()
#     else:
#         seconds_in_hours = int(c[0]) * 60 * 60
#         seconds_in_min = int(c[1]) * 60
#         seconds = int(c[2])
#         total_seconds = seconds_in_hours + seconds_in_min + seconds
#         print(total_seconds)
#         return total_seconds
#
#
# def restart_machine():
#     restart = input("Do you wish to restart your computer ? (yes / no): ")
#     sec = get_input_time()
#     if restart.lower() == "yes":
#         if min != 0:
#             str1 = "shutdown /r /t " + str(sec)
#         else:
#             str1 = "shutdown /r /t"
#         os.system(str1)
#     elif restart.lower() == "no":
#         print("restart operation cancelled")
#     else:
#         print("Enter Valid Input!!!!!!")
#         # restart_machine()
#
#
# def abort_shutdown():
#     os.system("shutdown /a")
#
#
# # restart_machine()
# # abort_shutdown()
# fun1()

#
# ls = [1,2,3,4]
#
# sq_ls = [each**2 for each in ls]
#
# print(sq_ls)
#
# sq_dc = {each:each**2 for each in ls}
#
# print(sq_dc)

# class Person:
#     def __init__(self):
#         self.fn = "L1"
# # class Employee:
# #     def __init__(self):
# #         self.ln = "L2"
#
# class derived(Person):
#     def __init__(self):
#         self.ln = "L2"
#
# obj = derived()
# print(obj.ln)
# print(obj.fn)

# def a(a,b):
#     pass
# def a(a):
#     pass
# a(1,2)


# class m1:
#     @staticmethod
#     def add(a,b):
#         return a+b
#     @classmethod
#     def fun(cls,arg1,arg2):
#
# res = m1.add(1,2)
# print(res)




# class FactorialGenerator:
#     def __init__(self,name):
#         self.filename = name
#     def prompt(self):
#         num = int(input("Enter the number for Factorial: "))
#         return num
#     def factorial(self,num):
#         fact = 1
#         if num < 0:
#             print("invalid num")
#         elif num == 0:
#             return 1
#         else:
#             for i in range(1,num+1):
#                 fact = fact*i
#             print(fact)
#             return fact
#
#     def generate_results(self,num):
#         val = self.factorial(num)
#         with open(self.filename) as file:
#             file.write(val)
#
# f_obj = FactorialGenerator(name="factor.txt")
#
# num = f_obj.prompt()
#
# v = f_obj.generate_results(num)
#
# print(v)
#
# from email_validator import validate_email
#
# testEmail = "example.@stackabuse.com"
#
# emailObject = validate_email(testEmail)
# print(emailObject.email)

# class Parent(object):
#     x = 1
#
# class Child1(Parent):
#     pass
#
# class Child2(Parent):
#     pass
#
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)

# 1 1 1
# 1 2 1
# 3 2 3


input_list = ['app', 'ppa', 'das','tab','pap' ,'bat']
output = [['app', 'ppa', 'pap'], ['das'],['bat','tab']]

def anagram(s1,s2):
    if(sorted(s1)) == sorted(s2):
        return True
    else:
        return False
ls = []
for i in range(len(input_list)):
    temp_ls = []
    for j in range(len(input_list)):
        if anagram(input_list[i],input_list[j]) \
                and input_list[j] not in temp_ls:
            temp_ls.append(input_list[j])
    if temp_ls not in ls:
        ls.append(temp_ls)
print(ls)

