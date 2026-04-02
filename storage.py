# how data is loaded/stored
# Where is the data stored?
# How do we read/write it?
# It does NOT care what a task means
# Important so if we change storage to SQLite, we just swap out this file instead of having to rework everything

import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)