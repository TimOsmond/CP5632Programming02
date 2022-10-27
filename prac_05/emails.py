"""
Extract name from email address and print list.
Estimate: 40 minutes
Actual:   90 minutes
"""


def main():
    """Get name from email and create dictionary of email to names to print"""
    email = input("Email: ")
    email_to_name = {}
    while email != "":
        username = get_name_from_email(email, email_to_name)
        check_name = input(f"Is your name {username}? (Y/N) ").lower()
        if check_name != "y" and check_name != "":
            username = input("Name: ").title()
        email_to_name[email] = username  # Add name to dictionary
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email, dictionary):
    """Extract users name from email address and add to dictionary"""
    username = email.split("@")[0].split(".")
    username = " ".join(username).title()
    dictionary[email] = username  # Add email and name to dictionary
    return username


main()
