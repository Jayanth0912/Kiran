# details ={
#     "Name":"giri",
#     "Age":20,
#     "address":{
#         "street":"Kuravanka",
#         "DoorNo":"2-2"
#     },
#     "Hobbies":{
#         "indoor":["chess","carron"],
#         "outdoor":["cricket","kabadi"]
#     },
#     "phone_numbers":[8106882928,9949399999]
# }
# print(details.get("Name"))
# print(details.get("address").get("street"))
# print(details.get("Hobbies").get("outdoor"))


# print("GFG")
#
# # code for disabling the softspace feature
# print('G', 'F', 'G')




# str1 = input ("Enter the string")
# d1 = dict()
# for c in str1:
#     if c in d1:
#         d1[c] = d1[c] + 2
#     else:
#         d1[c] = 1
#     print (d1)


# string = "Anand"
# print("Duplicate characters in a given string: ");
# for i in range(0, len(string)):
#     count = 1;
#     for j in range(i + 1, len(string)):
#         if (string[i] == string[j] and string[i] != ' '):
#             count = count + 1;
#             string = string[:j] + '0' + string[j + 1:];
#
#     if (count > 1 and string[i] != '0'):
#         print(string[i], " - ", count);


#
# test_str = "anand"
#
# count = 0
#
# for i in test_str:
#     if i == 'a':
#         count = count + 1
#
# # printing result
# print("Count of a, in anand is : "
#  + str(count))
#



# chars = "anand"
# check_string = "i am checking this string to see how many times each character appears"
#
# for char in chars:
#   count = check_string.count(char)
#   if count > 0:
#     print(char, count)

#
# str = input("Anand")
#
# repeatingchars = set ()
# for ch in str:
#     if(str.count(ch)>1):
#         repeatingchars.add(ch)
#         print("Repeating characters in given string :", repeatingchars)

# dict1 = {'K': 19, 'M': 22, 'T': 21, 'Z': 20}
# max_k = ""
# max_v = 0
# for e in dict1:
#     if dict1[e]>max_v:
#         max_k = e
#         max_v = dict1[e]
# print(max_k)


# student_tuples = [
# ('john', 'A', 12),
# ('jane', 'B', 15),
# ('dave', 'B', 10),
# ]
# output = [
# ('dave', 'B', 10),
# ('john', 'A', 12),
# ('jane', 'B', 15),
# ]
# # for e in student_tuples:
# #     print()
#
# print(sorted(student_tuples,key=lambda x:x[2]))


# student_tuples.sort()
# print(student_tuples)





# inp=[23, 2, 9, 34, 8, 9, 10, 74]
# o = [10, 2, 23, 34, 8, 9, 9, 74]
# def f1(inpt):
#     ls = [ int(d) for d in str(inpt)]
#     return sum(ls)
# print(sorted(inp,key=f1))

# class First():
#     def get_details(self):
#         print("Calling get_details() from Class 'First'")
#
# class Second():
#     def get_details(self):
#         print("Calling get_details() from Class 'Second'")
#
# class Child(First, Second):
#     def __init__(self):
#         self.second = Second()
#     def B2(self):
#         self.second.get_details()
# obj_child = Child()
# obj_child.B2()







# ( converted Integer to String )

# num = 10
# x=str(num)
# print(type(x))
# print(x)




# ( converted String to Integer )

# str = "10"
# x=int(str)
# print(type(x))
# print(x)


# ( converted float to Int )

# float = 10.5
# x=int(float)
# print(type(x))
# print(x)


#      ( converted Boolean to Int )
# bool_val = True
# # print("Initial value", bool_val)
# bool_val = int(bool_val == True)
# print("Resultant value", bool_val)


# #      ( converted list into Set )
# list = [1, 2, 3, 3]
# x= set(list)
# print(x)
#
# kiran_list = [1, 3, 3, 4, 5, 6, 6, 6, 6, 7]
# x = set(kiran_list)
# print(x)




# N = [1, 2, 3, 4, 2, 65, 8, 9, 10, 11, 12, 13, 14, 15]
# # Sorting list of Integers in ascending
# N.sort()
# print(N)


# ls = {1,2,4,6,3,7,8}
# ls2 = {1,2,3,5}
# maximum = max(ls2)
# summed = sum(ls2)
# num = (maximum * (maximum+1))/2
# print(int(num-summed))

# def f1(k):
#     return k.upper()
# print(f1("anand"))
#
#

#
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# print("Enter which operation would you like to perform?")
# ch = input("Enter any of these char for specific operation +,-,*,/: ")
#
# result = 0
# if ch == '+':
#     result = num1 + num2
# elif ch == '-':
#     result = num1 - num2
# elif ch == '*':
#     result = num1 * num2
# elif ch == '/':
#     result = num1 / num2
# else:
#     print("Input character is not recognized!")
# print(num1, ch , num2, ":", result)
#



# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))
# n=int(input('input the number:'))
# if ( n%2)==0:
#
#    print ('it is a even number',n)
# else:
# num = int(input("Enter a number: "))
# def getSum(n):
#     sum = 0
#     for digit in str(n):
#         sum += int(digit)
#     return sum
# print(getSum(n))


x=3
if x%2 ==0:
    print("even")
elif x%2==1:
    print("odd")