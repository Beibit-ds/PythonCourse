sentence = input()
if len(sentence) > 3 and "Я" in sentence:
    print("Долго, о себе")
elif len(sentence) == 3 or "Я" in sentence:
    print("Коротко, о себе")