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
else:
    print("Unknown command")




    
