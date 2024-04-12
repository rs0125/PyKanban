import sys
import pickle
from termcolor import colored

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
        # Display additional status fields
        for attr_name in dir(self):
            if not attr_name.startswith('__') and not callable(getattr(self, attr_name)):
                print(f"{attr_name.capitalize()}: {getattr(self, attr_name)}")

class Kanban:
    def __init__(self, name):
        self.name = name
        self.task_list = []

    def display_tasks(self):
        if len(self.task_list) != 0:
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

def create_task():
    name = input("Enter Task Name: ")
    assignee = input("Enter Task Assignee: ")
    reporter = input("Enter Task Reporter: ")
    deadline = input("Enter Task Deadline: ")
    priority = input("Enter Task Priority: ")
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
