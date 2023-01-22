# проверка имени пользователя
username = input()
if 3 <= len(username) <= 10 and \
    username.isalpha() and \
    username[0].isupper() and \
    username[1:].islower():
    print("Correct")
elif len(username) < 3 or len(username) > 10:
    print("Incorrect length")
elif not username.isalpha():
    print("Not only letters")
elif not username[0].isupper():
    print("First letter")
elif not username[1:].islower():
    print("Not all small")