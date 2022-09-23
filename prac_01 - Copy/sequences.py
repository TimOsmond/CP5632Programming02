"""
CP1404/CP5632 - Practical 1
Program to allow primary school students to learn about various number sequences.
A menu-driven program that has the following choices (where x and y are inputs
the user enters once at the start of the program):
Show the even numbers from x to y
Show the odd numbers from x to y
Show the squares from x to y
Exit the program
"""

MENU = "(C)alculate\n(Q)uit"
print(MENU)
choice = input("Enter your selection: ").upper()
while choice != "Q":
    if choice == "C":
        x = int(input("What is the first number: "))
        y = int(input("What is the last number: "))
        if x % 2 == 1:
            even_x = x + 1
        else:
            even_x = x
        if y % 2 == 0:
            even_y = y + 1
        else:
            even_y = y
        print("The even numbers are:")
        for i in range(even_x, even_y, 2):
            print(i, end=" ")
        if x % 2 == 0:
            odd_x = x + 1
        else:
            odd_x = x
        if y % 2 == 1:
            odd_y = y + 1
        else:
            odd_y = y
        print("\nThe odd numbers are:")
        for i in range(odd_x, odd_y, 2):
            print(i, end=" ")
        print("\nThe squares are:")
        for i in range(x, y + 1):
            print(i ** 2, end=" ")
        print("\n")
        print(MENU)
        choice = input("Enter your selection: ").upper()
print("Goodbye")
