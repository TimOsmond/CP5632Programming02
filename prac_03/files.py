"""
Testing the use of function to write to files.
"""
OUTPUT_FILE = "name.txt"


def main():
    """Print to and read from a file."""
    #  Code 1.
    name = input("Name: ")
    out_file = open(OUTPUT_FILE, "w")
    print(name, file=out_file)
    out_file.close()
    #  Code 2.
    in_file = open(OUTPUT_FILE, "r")
    read_line = in_file.readline()
    in_file.close()
    print(f"Your name is {read_line}")
    # Code 3.
    in_file = open("numbers.txt", "r")
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    in_file.close()
    result = number1 + number2
    print(result)
    #  Code 4.
    in_file = open("numbers.txt", "r")
    result = 0
    for line in in_file:
        number = int(line)
        result += number
    in_file.close()
    print(result)


main()
