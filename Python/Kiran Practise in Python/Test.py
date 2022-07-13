# lambda fuction

# x=lambda n:n**2
# print(x(5))
#
# y=lambda a,b,c,d,e,f: a**2 +b**2 +c -d +e/2+f
# print(y(1,2,3,4,5,6))

# import tutorial
# print(tutorial.my_name)
# print(tutorial.my_address)
# print(tutorial.f1())
# print(tutorial.f2(tutorial.my_name))
# print(tutorial.my_address1.get("city"))
# print(tutorial.my_address1.get("pincode"))


# a=10
# b=20
# # print(a+b)
# a="kiran"
# b=" kumar"
# print(a+b)
#
# ls1=[1,2,3,4]
# ls2=[5,6,7,8]
# print(ls1+ls2)
# ls1.append(ls2)
# print(ls1)
#
# def f1(a,b,c):
#     return a-b,b-c,c-a,b-a
# print(f1(22,15,20))
#
# x,y,z=f1(20,15,20)
# print(x,y,z)


# def greet(name,class_name,topic):
#     # print("hello",name,"Welcome to",class_name,"on",topic)
#       print("hello {} welcome to {} on {}".format(name,class_name,topic))
# greet("kiran","Demo class","python")
#
# def greet(name):
#     print("hello", name)
# greet("kiran")
import random
import string
from tkinter import StringVar

from each import each

# name="kiran"
# len_char=5
# for each in range(len_char):
#     print(name[each],end="")
# print()
# print("hello")


ovels = ["a", "e", "i", "o", "u"]
# for each in range(ovels):
#     if each.lower() in "aeiou":
#         print(ovels[each],end="")
# print()

# inp=input("enter a String: ")
# for each in inp:
#     if each in ovels:
#         print(each,inp.count(each))

# class

class student():
    def __init__(self,user_name,password):
        if user_name == "kiran" and password == "12345":
            pass
        else:
            raise Exception("UnAuthorised")
    def get_info(self):
        return "info"
    def get_name(self):
        return "name"
ram=student("kiran","gsdsdsf")
print(ram.get_info())
print(ram.get_name())


#( Program to take screenshot )

# import pyscreenshot
#
# # To capture the screen
# image = pyscreenshot.grab()
# #
# # # To display the captured screenshot
# # image.show()
# #
# # # To save the screenshot
# image.save("Kiran_kumar.png")
#
# #
#
# # import pyautogui
# from PIL import Image
# #
# # # Taking Screenshot
# # takeScreenshot = pyautogui.screenshot()
# #
# # # The path of Screenshot and r' is used for specifying raw string
# # screenshotPath = r'D:\fold\PDF\screenshot.png'
# #
# # # Saving the screenshot in the given Path
# # takeScreenshot.save(screenshotPath)
#
# # Opening image
# open_image = Image.open("Kiran_kumar.png")
# convert_image = open_image.convert('RGB')
#
# # Output Pdf Path
# outputpdfPath = r'D:\fold\kiran.pdf'
#
# # Saving the pdf
# open_image.save(outputpdfPath)
#

#
#
# import random
# import array
#
# # maximum length of password needed
# # this can be changed to suit your password length
# MAX_LEN = 12
#
# # declare arrays of the character that we need in out password
# # Represented as chars to enable easy string concatenation
# DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
#                      'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
#                      'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#                      'z']
#
# UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
#                      'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
#                      'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
#                      'Z']
#
# SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
#            '*', '(', ')', '<']
#
# # combines all the character arrays above to form one array
# COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
#
# # randomly select at least one character from each character set above
# rand_digit = random.choice(DIGITS)
# rand_upper = random.choice(UPCASE_CHARACTERS)
# rand_lower = random.choice(LOCASE_CHARACTERS)
# rand_symbol = random.choice(SYMBOLS)
#
# # combine the character randomly selected above
# # at this stage, the password contains only 4 characters but
# # we want a 12-character password
# temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
#
# # now that we are sure we have at least one character from each
# # set of characters, we fill the rest of
# # the password length by selecting randomly from the combined
# # list of character above.
# for x in range(MAX_LEN - 6):
#     temp_pass = temp_pass + random.choice(COMBINED_LIST)
#
#     # convert temporary password into array and shuffle to
#     # prevent it from having a consistent pattern
#     # where the beginning of the password is predictable
#     temp_pass_list = array.array('u', temp_pass)
#     random.shuffle(temp_pass_list)
#
# # traverse the temporary password array and append the chars
# # to form the password
# password = ""
# for x in temp_pass_list:
#     password = password + x
#
# # print out password
# print(password)

#
# import string
# lc = string.ascii_lowercase
# uc = string.ascii_uppercase
# x = list(range(10))
# print(lc,uc,x)
# for ind,each in enumerate(uc):
#     print(each,ind+1)



# pass_str = StringVar()
def Generator():
    password = ''
    pass_len = 8
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    print(password)

Generator()