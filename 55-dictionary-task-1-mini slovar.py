dictionary = {
    'Name': 'Имя',
    'Age': 'Возраст',
    'Dictionary': 'Словарь'
}
word = input("Word: ")
while word != "stop":
    if word in dictionary:
        print(dictionary[word])
    else:
        print("This word doesn't exist in our dictionary.")
    word = input("Word: ")