"""
Read the Wimbledon csv file and print out the names of the players who have won the most matches.
Estimate: 60 minutes
Actual:   32 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon csv results and print champions and countries."""
    winners_details = read_results_file(FILENAME)
    print(winners_details)
    winners_count = {}
    winner_names = set()
    for winner in winners_details:
        winner_names.add(winner[2])
    print(winner_names)


def read_results_file(filename):
    """Read the csv results file and create list."""
    winners_details = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            bits = line.strip().split(",")
            winners_details.append(bits)
    return winners_details


main()
