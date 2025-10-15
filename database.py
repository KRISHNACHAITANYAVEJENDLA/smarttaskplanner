import sqlite3

def init_db():
    conn = sqlite3.connect("planner.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            goal TEXT,
            task_name TEXT,
            description TEXT,
            dependencies TEXT,
            deadline TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_task(goal, task_name, desc, deps, deadline):
    conn = sqlite3.connect("planner.db")
    c = conn.cursor()
    c.execute("INSERT INTO tasks (goal, task_name, description, dependencies, deadline) VALUES (?, ?, ?, ?, ?)",
              (goal, task_name, desc, deps, deadline))
    conn.commit()
    conn.close()
