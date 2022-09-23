"""
Print the grade for a given score.
"""

from random import randint


def main():
    """Get score and print the grade."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = score_result(score)
    print(result)
    score = randint(0, 100)
    random_result = score_result(score)
    print(f"Your random score is {score} which is {random_result.lower()}.")


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
