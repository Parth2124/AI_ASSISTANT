import sqlite3

DB_NAME = "tasks.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        due_date TEXT,
        priority TEXT,
        category TEXT,
        status TEXT DEFAULT 'pending'
    );
    """)
    conn.commit()
    return conn


def add_task(conn, title, due_date, priority, category):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO tasks (title, due_date, priority, category)
        VALUES (?, ?, ?, ?)
    """, (title, due_date, priority, category))
    conn.commit()


def get_pending_tasks(conn):
    cur = conn.cursor()
    return cur.execute("""
        SELECT id, title, due_date, priority, category, status 
        FROM tasks WHERE status='pending'
    """).fetchall()


def complete_task(conn, task_id):
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET status='done' WHERE id=?", (task_id,))
    conn.commit()

def get_completed_tasks(conn):
    cur = conn.cursor()
    return cur.execute("SELECT * FROM tasks WHERE status='done'").fetchall()
