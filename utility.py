import pickle
from termcolor import colored
import os

class Task:
    def __init__(self, task_name, assignee, reporter, deadline, priority):
        self.task_name = task_name
        self.assignee = assignee
        self.reporter = reporter
        self.deadline = deadline
        self.priority = priority

    def add_status_field(self, field_name, field_value):
        setattr(self, field_name, field_value)

    def display(self):
        print("Task:", self.task_name)
        print("Assignee:", self.assignee)
        print("Reporter:", self.reporter)
        print("Deadline:", self.deadline)
        print("Priority: ", self.priority)

class Kanban:
    def __init__(self, name):
        self.name = name
        self.task_list = []

    def display_tasks(self):
        if len(self.task_list) != 0:
            # Sort tasks by priority
            priority_order = {"high": 3, "medium": 2, "low": 1}
            self.task_list.sort(key=lambda x: priority_order.get(x.priority.lower(), 0), reverse=True)
            for i in self.task_list:
                print()
                i.display()
        else:
            print("No Tasks Here")

    def display(self, color):
        print()
        print("--------------------------------------------------------------------")
        print(colored(self.name, color))
        self.display_tasks()
        print("--------------------------------------------------------------------")
        print()

    def move_task(self, task_name, destination_board):
        task = self.find_task(task_name)
        if task:
            destination_board.task_list.append(task)
            self.task_list.remove(task)
            print(f"Task '{task_name}' moved to {destination_board.name}")
        else:
            print(f"Task '{task_name}' not found in {self.name}")

    def find_task(self, task_name):
        for task in self.task_list:
            if task.task_name == task_name:
                return task
        return None
    
    def remove_task(self, task_name):
        task = self.find_task(task_name)
        if task:
            self.task_list.remove(task)
            print(f"Task '{task_name}' removed from {self.name}")
        else:
            print(f"Task '{task_name}' not found in {self.name}")

def create_task():
    name = input("Enter Task Name: ")
    assignee = input("Enter Task Assignee: ")
    reporter = input("Enter Task Reporter: ")
    deadline = input("Enter Task Deadline: ")
    while True:
        priority = input("Enter Task Priority (high/medium/low): ").lower()
        if priority in {"high", "medium", "low"}:
            break
        else:
            print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
    print()
    return Task(name, assignee, reporter, deadline, priority)

def display_kanban_boards(todo, prog, done):

    todo.display("red")
    prog.display("yellow")
    done.display("green")

def save_data(todo, prog, done):
    with open("kanban_data.pickle", "wb") as f:
        pickle.dump((todo, prog, done), f)

def load_data():
    try:
        with open("kanban_data.pickle", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("No previous data found.")
        return None, None, None
    
def move_task_between_boards(todo, prog, done):
    task_name = input("Enter task name to move: ")
    source_board_name = input("Enter source board (TODO, In Progress, Done): ")
    destination_board_name = input("Enter destination board (TODO, In Progress, Done): ")
    source_board = None
    destination_board = None
    if source_board_name.lower() == "todo":
        source_board = todo
    elif source_board_name.lower() == "in progress":
        source_board = prog
    elif source_board_name.lower() == "done":
        source_board = done
    else:
        print("Invalid source board.")

    if destination_board_name.lower() == "todo":
        destination_board = todo
    elif destination_board_name.lower() == "in progress":
        destination_board = prog
    elif destination_board_name.lower() == "done":
        destination_board = done
    else:
        print("Invalid destination board.")

    if source_board and destination_board:
        source_board.move_task(task_name, destination_board)
def wipe_data():
    try:
        os.remove("kanban_data.pickle")
        print("Data wiped successfully.")
    except FileNotFoundError:
        print("No data file found.")
