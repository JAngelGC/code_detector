from flask import Blueprint, jsonify, request, abort

tasks = Blueprint('tasks', __name__)

# Sample data
tasks_data = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Flask',
        'description': 'Need to find a good tutorial on the web',
        'done': False
    }
]

# Get all tasks
@tasks.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks_data})

# Get a single task
@tasks.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks_data if task['id'] == task_id), None)
    if task is None:
        abort(404)
    return jsonify({'task': task})

# Create a new task
@tasks.route('/', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    new_task = {
        'id': tasks_data[-1]['id'] + 1 if tasks_data else 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks_data.append(new_task)
    return jsonify({'task': new_task}), 201

# Update an existing task
@tasks.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks_data if task['id'] == task_id), None)
    if task is None:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) is not str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)

    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify({'task': task})

# Delete a task
@tasks.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks_data if task['id'] == task_id), None)
    if task is None:
        abort(404)
    tasks_data.remove(task)
    return jsonify({'result': True})
