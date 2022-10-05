# age = int(input("What is your age: "))
# while age < 0 or age > 120:
#     print("Invalid age")
#     age = int(input("What is your age: "))
# if age <= 4:
#     age_range = "Baby"
# elif age <= 17:
#     age_range = "Child"
# elif age <= 65:
#     age_range = "Adult"
# else:
#     age_range = "Old"
# print(f"You are considered {age_range}")

# from random import randint
# number = randint(1, 10)
# # print(f"{number}")
# guess = int(input("Guess a number between 1 and 10 incl: "))
# while guess != number:
#     print("Try again!")
#     guess = int(input("Guess a number between 1 and 10 incl: "))
# print(f"Correct, the number was {number}")

# count = 0
# total_age = 0
# number_people = int(input("How many ages: "))
# for i in range(1, number_people + 1):
#     count = + i
#     age = int(input(f"What is age {count}: "))
#     total_age += age
#     average_age = total_age / number_people
# print(f"Total age is {total_age} \nAverage age is {average_age}")

# total_people = 0
# total_age = 0
# age = int(input("What is their age 1: "))
# while age >= 0:
#     total_people += 1
#     total_age += age
#     age = int(input(f"What is their age {total_people + 1}: "))
# if total_people == 0:
#     print("No input")
# else:
#     average_age = total_age / total_people
#     print(f"Total age of {total_people} people is {total_age} \nTheir average age is {average_age}")

# gifts = int(input("How many gifts: "))
# students = int(input("How many students: "))
# gift_each = gifts // students
# remainder = gifts % students
# print(f"Each student gets {gift_each} with {remainder} left over.")

# GST = 1.1  # add 10% GST
# price = float(input("Price: "))
# add_gst = input("Add GST (Y/N): ").upper()
# if add_gst == "Y":
#     print(f"Price is ${price * GST:.2f}")
# else:
#     print(f"Price is ${price:.2f}")

# from random import randint
#
# length = int(input("Length: "))
# width = randint(1, length)
# print(f"Width: {width}")
# print(f"Area of {length} x {width} is {length * width}")

# def print_grid(number_of_rows, number_of_columns):
#     for i in range(number_of_rows):
#         for j in range(number_of_columns):
#             print("*", end="")
#         print()
#
#
# print_grid(3, 7)

# """
# module-level docstring
# """
# import random
# import string
#
# """Make sure it has a docstring."""
#
#
# def main():
#     MENU = """(G)et name, (P)rint Greeting, (S)ecret name, (Q)uit"""
#     choice = ""
#     choice = menu_choice(MENU, choice)
#     while choice != "Q":
#         if choice == "G":
#             name = get_valid_name()
#             print(f"Hello {name}")
#             choice = menu_choice(MENU, choice)
#         elif choice == "P":
#             print_greeting()
#             choice = menu_choice(MENU, choice)
#         else:
#             print_secret_name()
#             choice = menu_choice(MENU, choice)
#     print("Bye!")
#
#
# def print_secret_name():
#     name = get_valid_name()
#     for i in range(1, len(name) + 1):
#         secret_name = random.choice(string.ascii_letters[0:26])
#         print(secret_name, end="")
#     print()
#
#
# def print_greeting():
#     name = get_valid_name()
#     length = len(name)
#     print("*" * length)
#     print(name)
#     print("*" * length)
#
#
# def menu_choice(MENU, choice):
#     print(MENU)
#     choice = input("Choose: ").upper()
#     return choice
#
#
# def get_valid_name():
#     """This is a DOCSTRING."""
#     name = input("Name: ")
#     if name == "":
#         print("Invalid name")
#         name = get_valid_name()
#     return name
#
#
# main()
#
# names = ["Bob", "Alice", "John", "Jane", "George", "Mary"]
# number = int(input(f"Which name (max={len(names)}): "))
# try:
#     print(names[number - 1])
# except IndexError:
#     print("Invalid number")
# except ValueError:
#     print("Invalid number")

# words = "one two three".split()
# for i in range(len(words)):
#     words[i] = words[i].title()
# text = ", ".join(words)
# print(text)

# from operator import itemgetter
#
# score_pairs = [["Derek", 100], ["Bob", 90], ["Alice", 95]]
# print(score_pairs)
# score_pairs.sort(key=itemgetter(1, 0), reverse=True)
# print(score_pairs)

text = "This is a sentence"
words = text.split()
long_words = [word for word in words if len(word) > 3]
print(long_words)
