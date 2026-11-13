"""Mini Task Tracker - a menu-based task manager that saves tasks to tasks.json.

Each task is stored as a dictionary: {"title": "Read notes", "done": False}
The whole list is saved with json.dump() and loaded again with json.load(),
so the tasks are still there the next time the program runs.
"""

import json

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load the task list from tasks.json; return an empty list if that is not possible."""
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        # First run: there is no file yet, so start with an empty list.
        return []
    except json.JSONDecodeError:
        # The file exists but is empty or damaged.
        print("Warning: tasks.json could not be read. Starting with an empty list.")
        return []

    # Make sure the file holds a list of {"title": ..., "done": ...} dictionaries.
    valid = isinstance(tasks, list) and all(
        isinstance(task, dict) and "title" in task and "done" in task for task in tasks
    )
    if not valid:
        print("Warning: tasks.json has an unexpected format. Starting with an empty list.")
        return []
    return tasks


def save_tasks(tasks):
    """Write the task list to tasks.json."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    """Ask for a title and add it as a Pending task (done = False)."""
    title = input("Task title: ").strip()
    if title == "":
        print("Error: the title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    """Show a numbered list of tasks with [Pending] or [Done]."""
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")


def ask_task_number(tasks):
    """Ask for a task number and return its list index, or None if the input is invalid."""
    if len(tasks) == 0:
        print("There are no tasks yet.")
        return None

    text = input("Task number: ").strip()
    if not text.isdigit():
        print("Error: please enter a task number using digits, for example 1.")
        return None

    number = int(text)
    if number < 1 or number > len(tasks):
        print(f"Error: there is no task {number}. Choose a number from 1 to {len(tasks)}.")
        return None
    return number - 1          # the list starts at index 0, the display at 1


def complete_task(tasks):
    """Mark the selected task as done (done = True)."""
    index = ask_task_number(tasks)
    if index is None:
        return
    if tasks[index]["done"]:
        print("That task is already completed.")
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task completed.")


def delete_task(tasks):
    """Remove the selected task from the list."""
    index = ask_task_number(tasks)
    if index is None:
        return
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Task deleted: {removed['title']}")


def main():
    """Load saved tasks, then keep showing the menu until the user chooses Exit."""
    tasks = load_tasks()
    print("\n--- TASK TRACKER ---")
    if tasks:
        print(f"Loaded {len(tasks)} saved task(s) from {TASKS_FILE}.")

    while True:
        print("\n1. Add   2. View   3. Complete   4. Delete   5. Exit")
        try:
            choice = input("Choice: ").strip()
        except EOFError:           # input stream closed (for example when piping a test)
            print("\nGoodbye!")
            break

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
