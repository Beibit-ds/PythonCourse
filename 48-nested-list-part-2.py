'''
1 2 3
4 5 6
7 8 9
'''
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in lst:
    for element in row:
        print(f"{element} ", end="")
    print()