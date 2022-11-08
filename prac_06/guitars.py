"""
Store a list of guitars and print details.
"""
from prac_06.guitar import Guitar  # pylint: disable=import-error


def main():
    """Store a list of guitars and print their details"""

    guitars = []
    print("My guitars!")
    name = input("Name: ")

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

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
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), "
              f"worth ${guitar.cost:10,.2f} {vintage_string}")


main()
