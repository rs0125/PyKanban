import sys
from termcolor import colored, cprint

class kanban:
    task_list = []
    def __init__(self, name):
        self.name = name

    def display_tasks(self):
        if len(self.task_list) != 0:
            for i in self.task_list:
                print()
                print(i)
        else:
            print("No Tasks Here")

    def display(self, color):
        print()
        print("--------------------------------------------------------------------")
        print(colored(self.name, color))
        self.display_tasks()
        print("--------------------------------------------------------------------")
        print()

def kanban_display(todo, prog, done):
    todo.display("red")
    prog.display("yellow")
    done.display("green")

class Task:
    def __init__(self, task_name, assignee, reporter, deadline, priority):
        self.task_name = task_name
        self.assignee = assignee
        self.reporter = reporter
        self.deadline = deadline
        self.priority = priority

    def add_status_field(self, field_name, field_value):
        setattr(self, field_name, field_value)

def task_input():
    name = input("Enter Task Name")
    assignee = input("Enter Task Assignee")
    reporter = input("Enter Task Reporter")
    deadline = input("Enter Task Deadline")
    priority = input("Enter Task Priority")

todo = kanban("TODO")
prog = kanban("In Progress")
done = kanban("Done")

kanban_display(todo, prog, done)
