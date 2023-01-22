cities = ["Houston", "Astana", "Stockholm"]
'''
*******
******
*********
'''
# option 2
for city in cities:
    count = len(city)
    for i in range(count):
        print("*", end="")
    print()

# простой вариант
for city in cities:
    print("*" * len(city))