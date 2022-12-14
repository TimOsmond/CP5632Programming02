"""
Guitars class
Estimated 60
1510
"""

import datetime


class Guitar:
    """Get a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Get the age of the guitar."""
        today = datetime.date.today()
        current_year = today.year
        # print(current_year)
        return current_year - self.year

    def is_vintage(self):
        """Check if the guitar is vintage."""
        return self.get_age() >= 50
