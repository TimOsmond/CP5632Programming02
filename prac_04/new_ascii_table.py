"""
Lookup ASCII and vice versa.
"""
MAX_COLUMNS = 10
MIN_COLUMNS = 2
LOWER = 33
UPPER = 127


def main():
    """Get a valid number, lookup ASCII and vice versa."""
    # valid_number = int(input("Enter a number (10-50): "))
    lower = 10
    upper = 50
    input_number = int(input(f"Enter a number ({lower}-{upper}): "))
    valid_number = get_number(lower, upper)
    print(f">>>{valid_number}")
    # character = input("Enter a character: ")
    # char_ascii = ord(character)
    # print(f"The ASCII code for {character} is {char_ascii}")
    # char_number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
    # while char_number < LOWER or char_number > UPPER:
    #     print("Invalid number")
    #     char_number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
    # char = chr(char_number)
    # print(f"The character for {char_number} is {char}\n")
    # for value in range(LOWER, UPPER + 1):
    #     print(f"{value:4} {chr(value):>4}")
    # # The following code was taken from the answer sheet for future reference
    # # ASCII tables with columns (two versions)
    # columns = int(input("Enter number of columns: "))
    # while columns < MIN_COLUMNS or columns > MAX_COLUMNS:
    #     print("Please use a value between {} and {}".format(MIN_COLUMNS, MAX_COLUMNS))
    #     columns = int(input("Enter number of columns: "))
    # # calculate the range of values and the number of full rows
    # number_of_values = UPPER - LOWER + 1
    # rows = number_of_values // columns
    #
    # print("Version 1: Horizontal then vertical ordering")
    # # iterate through the full rows first, incrementing by 1
    # value = LOWER
    # for row in range(rows):
    #     for column in range(columns):
    #         print("{:6} {:>2}".format(value, chr(value)), end="")
    #         value += 1
    #     print()
    #
    # # last row is special as it may not have all columns so handle separately
    # # start where we left off and only print up to UPPER
    # starting_value = value
    # for value in range(starting_value, UPPER + 1):
    #     print("{:6} {:>2}".format(value, chr(value)), end="")
    # print("\n")
    #
    # print("Version 2: Vertical then horizontal ordering")
    # # iterate through rows
    # for row in range(rows + 1):
    #     starting_value = LOWER + row
    #     value = starting_value
    #     # print all column values not including the last one (-1)
    #     for column in range(columns - 1):
    #         value_to_print = value + (column * rows)
    #         print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
    #         value += 1
    #
    #     # last column may not exist so handle separately
    #     # having the if statement outside the for loop means we don't do it every column,
    #     # so it is more efficient (we can't avoid doing it every row AFAIK)
    #     value_to_print = value + ((column + 1) * rows)
    #     if value_to_print <= UPPER:
    #         print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
    #     print()


def get_number(lower, upper):
    """Get a valid number."""
    try:
        while input_number < lower or input_number > upper:
            print("Please enter a valid number!")
            input_number = int(input(f"Enter a number ({lower}-{upper}): "))
    except ValueError:
        print("Please enter a valid number!")
        input_number = int(input(f"Enter a number ({lower}-{upper}): "))
    else:
        valid_number = input_number
        return valid_number


main()
