"""
Lookup ASCII and vice versa.
"""
LOWER = 33
UPPER = 127

character = input("Enter a character: ")
char_ascii = ord(character)
print(f"The ASCII code for {character} is {char_ascii}")
char_number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
while char_number < LOWER or char_number > UPPER:
    print("Invalid number")
    char_number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
char = chr(char_number)
print(f"The character for {char_number} is {char}\n")
for i in range(LOWER, UPPER + 1):
    print(f"{i:<4} {(chr(i)):>2}")
