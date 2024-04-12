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

## File Structure

```
kanban-board/
│
├── main.py             # Main script containing the CLI interface
├── utility.py      # Utility functions for Kanban board management
└── kanban_data.pickle  # Binary file for storing Kanban board data
```

## Documentation

- **`main.py`**: Contains the main script with the CLI interface. Users interact with the Kanban board through this script.
- **`kanban_util.py`**: Contains utility functions for Kanban board management, including task creation, data storage, and board manipulation.
- **`kanban_data.pickle`**: Binary file for storing Kanban board data. Tasks and board configurations are saved here for persistence between sessions.
