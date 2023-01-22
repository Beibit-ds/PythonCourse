n = int(input("Количество книг: "))
books = []
for i in range(n):
    book = input("Книга: ")
    books.append(book)
keyword = input("Поиск: ")
for book in books:
    if keyword in book:
        print(book)
