
# num=int(input("enter a number:"))
# for i in range(1,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print("Prime")
#

# num=int(input("enter a number:"))
# for i in range(1,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print("Prime")


# import traceback
# def f1():
#     try:
#         for Number in range (100, 201):
#             count = 0
#             for i in range(2, (Number//2 + 1)):
#                 if Number % i == 0:
#                     count = count + 1
#                     break
#             if (count == 0 and Number != 1):
#                 print(" %d" %Number, end = '  ')
#     except Exception as e:
#         traceback.print_exc()
#         print("Unable to generate Prime Numbers")
#         # raise("Unable to generate Prime Numbers")
# f1()


# from numpy import *
# arr1 = array([
#             [1,2,3,4,5,6],
#             [3,6,9,8,9,8]
#             ])
# arr2=arr1.flatten()
# arr3=arr2.reshape(2,2,3)
# print(arr3)


from numpy import *
m1=matrix('1 2 4; 4 5 6; 6 8 9')
m2=matrix('1 2 8; 4 6 6; 6 7 9')
m3 = m1 * m2
print(m3)
# print(diagonal(m))
# print(m)
# print(m.max())














