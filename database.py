import sqlite3

class Database:
    def __init__(self, db_name='todos.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    done BOOLEAN NOT NULL CHECK (done IN (0, 1))
                )
            ''')

    def query(self, query, args=(), one=False):
        cur = self.conn.execute(query, args)
        rv = [dict((cur.description[idx][0], value)
                   for idx, value in enumerate(row)) for row in cur.fetchall()]
        return (rv[0] if rv else None) if one else rv

    def execute(self, query, args=()):
        with self.conn:
            self.conn.execute(query, args)
