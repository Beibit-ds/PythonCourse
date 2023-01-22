'''
Множество
Set
'''
my_set = {1,2,3, True, 'hello', 2, True}
set_2 = {2, 3, False}
print(my_set)
print(set_2)
print(my_set.union(set_2))
# 0 - False
# 1 - True
print(bool(-10))
print(my_set.difference(set_2))
print(set_2.difference(my_set))
