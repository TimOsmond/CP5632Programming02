"""
Write 3 different versions of code to
generate a random Boolean (True or False).
"""

import random

random_boolean = bool(random.getrandbits(1))
print(random_boolean)

random_boolean = bool(random.choice([True, False]))
print(random_boolean)

print(bool(random.randint(0, 1)))
