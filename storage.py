# how data is loaded/stored
# Where is the data stored?
# How do we read/write it?
# It does NOT care what a task means
# Important so if we change storage to SQLite, we just swap out this file instead of having to rework everything
# storage.py
# “How do I talk to the database?”
# taskmanager.py
# “What should happen in the app?”
import sqlite3

DB_NAME = "tasks.db"

#initialize db as first step in program
def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_title TEXT NOT NULL,
            task_completed BOOLEAN NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def insert_task(task_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (task_title, task_completed) VALUES (?, ?)",
        (task_name, False)
    )
    conn.commit()
    conn.close()


def get_all_tasks():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall() 
    cursor.close()
    conn.close()
    return rows

#like renaming task name
def update_task_title(task_ID, task_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # prepare sql query
    sql_query = "UPDATE tasks SET task_title = ? WHERE task_id = ?"
    cursor.execute(sql_query, (task_name, task_ID))
    conn.commit()
    cursor.close()
    conn.close()

def mark_task_completed(task_ID):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # prepare sql query
    sql_query = "UPDATE tasks SET task_completed = TRUE WHERE task_id = ?"
    cursor.execute(sql_query, (task_ID,))
    conn.commit()
    cursor.close()
    conn.close()

def delete_task(task_ID):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    sql_delete_query = "DELETE FROM tasks WHERE task_id = ?"
    cursor.execute(sql_delete_query, (task_ID,))
    conn.commit()
    cursor.close()
    conn.close()

