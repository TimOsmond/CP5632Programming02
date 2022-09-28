"""
Calculate stock price from a starting price using random.
The end of each day, stock has 50% chance of an increase and 50% chance of a decrease.
Above a limit or below a limit ends program.
"""

import random

MAX_PRICE = random.randint(5, 1000)
MIN_PRICE = random.uniform(0.1, 10)
STARTING_PRICE = random.randint(10, 100)
OUTPUT_FILE = "earnings.txt"
MAX_INCREASE = random.uniform(1, 2)  # Maximum percentage increase
MAX_DECREASE = random.uniform(0.01, 0.8)  # Maximum percentage decrease
CHANCE_OF_INCREASE = 50  # Percentage chance of increase (inclusive)


def main():
    """Calculate stock price from a starting price using random."""
    number_of_days = 0
    price = STARTING_PRICE
    print(f"Starting price: ${STARTING_PRICE:.2f}")
    out_file = open(OUTPUT_FILE, 'w')
    while MAX_PRICE >= price >= MIN_PRICE:
        day_chance = random.randint(0, 100)  # Chance of price going up or down
        number_of_days += 1
        price = calculate_profit_loss(day_chance, price)
        print(f"On day {number_of_days} price is: ${price:.2f}", file=out_file)
        print(f"On day {number_of_days} price is: ${price:.2f}")
    out_file.close()
    if price > MAX_PRICE:
        print("You're a winner!")
    else:
        print("You're bankrupt!")


def calculate_profit_loss(day_chance, price):
    """Calculate profit or loss for the day."""
    if day_chance <= CHANCE_OF_INCREASE:
        price = price * random.uniform(1, MAX_INCREASE)  # Increase price
    else:
        price = price * random.uniform(MAX_DECREASE, 1)  # Decrease price
    return price


main()
