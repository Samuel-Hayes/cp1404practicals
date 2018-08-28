WORD_COUNT = {}
word_count = 0
user_string = str(input("Please enter a string: "))
words = user_string.split()
for word in words:
    frequency = WORD_COUNT.get(word, 0)     #didn't know this
    WORD_COUNT[word] = frequency + 1
words = list(WORD_COUNT.keys()) #didn't know this
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, WORD_COUNT[word]))

print(WORD_COUNT)
