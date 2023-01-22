'''
Lists
'''
# append
lst = [1,2,3,4]
lst.append(5)
print(lst)
# extend
lst_1 = [1,2,3,4]
lst_2 = [5,6,7]
# lst_3 = lst_1 + lst_2
# print(lst_3)
lst_1.extend(lst_2)
print(lst_1)
# del
lst_1 = [1,2,3,4]
del lst_1[2]
print(lst_1)