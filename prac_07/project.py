"""Project management program."""




class Project:
    """Get a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_estimate):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_estimate = completion_estimate

    def __repr__(self):
        """Return a string representation of Project object."""
        return f"Project({self.name}, {self.start_date}, {self.priority}, {self.cost_estimate}, {self.completion_estimate})"

    def __lt__(self, other):
        """Overload less than to compare year."""
        return self.priority < other.priority

    def is_complete(self):
        """Check if the project is complete."""
        return self.completion_estimate == 100

    def __str__(self):
        """Return a string representation of Project object."""
        return f"{self.name} ({self.start_date}) : ${self.cost_estimate:.2f}"

    def get_age(self):
        """Get the age of the project."""
        today = datetime.date.today()
        current_year = today.year
        # print(current_year)
        return current_year - self.year
