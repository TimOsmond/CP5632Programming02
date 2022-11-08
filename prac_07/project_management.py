"""
Project management program.
"""

import datetime
from project import Project
from operator import attrgetter


MENU_STRING = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd project
- (U)pdate project
- (Q)uit"""
FILENAME = "projects.txt"
HEADER = "Name  Start Date  Priority    Cost Estimate  Completion Estimate"


def main():
    """Project management program"""
    projects = load_projects(FILENAME)
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("File to load: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("File to save: ")
            save_projects(projects, filename)
        elif choice == "D":
            display(projects)
        elif choice == "A":
            add(projects)
            projects.append(add_project())
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU_STRING)
        choice = input(">>> ").upper()
    save_projects(projects, FILENAME)
    print("Thank you for using the Project Management Program")


def load_projects(filename):
    """Load projects from file"""
    projects = []
    with open(filename, encoding="utf-8") as in_file:
        in_file.readline()  # Remove header
        for line in in_file:
            parts = line.strip().split('\t')
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)
    return projects


def save_projects(projects, filename):
    """Save projects to tab delimited file"""
    with open(filename, 'w', encoding="utf-8") as out_file:
        print(HEADER, file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_estimate}", file=out_file)


def display(projects):
    """Display projects"""
    print("Incomplete projects:")
    incomplete_projects = [project for project in projects if not project.is_complete()]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(" ", project)
    print("Complete projects:")
    complete_projects = [project for project in projects if project.is_complete()]
    complete_projects.sort()
    for project in complete_projects:
        print(" ", project)


main()
