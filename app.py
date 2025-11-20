import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            return tasks
    except:
        return []

