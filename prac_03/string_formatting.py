"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

NAME = "Gibson L-5 CES"
YEAR = 1922
COST = 16035.4

# The ‘old’ manual way to format text with string concatenation:
print("My guitar: " + NAME + ", first made in " + str(YEAR))

# A better way - using str.format():
print("My guitar: {}, first made in {}".format(NAME, YEAR))
print("My guitar: {0}, first made in {1}".format(NAME, YEAR))
print("My {0} was first made in {1} (that's right, {1}!)".format(NAME, YEAR))

# And with f-string formatting (introduced in Python 3.6)
print(f"My {NAME} was first made in {YEAR} (that's right, {YEAR}!)")

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(NAME, COST))
print(f"My {NAME} would cost ${COST:,.2f}")

# Aligning columns by using width after the :
# This loop uses enumerate, useful when you want both the index and value
numbers = [1, 19, 123, 456, -25]

for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

# Use f-string formatting to produce the output:
# 1922 Gibson L-5 CES for about $16,035!
print(f"{YEAR} {NAME} for about ${COST:.0f}!")

# Using a for loop with the range function and string formatting,
# produce the following right-aligned output (DO NOT use a list):
#   0
#  50
# 100
# 150
for i in range(0, 151, 50):
    print(f"{i:3}")
