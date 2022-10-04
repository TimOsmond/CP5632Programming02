"""
Ask for indefinite number of strings until empty
string and print duplicates.
"""


def main():
    """Get strings and print duplicates."""
    strings = []
    string = get_string()
    while string != "":
        strings.append(string)
        string = get_string()
    if len(strings) > 0:
        print("The unique strings are:")
        print_unique_strings(strings)
    else:
        print("No strings entered.")


def get_string():
    """Get string from user."""
    string = input("Enter string: ")
    return string


def print_unique_strings(strings):
    """Print duplicate strings."""
    for i, string in enumerate(strings):
        if string in strings[:i]:
            print(string)


main()
