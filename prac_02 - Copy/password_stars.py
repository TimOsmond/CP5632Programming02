"""
Get password and check length.
Print asterisks for each character in password.
"""

PASSWORD_LENGTH = 6


def main():
    """Get password and check length. Print asterisks for each character in password."""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print asterisks for each character in password."""
    print('*' * len(password))


def get_password():
    """Get password and check length."""
    password = input("Password: ")
    while len(password) < PASSWORD_LENGTH:
        print("Invalid password")
        password = input("Password: ")
    return password


main()
