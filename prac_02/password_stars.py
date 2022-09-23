"""
Get password and check length.
Print asterisks for each character in password.
"""

PASSWORD_LENGTH = 6


def main():
    """Get password and check length."""
    password = input("Password: ")
    while len(password) < PASSWORD_LENGTH:
        print("Invalid password")
        password = input("Password: ")
    print('*' * len(password))


main()
