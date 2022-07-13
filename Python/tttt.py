# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
#
# driver.find_element(By.XPATH,"//button")
# driver.find_elements(By.XPAYTH,//button)

# # Tuple
# t = (1,2)
#
# # Dict
# d = {"name":"user1"}
#
# # set
# s = {1,2,3}
#
# # list
# l = [1,2,3]

#
# st = "Swapna Tech Lead in Office"
# out = "Sw1pn1 T2ch L21d in 4ff3c2"
# st_ls = list(st)
# ovels = {
#     "a":1,
#     "e":2,
#     "i":3,
#     "o":4,
#     "u":5,
# }
# for ind,each in enumerate(st_ls):
#     if each.lower() in ovels:
#         st_ls[ind]= ovels[each.lower()]
# print("".join(st_ls))



n = 37

ls = []
for i in range(n):
    if (n-i > i):
        ls.append((i,n-i))
print(ls)