"""
Store a list of guitarsand print details.
"""
from prac_06.guitar import Guitar


def main():
    """Store a list of guitars and print their details"""

    guitars = []
    print("My guitars!")
    name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    while name != "":
        # name = input("Name: ")
        year = int(input("Year: "))
        cost = input("Cost: ")
        if "$" in cost:
            try:
                cost = float(cost[1:])
            except ValueError:
                print("Invalid cost")
                cost = input("Cost: ")
        cost = float(cost)
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input("\nName: ")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
