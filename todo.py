from database import Database

class TodoManager:
    """
    A class to manage TODO operations using a database.
    """

    def __init__(self):
        """
        Initialize the TodoManager with a database connection.
        """
        self.db = Database()

    def get_todos(self):
        """
        Retrieve all TODO items from the database.

        :return: A list of dictionaries, each representing a TODO item.
        """
        return self.db.query('SELECT * FROM todos')

    def add_todo(self, title, description=''):
        """
        Add a new TODO item to the database.

        :param title: The title of the TODO item.
        :param description: The description of the TODO item (default is an empty string).
        :return: The newly added TODO item as a dictionary.
        """
        self.db.execute('INSERT INTO todos (title, description, done) VALUES (?, ?, ?)', (title, description, False))
        return self.db.query('SELECT * FROM todos ORDER BY id DESC LIMIT 1', one=True)

    def update_todo(self, todo_id, title, description='', done=False):
        """
        Update an existing TODO item in the database.

        :param todo_id: The ID of the TODO item to update.
        :param title: The new title of the TODO item.
        :param description: The new description of the TODO item (default is an empty string).
        :param done: The completion status of the TODO item (default is False).
        :return: The updated TODO item as a dictionary.
        """
        self.db.execute('UPDATE todos SET title = ?, description = ?, done = ? WHERE id = ?', (title, description, done, todo_id))
        return self.db.query('SELECT * FROM todos WHERE id = ?', (todo_id,), one=True)

    def delete_todo(self, todo_id):
        """
        Delete a TODO item from the database.

        :param todo_id: The ID of the TODO item to delete.
        :return: True if the TODO item was successfully deleted.
        """
        self.db.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
        return True
