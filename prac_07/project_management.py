"""
Project management program.
"""

import datetime
from operator import attrgetter
from project import Project  # pylint: disable=import-error

# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))

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
        elif choice == "F":
            filter_by_date(projects)
        elif choice == "A":
            add(projects)
            # projects.append(add_project())
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU_STRING)
        choice = input(">>> ").upper()
    save_projects(projects, FILENAME)
    print("Thank you for using custom_built project management software.")


def load_projects(filename):
    """Load projects from file"""
    projects = []
    with open(filename, encoding="utf-8") as in_file:
        in_file.readline()  # Remove header
        for line in in_file:
            parts = line.strip().split('\t')
            start_date = datetime.datetime.strptime(parts[1], "%Y-%m-%d").date()
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
        print(f"\t{project}")
    print("Complete projects:")
    complete_projects = [project for project in projects if project.is_complete()]
    complete_projects.sort()
    for project in complete_projects:
        print(f"\t{project}")


def display_listed_projects(projects):  # add number to list
    for project in enumerate(projects):
        print(project[0], project[1])


def add(projects):
    """Add project"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = get_valid_integer("Priority: ")
    cost_estimate = get_valid_float("Cost estimate: ")
    completion_estimate = get_valid_float("Percent complete: ")
    project = Project(name, start_date, priority, cost_estimate, completion_estimate)
    projects.append(project)


def get_valid_date(prompt):
    """Get valid date"""
    valid_date = False
    while not valid_date:
        try:
            start_date = input(prompt)
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            valid_date = True
        except ValueError:
            print("Invalid date")
    return start_date


def get_valid_integer(prompt):
    """Get valid integer"""
    valid_integer = False
    while not valid_integer:
        try:
            integer = int(input(prompt))
            valid_integer = True
        except ValueError:
            return ""
    return integer


def get_valid_float(prompt):
    """Get valid float"""
    valid_float = False
    while not valid_float:
        try:
            float_value = float(input(prompt))
            valid_float = True
        except ValueError:
            return ""
    return float_value


def update_project(projects):
    """Update project"""
    display_listed_projects(projects)
    name = int(input("Project choice: "))
    project = get_project_by_number(projects, name)
    if project is not None:
        print(project[1])
        project[1].completion_estimate = get_valid_integer("New Percentage: ") or project[1].completion_estimate
        project[1].priority = get_valid_integer("New Priority: ") or project[1].priority
    else:
        print("Project not found")


def get_project_by_number(projects, number):
    """Get project by number"""
    for project in enumerate(projects):
        if project[0] == number:
            return project
    return None


def add_project():
    """Add project"""
    name = input("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = get_valid_integer("Priority: ")
    cost_estimate = get_valid_float("Cost estimate: ")
    completion_estimate = get_valid_float("Completion estimate: ")
    project = Project(name, start_date, priority, cost_estimate, completion_estimate)
    return project


def filter_by_date(projects):
    """Filter projects by date"""
    date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
    filtered_projects = [project for project in projects if project.start_date >= date]
    filtered_projects.sort(key=attrgetter("start_date", "priority"))
    for project in filtered_projects:
        print(project)


main()
