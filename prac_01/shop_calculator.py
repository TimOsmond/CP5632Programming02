"""
CP1404/CP5632 - Practical 1
Program to allow the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the
amount is displayed on the screen.
"""

DISCOUNT = 0.9  # percent discount
TOTAL_PRICE = 0

number_items = int(input("Number of items: "))
while number_items < 0:
    print("Invalid number of items!")
    number_items = int(input("Number of items: "))
for i in range(1, number_items + 1):
    item_price = float(input("Price of item: "))
    TOTAL_PRICE += item_price
if TOTAL_PRICE > 100:
    TOTAL_PRICE = TOTAL_PRICE * DISCOUNT
print(f"Total price for {number_items} items is ${TOTAL_PRICE:.2f}")
