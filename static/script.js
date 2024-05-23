document.addEventListener('DOMContentLoaded', fetchTodos);

function fetchTodos() {
    fetch('/todos')
        .then(response => response.json())
        .then(data => {
            const todoList = document.getElementById('todo-list');
            todoList.innerHTML = '';
            data.forEach(todo => {
                const li = document.createElement('li');
                li.innerHTML = `
                    ${todo.title} - ${todo.description}
                    <button onclick="deleteTodo(${todo.id})">Delete</button>
                    <button onclick="updateTodoPrompt(${todo.id})">Update</button>
                `;
                todoList.appendChild(li);
            });
        });
}

function addTodo() {
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;

    fetch('/todos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, description })
    })
    .then(response => response.json())
    .then(data => {
        fetchTodos();
        document.getElementById('title').value = '';
        document.getElementById('description').value = '';
    });
}

function deleteTodo(id) {
    fetch(`/todos/${id}`, {
        method: 'DELETE'
    })
    .then(() => {
        fetchTodos();
    });
}

function updateTodoPrompt(id) {
    const title = prompt('Enter new title:');
    const description = prompt('Enter new description:');
    if (title !== null && description !== null) {
        updateTodo(id, title, description);
    }
}

function updateTodo(id, title, description) {
    fetch(`/todos/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, description, done: false })
    })
    .then(response => response.json())
    .then(() => {
        fetchTodos();
    });
}
