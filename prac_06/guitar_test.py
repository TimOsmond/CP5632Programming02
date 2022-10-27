"""
Test guitars class
"""

from prac_06.guitars import Guitar


def main():
    name1 = "Gibson L-5 CES"
    year1 = 1922
    cost1 = 16035.40
    guitar = Guitar(name1, year1, cost1)
    another_guitar = Guitar("Another Guitar", 2012, 1512.9)
    print(f"{guitar.name} get_age() - Expected 100, Got {guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True, Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} get_age() - Expected 10, Got {another_guitar.get_age()}")
    print(f"{another_guitar.name} is_vintage() - Expected False, Got {another_guitar.is_vintage()}")


main()
