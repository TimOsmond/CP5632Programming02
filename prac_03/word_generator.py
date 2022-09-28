"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
import string

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

for i in range(1):
    menu_choices = random.sample(string.ascii_lowercase, 3)
    consonant = menu_choices[0]
    vowel = menu_choices[1]
    either = menu_choices[2]
    print(menu_choices)
word_format = input(f"What format:\n \t{consonant} is consonant\n \t{vowel} is vowel\n "
                    f"\t{either} is either\n \tOther letters are used:\n"
                    f"*menu letters cannot be used*\n> ").lower()
word = ""
for kind in word_format:
    if kind == consonant:
        word += random.choice(CONSONANTS)
    elif kind == vowel:
        word += random.choice(VOWELS)
    elif kind == either:
        word += random.choice(string.ascii_lowercase)
    else:
        word += kind
print(word)
