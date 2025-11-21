import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            return tasks
    except:
        return []

def save_tasks(tasks):
    try:
        with open("tasks.json", "w") as f:
            json.dump(tasks, f, indent=4)
    except:
        print("Error Saving Tasks!")

def add_task():
    tasks = load_tasks()
    text = input("Enter Your Tasks: ")
    if text.strip() == "":
        return 
    if tasks == []:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1
    new_task = {"id": new_id, "text": text, "completed": False}
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task Added!")

def view_tasks():
    tasks = load_tasks()
    if tasks == []:
        print("No tasks found!\n")
        return 
    for task in tasks:
        if task["completed"]:
            symbol = "Y"
        else:
            symbol = "X"
        print(f"{task["id"]}.{task["text"]} [{symbol}]")

def del_task():
    del_id = int(input("Enter the task ID to delete: "))
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == del_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Tasks deleted!")
            return 
    print("Task not found")
    return 

def mark_done():
    done_id = int(input("Enter the task ID to mark as Completed: "))
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == done_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked as done!")
            return
    print("Task not found")
    return 
