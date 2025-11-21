# To-Do List App (Python CLI)

A simple command-line To‑Do List app built with Python. It lets you add, view, delete, and mark tasks as completed. Your tasks are saved in a `tasks.json` file so they persist between runs.

---

## 📌 Features

* Add new tasks
* View all tasks with completion status
* Delete tasks by ID
* Mark tasks as completed
* Persistent storage using JSON

---

## 🚀 How to Run

1. Make sure Python is installed on your system.
2. Place the script and an optional `tasks.json` file in the same folder.
3. Run the script:

```bash
python your_script_name.py
```

---

## 📂 File Structure

```
project_folder/
│── tasks.json       # Stores your tasks
│── script.py        # The main program
```

---

## 📝 Usage

When you run the script, you'll see a menu like this:

```
----MENU----
1.Add
2.View
3.Delete
4.Mark Done
5.Exit
```

Choose an option by typing the number.

### ➕ Add Task

Enter a task description to create a new task.

### 👀 View Tasks

Displays tasks in this format:

```
1.Buy milk [X]
2.Complete homework [Y]
```

`X` → Not completed
`Y` → Completed

### ❌ Delete Task

Enter the task ID to delete it.

### ✔ Mark as Done

Enter the task ID to mark it as completed.

---

## 🛠 How It Works

### `tasks.json`

Stores tasks as a list of dictionaries:

```json
[
  {
    "id": 1,
    "text": "Sample task",
    "completed": false
  }
]
```

### Incremental IDs

IDs auto-increment based on the last task.

---

## 📌 Notes

* If `tasks.json` doesn't exist, it's created automatically.
* Empty input for task text is ignored.
* Invalid IDs show an error instead of crashing.

---

## 🤝 Contributions

Feel free to improve the program or add new features.

---

## 📄 License

This project is free to use and modify.
