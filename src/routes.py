import asyncio
from flask import jsonify
from manage import app, db, ma
from schemas.TaskSchema import task_schema, tasks_schema
from models.Task import Task

@app.route('/task', methods=['POST'])
def create_task():
    title = request.json['title']
    description = request.json['description']
    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()
    return  task_schema.jsonify(new_task)

@app.route('/tasks')
def get_all_task():
    tasks = Task.query.all()
    return jsonify(tasks_schema.dump(tasks))

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_byId(id):
    task = Task.query.get(id)
    return task_schema.jsonify(task)

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    title = request.json['title']
    description = request.json['description']
    task.title = title
    task.description = description
    db.session.commit()
    return task_schema.jsonify(task)

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)

@app.route('/', methods=['GET', 'POST'])
def getData():
    data = {
        "data": ["lunes", "martes"]
    }
    return data