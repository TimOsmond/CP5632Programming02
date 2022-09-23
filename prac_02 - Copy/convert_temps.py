"""
Read temperatures in Fahrenheit and convert to Celsius.
"""


def main():
    """Read temperatures in Fahrenheit and convert to Celsius."""
    in_file = open("temps_input.txt", "r")
    out_file = open("temps_output.txt", "w")
    for line in in_file:
        fahrenheit = float(line)
        celsius = convert_to_celsius(fahrenheit)
        print(celsius, file=out_file)
    in_file.close()
    out_file.close()


def convert_to_celsius(fahrenheit):
    """Convert from Fahrenheit to Celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
