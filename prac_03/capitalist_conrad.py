"""
Calculate stock price starting at $10.00 using random.
The end of each day, stock has 50% chance of 0-10% increase and 50% chance of 0-5% decrease.
Above $1000.00 or below $0.01 ends program.
"""

import random

MAX_PRICE = 1000
MIN_PRICE = 0.01
STARTING_PRICE = 10

number_of_days = 0
price = STARTING_PRICE
print(f"Starting price: ${STARTING_PRICE:.2f}")
while MAX_PRICE >= price >= MIN_PRICE:
    day_chance = random.randint(0, 100)
    number_of_days = number_of_days + 1
    if day_chance < 50:
        price = price * random.uniform(1, 1.1)
    else:
        price = price * random.uniform(1, 0.95)
    print(f"On day {number_of_days} price is: ${price:.2f}")
if price > 1000:
    print("You earnt over $1000!")
else:
    print("You're bankrupt!")
