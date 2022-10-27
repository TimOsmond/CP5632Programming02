"""
Analyse lists of languages and return data.
Expected: 30 mins
Actual: 30 mins
"""

from programming_language import ProgrammingLanguage


def main():
    """Show details of programming languages."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print("The dynamically typed languages are:")
    for language in [python, ruby, visual_basic]:
        if language.is_dynamic():
            print(language.name)


main()
