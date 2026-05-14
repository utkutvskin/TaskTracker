import sys
import json
import os
from datetime import datetime

arguments = sys.argv # List of arguments

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            data = json.load(file)
            return data
    else:
        return []
    
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    
def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None
    
if sys.argv[1] == "add":
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": sys.argv[2],
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": None
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully: {new_task['description']}")

elif sys.argv[1] == "list":
    tasks = load_tasks()
    status_filter = sys.argv[2] if len(sys.argv) > 2 else None
    for task in tasks:
        if status_filter is None or task["status"] == status_filter:
            print(f"[{task["id"]}] {task["description"]} ({task["status"]}) - {task["createdAt"]}")


elif sys.argv[1] == "delete":
    tasks = load_tasks()
    task = find_task(tasks, int(sys.argv[2]))
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"{task["description"]} deleted successfully.")
    else:
        print("Task doesn't exist.")

elif sys.argv[1] == "update":
    tasks = load_tasks()
    task = find_task(tasks, int(sys.argv[2]))

    if task:
        task["description"] = sys.argv[3]
        task["updatedAt"] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task: [{task["id"]}] {task["description"]} updated successfully at {task["updatedAt"]}.")
    else:
        print("Task doesn't exist.")

elif sys.argv[1] == "mark-done":
    tasks = load_tasks()
    task = find_task(tasks, int(sys.argv[2]))

    if task:
        task["status"] = "done"
        save_tasks(tasks)
        print(f"Task: {task["description"]} marked as done.")
    else:
        print("Task doesn't exist.")

elif sys.argv[1] == "mark-in-progress":
    tasks = load_tasks()
    task = find_task(tasks, int(sys.argv[2]))

    if task:
        task["status"] = "in-progress"
        save_tasks(tasks)
        print(f"Task: {task["description"]} marked as in progress.")
    else:
        print("Task doesn't exist.")
else:
    print("Unknown command")





    
