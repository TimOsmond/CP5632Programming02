"""
Read the Wimbledon csv file and print out the names of the players who have won the most matches.
Estimate: 60 minutes
Actual:   32 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon csv results and print champions and countries."""
    winners_details = read_results_file(FILENAME)
    winners_count, winners_countries = get_results(winners_details)
    print_results(winners_count, winners_countries)


def read_results_file(filename):
    """Read the csv results file and create list."""
    winners_details = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            bits = line.strip().split(",")
            winners_details.append(bits)
    return winners_details


def get_results(winners_details):
    """ Get list results and return winners and countries."""
    winners_count = {}
    for winner in winners_details:
        try:
            winners_count[winner[2]] += 1
        except KeyError:
            winners_count[winner[2]] = 1
    winners_countries = set()
    for countries in winners_details:
        winners_countries.add(countries[1])
    return winners_count, winners_countries


def print_results(winners_count, winners_countries):
    """Print the results."""
    print("Wimbledon Champions:")
    for winner, count in winners_count.items():
        print(f"{winner} {count}")
    print(f"\nThese {len(winners_countries)} countries have won Wimbledon")
    print(", ".join(sorted(winners_countries)))


main()
