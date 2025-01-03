from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load todos from file
def load_todos():
    try:
        with open('todos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save todos to file
def save_todos(todos):
    with open('todos.json', 'w') as f:
        json.dump(todos, f)

# Get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(load_todos())

# Add new todo
@app.route('/todos', methods=['POST'])
def add_todo():
    todos = load_todos()
    new_todo = request.json
    new_todo['id'] = str(datetime.now().timestamp())
    new_todo['completed'] = False
    todos.append(new_todo)
    save_todos(todos)
    return jsonify(new_todo), 201

# Update todo
@app.route('/todos/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = request.json['completed']
            save_todos(todos)
            return jsonify(todo)
    return jsonify({'error': 'Todo not found'}), 404

# Delete todo
@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todos = load_todos()
    todos = [todo for todo in todos if todo['id'] != todo_id]
    save_todos(todos)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)