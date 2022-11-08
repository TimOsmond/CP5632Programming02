"""
Guitars class
Estimated 60
1510
"""


class Guitar:
    """Get a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of Guitar object."""
        return f"{self.name:>25} ({self.year}) : ${self.cost:10,.2f}"
