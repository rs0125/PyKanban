import sys
from termcolor import colored, cprint

class kanban:
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

    def display(self):
        print("Task:", self.task_name)
        print("Assignee:", self.assignee)
        print("Reporter:", self.reporter)
        print("Deadline:", self.deadline)
        # Display additional status fields
        for attr_name in dir(self):
            if not attr_name.startswith('__') and not callable(getattr(self, attr_name)):
                print(f"{attr_name.capitalize()}: {getattr(self, attr_name)}")

def indiv_input():
    name = input("Enter Task Name")
    assignee = input("Enter Task Assignee")
    reporter = input("Enter Task Reporter")
    deadline = input("Enter Task Deadline")
    priority = input("Enter Task Priority")
    print()
    return Task(name, assignee, reporter, deadline, priority)

def kanban_input(Table):
    Table.task_list.append(indiv_input())


todo = kanban("TODO")
prog = kanban("In Progress")
done = kanban("Done")
kanban_input(todo)

# Displaying the task details

kanban_display(todo, prog, done)
