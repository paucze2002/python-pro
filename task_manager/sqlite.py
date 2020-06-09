import sqlite3
# from tasks import Tasks

conn = sqlite3.connect('tasks.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS tasks (
        name text,
        date text,
        description text,
        hash text
        )""")


# task_1 = Tasks('Cleaning', '20-02-2020', 'Clean my room')

# c.execute("INSERT INTO tasks VALUES (?, ?, ?, ?)", (task_1.name, task_1.date, task_1.description, task_1.hash))
# conn.commit()


def list_tasks():
    # TODO: List not in bracelets
    with conn:
        c.execute("SELECT * FROM tasks")
        print(c.fetchall())


def list_tasks_today(day, month, year):
    # TODO: List not in bracelets
    with conn:
        c.execute("SELECT * FROM tasks WHERE date LIKE ?", (day + '%' + month + '%' + year,))
        print(c.fetchall())


def list_tasks_month(month, year):
    # TODO: List not in bracelets
    with conn:
        c.execute("SELECT * FROM tasks WHERE date LIKE ?", ('%' + month + '%' + year,))
        print(c.fetchall())


def add_task(task):
    with conn:
        c.execute("INSERT INTO tasks VALUES (:name, :date, :description, :hash)",
                  {'name': task.name, 'date': task.date, 'description': task.description, 'hash': task.hash})
        # TODO: List not in bracelets
        c.execute("SELECT * FROM tasks WHERE name=:name", {'name': task.name})
        print(c.fetchall())


def edit_task_name(task_hash, name):
    with conn:
        c.execute("UPDATE tasks SET name = :name WHERE hash = :hash", {'name': name, 'hash': task_hash})


def edit_task_date(task_hash, date):
    with conn:
        c.execute("UPDATE tasks SET date = :date WHERE hash = :hash", {'date': date, 'hash': task_hash})


def edit_task_description(task_hash, description):
    with conn:
        c.execute("UPDATE tasks SET description = :description WHERE hash = :hash",
                  {'description': description, 'hash': task_hash})
        print()


def delete_task(task_hash):
    with conn:
        c.execute("DELETE FROM tasks WHERE hash=:hash", {'hash': task_hash})


# conn.close()
