"""
Analyse programming languages from given lists.
"""


class ProgrammingLanguage:
    """Language details from lists"""

    def __init__(self, name="", typing="", reflection="", year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string of language details from lists"""
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, " \
               f"First appeared in {self.year}"

    def is_dynamic(self):
        """Check if is dynamic"""
        return self.typing == "Dynamic"
