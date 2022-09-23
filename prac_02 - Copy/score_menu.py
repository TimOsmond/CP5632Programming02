"""
Get a valid score between 0-100 inclusive.
Print a result for the score.
Print stars for the score number.
"""

MENU = """(E)nter score\n(Q)uit"""


def main():
    """Get a valid score between 0-100 inclusive. Print a result for the score.
    Print stars for the score number."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "E":
            score = int(input("Enter score: "))
            while score < 0 or score > 100:
                print("Invalid score")
                score = int(input("Enter score: "))
            result = score_result(score)
            print(result)
            print("*" * score)
            print(MENU)
            choice = input(">>> ").upper()
        else:
            print("Bye!")
    print("Bye!")


def score_result(score):
    """Return the grade for a given score."""
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
