"""
Open a list of guitars and print details.
"""
from guitar import Guitar  # pylint: disable=import-error


def main():
    """Open a list of guitars and print their details"""

    print("My guitars!")

    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
    # File format is like: Name,Year,Cost
    for line in in_file:
        # print(repr(line))  # debugging
        parts = line.strip().split(',')
        # print(parts)  # debugging
        # Construct a guitar object using the elements
        # price should be a float
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        # Add the guitar we've just constructed to the list
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()
    guitars.sort()
    # Loop through and display all guitars
    for guitar in guitars:
        print(guitar)

    print("\nAdd Guitar?")
    name = input("Name: ")
    while name != "":
        is_valid_input = False
        while not is_valid_input:
            try:
                year = int(input("Year: "))
                is_valid_input = True
            except ValueError:
                print("Invalid year")

        is_valid_input = False
        while not is_valid_input:
            try:
                cost = input("Cost: ")
                if "$" in cost:
                    cost = float(cost[1:])
                cost = float(cost)
                is_valid_input = True
            except ValueError:
                print("Invalid cost")
            guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost:.2f} added.")
            name = input("\nName: ")
    guitars.sort()
    print("My guitars!")
    # Loop through and display all guitars
    for guitar in guitars:
        print(guitar)
    # Open the file for writing
    out_file = open('guitars.csv', 'w')
    # File format is like: Name,Year,Cost
    for guitar in guitars:
        out_file.write("{},{},{}\n".format(guitar.name, guitar.year, guitar.cost))
    # Close the file as soon as finished writing to it
    out_file.close()


main()
