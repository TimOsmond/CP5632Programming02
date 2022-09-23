"""
Create 20 floats of random values between -200 to +200
"""

import random


def main():
    """Create 20 floats of random values between -200 to +200"""
    out_file = open("temps_input.txt", "w")
    for i in range(20):
        number = random.uniform(-200, 200)
        print(number, file=out_file)
    out_file.close()


main()
