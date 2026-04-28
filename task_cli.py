import sys
import json
import os

arguments = sys.argv # List of arguments

if sys.argv[1] == "add":
    load_tasks()
else:
    print("Unknown command")

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            data = json.load(file)
            return data
    else:
        return []
    
