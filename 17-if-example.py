item = input("Продукт: ")
# банан = 2, апельсин = 1.5
count = int(input("Количество: "))
if item == "banana":
    print(count * 2)
elif item == "orange":
    print(count * 1.5)
else:
    print("Такого продукта нет в каталоге.")
