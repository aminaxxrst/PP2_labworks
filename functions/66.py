#lambda with sorted, sort list by length of words
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words) #["pie", "apple", "banana", "cherry"]