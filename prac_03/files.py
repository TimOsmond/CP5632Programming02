"""
Testing the use of function to write to files.
"""
OUTPUT_FILE = "name.txt"


def main():
    """Print text to a file."""
    name = input("Name: ")
    out_file = open(OUTPUT_FILE, "w")
    print(name, file=out_file)
    out_file.close()


main()
