import sqlite3

class Database:
    def __init__(self, db_name='todos.db'):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    done BOOLEAN NOT NULL CHECK (done IN (0, 1))
                )
            ''')

    def query(self, query, args=(), one=False):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.execute(query, args)
            rv = [dict((cur.description[idx][0], value)
                       for idx, value in enumerate(row)) for row in cur.fetchall()]
            return (rv[0] if rv else None) if one else rv

    def execute(self, query, args=()):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute(query, args)

    def print_all_todos(self):
        todos = self.query('SELECT * FROM todos')
        for todo in todos:
            print(todo)
