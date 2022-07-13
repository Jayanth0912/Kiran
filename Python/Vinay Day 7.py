# import os
#
# import tgt as tgt
# from pip._internal.cli.cmdoptions import src
#
# os.remove(os.path.join("D:\Python\k1.py"))
# print(os.getcwd())
#
#
# # Write a method to copy files from one directory to another directory
#
# # add your name to each file inside target directory
#
# def method(src_path, tgt, path):
#     pass
#
# method(src, tgt)



# Folder Created in Particulat Path
#
# import os
#
# # Directory
# directory = "Kiran"
#
# # Parent Directory path
# parent_dir = "D:/Kumar/Folders"
#
# # Path
# path = os.path.join(parent_dir, directory)
#
# os.makedirs(path)
# print("Directory '% s' created" % directory)



# Rename Folder
# import os
#
# os.rename("D:\Kumar", "D:\Rajesh")
#
# print("The File has been successfully renamed!")

# file copying

# import shutil
#
# original = r'D:\Rajesh\kk.txt'
# target = r'D:\Files\kk.txt'
#
# shutil.copyfile(original, target)


# Stock Market Profit of Code
# vals = [7,1,5,3,6,4]
#
# min_val = 0
# max_val = 0
# min_ind = 0
# for index,i in enumerate(vals):
#     if min_val == 0 or i< min_val:
#         min_val = i
#         min_ind = index
#     if index > min_ind and i>max_val:
#         max_val = i
# print(max_val-min_val)


#
# file1=open("sample text.txt",'r')
# print(file1.name)
# print(file1.mode)
# file1.close()


# File Inside of Content printing

# with open("sample text.txt",'r') as f1:
#     for each_line in f1:
#         print(each_line)
#

   # In file Print On How many words are same in given count

# search_string="kiran"
# count=0
# with open("sample text.txt",'r') as f1:
#     for each_line in f1:
#         if search_string in each_line:
#             count+=1
#     print(count)

# import os
# if os.path.exists("sample text.txt"):
# os.rename("sample text.txt","sample.txt")
    # print("Successfully changed rename in file")
# os.remove("sample.txt")
    # print("Successfully Deleted")


# os.mkdir
# os.chdir - Change Directory
# os.getcwd - current working Directory
# os.rmdir - Remove Directory


import os
# file="kiran.txt"
# parent_dir='D:/Python/kiran.txt'
# content='This is Kiran I am from MPL'
# with open("kiran.txt","a") as k1:
#     for each in k1:
#             f.write(each)


def k1():
    name= "kiran"
    return name
name=k1()













