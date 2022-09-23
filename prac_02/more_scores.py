"""
Get scores and generate that many random numbers between 1-100 incl.
Write results to a file.
"""

from random import randint


def main():
    """Get scores and generate that many random numbers between 1-100 incl.
    Write results to a file."""
    number_of_scores = int(input("How many scores: "))
    out_file = open("results.txt", "w")
    for i in range(number_of_scores):
        score = randint(1, 100)
        result = score_result(score)
        print(f"{score} is {result}", file=out_file)
    out_file.close()


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
