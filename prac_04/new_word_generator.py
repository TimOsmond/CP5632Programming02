"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    """ Generate a random word based on the user's input. """
    consonant = "c"
    vowel = "v"
    word_format = input(f"What format:\n \t{consonant} is consonant\n \t{vowel} is vowel\n>> ").lower()
    word = ""
    while not is_valid_input(word_format):
        word_format = input("Invalid input, please enter a valid format: ").lower()
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        if kind == "v":
            word += random.choice(VOWELS)
    print(word)


def is_valid_input(word_format):
    """ Check if the input is valid. """
    for kind in word_format:
        if kind not in ("c", "v"):
            return False
    return True


main()
