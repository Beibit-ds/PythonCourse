lst = [1, 3 ,4, 5, 645, 23]
lst.sort()
print(lst)
lst = [1, 3 ,4, 5, 645, 23]
lst.clear()
print(lst)
lst = [1, 3 ,4, 5, 645, 23]
res = lst.pop()
print(res)
lst = [1, 3 ,4, 5, 645, 23]
lst.reverse()
print(lst)
# не копирует
lst = [1, 3 ,4, 5, 645, 23]
lst_2 = lst
print(lst_2)
lst_2[0] = 100
print(lst_2)
print(lst)
# Копирует
lst = [1, 3 ,4, 5, 645, 23]
lst_2 = lst.copy()  # copy
print(lst_2)
lst_2[0] = 100
print(lst_2)
print(lst)