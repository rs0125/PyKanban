from termcolor import colored  # Import colored function from termcolor module
from utility import *  # Import all functions and classes from utility module


def main():
    # Load existing data or create new instances of Kanban boards if data does not exist
    todo, prog, done = load_data()
    if todo is None:
        todo = Kanban("TODO")
    if prog is None:
        prog = Kanban("In Progress")
    if done is None:
        done = Kanban("Done")

    while True:
        # Display menu options
        print("Select an action:")
        print("1. Add Task")
        print("2. Move Task")
        print("3. Display Kanban Board")
        print("4. Save Data")
        print("5. Remove Task")
        print("6. Wipe Data")
        print("7. Exit")

        # Prompt user for choice
        choice = input("Enter your choice: ")

        # Perform actions based on user choice
        if choice == "1":  # Add Task
            task = create_task()  # Create a new task
            todo.task_list.append(task)  # Add the task to the TODO board
            print("Task added to TODO board.")
            display_kanban_boards(todo, prog, done)  # Display updated Kanban boards

        elif choice == "2":  # Move Task
            move_task_between_boards(todo, prog, done)  # Move a task between boards

        elif choice == "3":  # Display Kanban Board
            display_kanban_boards(todo, prog, done)  # Display Kanban boards

        elif choice == "4":  # Save Data
            save_data(todo, prog, done)  # Save Kanban board data to file
            print(colored(("Data saved successfully."), "blue"))  # Print confirmation message

        elif choice == "5":  # Remove Task
            board_name = input("Enter board name (TODO, In Progress, Done): ")
            task_name = input("Enter task name to remove: ")
            if board_name.lower() == "todo":
                todo.remove_task(task_name)  # Remove task from the TODO board
            elif board_name.lower() == "in progress":
                prog.remove_task(task_name)  # Remove task from the In Progress board
            elif board_name.lower() == "done":
                done.remove_task(task_name)  # Remove task from the Done board
            else:
                print("Invalid board name.")

        elif choice == "6":
            wipe_data() #Deletes the pickle file

        elif choice == "7":  # Exit
            print("Exiting program.")
            exit()

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
