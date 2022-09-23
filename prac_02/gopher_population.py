"""
Estimate the population of 1000 gophers after 10 years.
"""
from random import randint


def main():
    """Estimate the population of 1000 gophers after 10 years."""
    population = 1000
    years = 10
    print("Welcome to the Gopher Population Simulator!")
    print(f"Starting population: {population}")
    print("Year 1")
    print()
    for year in range(2, years + 1):
        birth_rate, born = number_born(population)
        death_rate, died = number_died(population)
        print(f"{born:.0f} gophers were born. {died:.0f} died.")
        population = total_population(birth_rate, death_rate, population)
        print(f"population: {population:.0f}")
        print(f"Year {year}")
        print()


def number_born(population):
    """Calculate the number of gophers born."""
    birth_rate = (randint(10, 20)) / 100
    born = population * birth_rate
    return birth_rate, born


def number_died(population):
    """Calculate the number of gophers that died."""
    death_rate = (randint(5, 25)) / 100
    died = population * death_rate
    return death_rate, died


def total_population(birth_rate, death_rate, population):
    """Return the total population after birth and death rates."""
    population = population + (population * birth_rate) - (population * death_rate)
    return population


main()
