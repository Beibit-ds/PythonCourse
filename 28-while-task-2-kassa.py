total = 0
print("---------- КАССА ----------")
while True:
    text = input("Цена: ")
    if text.lower() == 'stop':
        break
    if not text.isnumeric():
        print('Incorrect price. ')
        continue
    price = int(text)
    total += price
print(total)
