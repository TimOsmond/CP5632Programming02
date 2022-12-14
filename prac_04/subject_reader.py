"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Display classes information"""
    data = get_data()
    print(data)
    print_details(data)


def print_details(data):
    """Print details of classes"""
    for class_details in data:
        print("{} is taught by {:12} and has {:3} students".format(*class_details))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    with open(FILENAME) as input_file:
        data = []  # list of lists
        for line in input_file:
            print(line)  # See what a line looks like
            print(repr(line))  # See what a line really looks like
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            print(parts)  # See what the parts look like (notice the integer is a string)
            parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
            print(parts)  # See if that worked
            print("----------")
            data.append(parts)
        return data


main()
