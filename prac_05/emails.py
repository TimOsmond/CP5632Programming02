"""
Extract name from email address and print list.
Estimate: 40 minutes
Actual:   32 minutes
"""

email = input("Email: ")
email_to_name = {}
while email != "":
    name = email.split("@")[0].split(".")
    name = " ".join(name).title()
    email_to_name[email] = name
    # email = input("Email: ")
    print(email_to_name)
