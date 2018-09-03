unique_words = {}
user_string = str(input("Please enter a string: "))
words = user_string.split()
for word in words:
    frequency = unique_words.get(word, 0) + 1
words = list(unique_words.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, unique_words[word]))

print(unique_words)
