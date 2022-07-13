# # class A:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age
# #   def add(self,a,b):
# #       return a+b
# #
# # class C:
# #   def __init__(self, name, age):
# #     self.name = "dfghj"
# #     self.age = age
# #   def add(self,a,b):
# #       return a+b
# #
# # class B(A,C):
# #     pass
# #
# # p1=B("kiran",20)
# # print(p1.name)
#
#
# class Class1:
#     def m(self):
#         print("In Class1")
#
#
# class Class2(Class1):
#     def m(self):
#         print("In Class2")
#
#
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#
#
# class Class4(Class2, Class3):
#     def m(self):
#         print("In Class4")
#
#
# obj = Class4()
# obj.m()



# def get_employee_details():
#     print("kiran")
#
# class employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

#     def get_employee_details(self):
#         print(self.name,self.id)
#
#
# get_employee_details()


# kiran = employee("kiran",1001)
#
# print(kiran.name)
# print(kiran.id)



# def add(a,b):
#     return a+b
# print(add(10,20))
#
# class kiran:
#     def add(self,a,b):
#         return a+b,a-b
#
# kiran=kiran()
# print(kiran.add(2,3))



class Apple:
    def __init__(self,contact_num,alternative_contact_num):
        self.contact_num=contact_num
        self.alternative_contact_num=alternative_contact_num
vinay=Apple("8106882928","6301717489")
print(vinay.contact_num)
print(vinay.alternative_contact_num)



