from database import Database

class TodoManager:
    def __init__(self):
        self.db = Database()

    def get_todos(self):
        return self.db.query('SELECT * FROM todos')

    def add_todo(self, title, description=''):
        self.db.execute('INSERT INTO todos (title, description, done) VALUES (?, ?, ?)', (title, description, False))
        return self.db.query('SELECT * FROM todos ORDER BY id DESC LIMIT 1', one=True)

    def update_todo(self, todo_id, title, description='', done=False):
        self.db.execute('UPDATE todos SET title = ?, description = ?, done = ? WHERE id = ?', (title, description, done, todo_id))
        return self.db.query('SELECT * FROM todos WHERE id = ?', (todo_id,), one=True)

    def delete_todo(self, todo_id):
        self.db.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
        return True
