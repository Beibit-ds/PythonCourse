# определите тип предложения
sentence = input()
if "." in sentence:
    print("Повествовательное")
elif "?" in sentence:
    print("Вопросительное")
elif "?" in sentence:
    print("Побудительное")
else:
    print("Непонятно")