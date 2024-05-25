import sqlite3

class Database:
    """
    A class to represent a database connection and operations for a TODO application.
    """

    def __init__(self, db_name='todos.db'):
        """
        Initialize the Database with a given database name and create the table if it doesn't exist.

        :param db_name: The name of the database file (default is 'todos.db').
        """
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        """
        Create the todos table if it does not already exist.
        """
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
        """
        Execute a query and return the results.

        :param query: The SQL query to execute.
        :param args: The arguments to substitute into the query.
        :param one: Whether to return only one result (default is False).
        :return: The result(s) of the query as a list of dictionaries.
        """
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.execute(query, args)
            rv = [dict((cur.description[idx][0], value)
                       for idx, value in enumerate(row)) for row in cur.fetchall()]
            return (rv[0] if rv else None) if one else rv

    def execute(self, query, args=()):
        """
        Execute a query that modifies the database.

        :param query: The SQL query to execute.
        :param args: The arguments to substitute into the query.
        """
        with sqlite3.connect(self.db_name) as conn:
            conn.execute(query, args)

    def print_all_todos(self):
        """
        Print all TODOs in the database to the console.
        """
        todos = self.query('SELECT * FROM todos')
        for todo in todos:
            print(todo)
