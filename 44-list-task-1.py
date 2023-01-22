n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)
for word in words[1:-1]:
    print(word)