"""
CP1404/CP5632 - Practical 1
Program to show menu structure usage.
"""
name = input("Name: ")
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
print(MENU)
choice = input("Choose: ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
        print(MENU)
        choice = input("Choose: ").upper()
    elif choice == "G":
        print(f"Goodbye {name}")
        print(MENU)
        choice = input("Choose: ").upper()
    else:
        print("Invalid choice")
        print(MENU)
        choice = input("Choose: ").upper()
print("Finished.")
