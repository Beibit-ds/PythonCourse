def count_words_in_string(sentence):
    words = sentence.split(" ")
    number_of_words = len(words)
    return number_of_words

s1 = "I love Python"
number_of_words = count_words_in_string(s1)
print(number_of_words)