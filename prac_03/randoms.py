"""
Test the import of functions and ability for:
import random
    print(random.randint(5, 20))  # line 1
    print(random.randrange(3, 10, 2))  # line 2
    print(random.uniform(2.5, 5.5))  # line 3
and
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""

# What did you see on line 1?
# 5
# What was the smallest number you could have seen, what was the largest?
# smallest 5, largest 20

# What did you see on line 2?
# 3
# What was the smallest number you could have seen, what was the largest?
# smallest 3, largest 9
# Could line 2 have produced a 4?
# no

# What did you see on line 3?
# 3.4934706473081665
# What was the smallest number you could have seen, what was the largest?
# smallest 1.0, largest 5.5

from random import randint
from random import uniform

print(randint(0, 10))  # Whole numbers only
print(uniform(0, 100))  # To 15 decimal places
