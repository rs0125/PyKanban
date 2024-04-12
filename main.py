import sys
import pickle
from termcolor import colored
from utility import *


def main():
    todo, prog, done = load_data()
    if todo is None:
        todo = Kanban("TODO")
    if prog is None:
        prog = Kanban("In Progress")
    if done is None:
        done = Kanban("Done")

    while True:
        print("Select an action:")
        print("1. Add Task")
        print("2. Move Task")
        print("3. Display Kanban Board")
        print("4. Save Data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = create_task()
            todo.task_list.append(task)
            print("Task added to TODO board.")
            display_kanban_boards(todo, prog, done)
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
            save_data(todo, prog, done)
            print(colored(("Data saved successfully."),"blue"))
        elif choice == "5":
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
