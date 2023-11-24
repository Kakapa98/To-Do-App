import json
from datetime import datetime, timedelta

tasks_file = "tasks.txt"

def load_tasks():
    """
    Load tasks from a text file.

    Returns:
        list: List of tasks loaded from the file.

    Instructions:
        1. Use a 'try' block to attempt opening the tasks file in read mode.
        2. Inside the 'try' block, use 'json.load(file)' to load the tasks from the file.
        3. If the file is not found (FileNotFoundError), catch the exception and return an empty list.
    """
    pass

def save_tasks():
    """
    Save tasks to a text file.

    Instructions:
        1. Open the specified file (tasks_file) in write mode using the 'with' statement.
        2. Use the json.dump() function to write the current tasks list to the file in JSON format.
        3. The 'w' mode ensures that the file is opened for writing, creating a new file if it doesn't exist.
        4. This operation overwrites the existing content of the file with the serialized JSON representation of the tasks.
    """
    pass

tasks = load_tasks()

def add_task():
    """
    Add a new task to the to-do list.

    User Input:
        str: Task name entered by the user.

    Instructions:
        1. Receive input for the task name from the user.
        2. Check if the task name is not empty.
        3. If the task name is not empty, add a new task to the to-do list with the provided name and 'Not Done' status.
        4. Save the updated task list to the file.
        5. Print a message indicating the success or failure of the operation.
    """
    pass

def mark_done():
    """
    Mark a task as done from the to-do list.

    User Input:
        int: Task number to mark as done.

    Instructions:
        1. Display the list of tasks with their status.
        2. Receive input for the task number to mark as done from the user.
        3. Check if the input is a valid integer within the range of available tasks.
        4. If valid, mark the selected task as done and save the updated task list to the file.
        5. Print a message indicating the success or failure of the operation.
        6. If the input is not a valid integer, handle the exception and print an error message.
    """
    pass

def view_tasks():
    """
    View all tasks in the to-do list.

    Instructions:
        1. Display the list of tasks with their status.
    """
    pass

def main_menu():
    """
    Display the main menu and handle user choices.

    Instructions:
        1. Display the available options in the main menu.
        2. Receive input for the user's choice.
        3. Based on the user's choice, call the corresponding function (add_task, mark_done, view_tasks, or exit).
        4. Repeat the process until the user chooses to exit.
    """
    pass

if __name__ == "__main__":
    print("Welcome to the To-Do List App!")
    main_menu()
