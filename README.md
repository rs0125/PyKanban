# PyKanban
This project is a command-line interface (CLI) based Kanban board implemented in Python. It allows users to manage tasks across different boards, including "TODO," "In Progress," and "Done."

## Features

- **Add Task**: Users can add tasks to the Kanban board.
- **Move Task**: Tasks can be moved between different boards.
- **Display Board**: Users can display tasks on each board.
- **Save and Load Data**: Data can be saved to and loaded from binary files to persist tasks between sessions.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/kanban-board.git
   ```

2. Install the required dependencies:

   ```bash
   pip install termcolor
   ```

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. Follow the on-screen prompts to interact with the Kanban board.


## File Structure Documentation

- **`main.py`**: Contains the main script with the CLI interface. Users interact with the Kanban board through this script.
- **`kanban_util.py`**: Contains utility functions for Kanban board management, including task creation, data storage, and board manipulation.
- **`kanban_data.pickle`**: Binary file for storing Kanban board data. Tasks and board configurations are saved here for persistence between sessions.

## Function Documentation

### `Task` class

#### `__init__(self, task_name, assignee, reporter, deadline, priority)`
- **Parameters:**
  - `task_name` (str): The name of the task.
  - `assignee` (str): The person assigned to the task.
  - `reporter` (str): The person reporting the task.
  - `deadline` (str): The deadline for the task.
  - `priority` (str): The priority of the task (high, medium, low).

#### `add_status_field(self, field_name, field_value)`
- **Parameters:**
  - `field_name` (str): The name of the additional status field.
  - `field_value` (str): The value of the additional status field.
- **Description:** Adds an additional status field to the task.

#### `display(self)`
- **Description:** Displays the details of the task.

### `Kanban` class

#### `__init__(self, name)`
- **Parameters:**
  - `name` (str): The name of the Kanban board.
- **Description:** Initializes a new Kanban board with the given name.

#### `display_tasks(self)`
- **Description:** Displays all tasks in the Kanban board, sorted by priority.

#### `display(self, color)`
- **Parameters:**
  - `color` (str): The color of the Kanban board header.
- **Description:** Displays the Kanban board with a colored header.

#### `move_task(self, task_name, destination_board)`
- **Parameters:**
  - `task_name` (str): The name of the task to move.
  - `destination_board` (Kanban): The destination Kanban board.
- **Description:** Moves a task from the current board to the destination board.

#### `find_task(self, task_name)`
- **Parameters:**
  - `task_name` (str): The name of the task to find.
- **Returns:** The task object if found, otherwise `None`.
- **Description:** Finds a task in the Kanban board by name.

#### `remove_task(self, task_name)`
- **Parameters:**
  - `task_name` (str): The name of the task to remove.
- **Description:** Removes a task from the Kanban board.

### `create_task()`
- **Returns:** A new `Task` object created from user input.
- **Description:** Prompts the user to enter details for a new task and creates a `Task` object.

### `display_kanban_boards(todo, prog, done)`
- **Parameters:**
  - `todo` (Kanban): The TODO Kanban board.
  - `prog` (Kanban): The In Progress Kanban board.
  - `done` (Kanban): The Done Kanban board.
- **Description:** Displays all three Kanban boards with their respective tasks.

### `save_data(todo, prog, done)`
- **Parameters:**
  - `todo` (Kanban): The TODO Kanban board.
  - `prog` (Kanban): The In Progress Kanban board.
  - `done` (Kanban): The Done Kanban board.
- **Description:** Saves the data of all three Kanban boards to a pickle file.

### `load_data()`
- **Returns:** A tuple containing the TODO, In Progress, and Done Kanban boards.
- **Description:** Loads the data of all three Kanban boards from a pickle file.

### `move_task_between_boards(todo, prog, done)`
- **Parameters:**
  - `todo` (Kanban): The TODO Kanban board.
  - `prog` (Kanban): The In Progress Kanban board.
  - `done` (Kanban): The Done Kanban board.
- **Description:** Moves a task between Kanban boards based on user input.

### `wipe_data()`
- **Description:** Wipes all Kanban board data by removing the pickle file.

