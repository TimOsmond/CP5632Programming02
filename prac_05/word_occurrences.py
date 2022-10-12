"""
Word Occurrences
Count the number of each word in a sentence and print alphabetically.
Estimate: 30 minutes
Actual:   35 minutes
"""

words = (input("What is the sentence: ").lower().split(" "))
words.sort()
word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
max_word_length = max((len(word) for word in word_to_count))
for word, count in word_to_count.items():
    print(f"{word:{max_word_length}} : {count}")
