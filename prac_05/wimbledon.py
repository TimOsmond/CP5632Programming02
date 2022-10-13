"""
Read the Wimbledon csv file and print out the names of the players who have won the most matches.
Estimate: 60 minutes
Actual:   32 minutes
"""


def main():
    filename = "wimbledon.csv"
    read_results_file(filename)


def read_results_file(filename):
    winner_details = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            bits = line.strip().split(",")
            winner_details.append(bits)
        print(winner_details)


main()
