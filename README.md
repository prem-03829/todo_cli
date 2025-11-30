# To-Do CLI

A simple, persistent command-line task manager built with Python. It allows you to manage your daily tasks directly from the terminal, using a local JSON file to save your progress.

## Features

* **Add Tasks:** Quickly add new items to your list.
* **View Tasks:** See all your tasks with color-coded status (Red for pending, Green for completed).
* **Update & Delete:** Modify existing task text or remove tasks by ID.
* **Mark Done:** Toggle task status to completed.
* **Persistent Storage:** Automatically saves all data to `tasks.json`, so you don't lose your list when you close the program.

## Tech Stack

* **Python 3**
* **Colorama:** For colored terminal output.
* **JSON:** For local data storage.

## Folder Structure

```text
To_Do_CLI/
├── venv/                # Virtual environment
├── app.py               # Main application logic
├── requirements.txt     # Project dependencies
├── tasks.json           # Data file (created automatically)
└── README.md
```
## Installation

Clone the repository (if you haven't already):
```
git clone https://github.com/prem-03829/todo_cli.git
cd todo_cli
```
Set up a Virtual Environment (Recommended):
```
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

Install Dependencies:
```
pip install -r requirements.txt
```
## How to Run
Run the application using Python:
```
python app.py
```
## Menu Options

Once the app is running, choose an option by entering the corresponding number:

Add: Type your task description.

View: Lists all tasks with their IDs and current status.

Delete: Remove a task using its ID.

Update: Fix a typo or change a task description.

Mark Done: Check off a task using its ID.

Exit: Closes the application.

## Known Issues / TODO
- Add sorting options (completed first / pending first).
- Add timestamps for tasks.
- Add search functionality.
- Plan to add a "Clear All" feature in the future.