import sys
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

def main():
    todo = Kanban("TODO")
    prog = Kanban("In Progress")
    done = Kanban("Done")

    while True:
        print("Select an action:")
        print("1. Add Task")
        print("2. Move Task")
        print("3. Display Kanban Board")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = create_task()
            todo.task_list.append(task)
            print("Task added to TODO board.")
        elif choice == "2":
            task_name = input("Enter task name to move: ")
            destination_board_name = input("Enter destination board (TODO, In Progress, Done): ")
            if destination_board_name.lower() == "todo":
                todo.move_task(task_name, todo)
                display_kanban_boards(todo, prog, done)
            elif destination_board_name.lower() == "in progress":
                todo.move_task(task_name, prog)
                display_kanban_boards(todo, prog, done)
            elif destination_board_name.lower() == "done":
                todo.move_task(task_name, done)
                display_kanban_boards(todo, prog, done)
            else:
                print("Invalid destination board.")
        elif choice == "3":
            display_kanban_boards(todo, prog, done)
        elif choice == "4":
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
