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
    for task in tasks:
        print(f"[{task["id"]}] {task["description"]} ({task["status"]}) - {task["createdAt"]}")

elif sys.argv[1] == "delete":
    tasks = load_tasks()
    found = False
    
    for task in tasks:
        if int(sys.argv[2]) == task["id"]:
            found = True
            tasks.remove(task)
            save_tasks(tasks)
            print(f"{task["description"]} deleted successfully.")
    if not found:
        print("Task ID doesn't exist.")

elif sys.argv[1] == "update":
    tasks = load_tasks()
    found = False

    for task in tasks:
        if int(sys.argv[2]) == task["id"]:
            found = True
            task["description"] = sys.argv[3]
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task: [{task["id"]}] {task["description"]} updated successfully at {task["updatedAt"]}.")
    if not found:
        print("Task doesn't exist.")

else:
    print("Unknown command")





    
