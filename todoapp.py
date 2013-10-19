__author__ = 'Modulus'

from flask import Flask
from flask.ext import restful
from flask.ext.restful import (reqparse, abort, fields, marshal_with,
                               marshal)

app = Flask(__name__)
api = restful.Api(app)

TODOS = [
    { 'task': 'build an API' },
    { 'task': '?????', 'otherField': 'secret data!',},
    { 'task': 'profit!'},
    ]

#only output the task field


fields = {
    'task': fields.String
}

# Todo
#   show a single todo item and lets you delete them
class Todo(restful.Resource):
    @marshal_with(fields)
    def get(self, todo_id):
        if not(len(TODOS) > todo_id > 0) or TODOS[todo_id] is None:
            abort(404, message="Todo {} doesn't exist".format(todo_id))
        return TODOS[todo_id]

    def delete(self, todo_id):
        if not(len(TODOS) > todo_id > 0):
            abort(404, message="Todo {} doesn't exist".format(todo_id))
        TODOS[todo_id] = None
        return "", 204

# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

class TodoList(restful.Resource):
    @marshal_with(fields)
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS.append(task)
        return marshal(task, fields), 201

## Actually setup the Api resource routing here
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/')

if __name__ == '__main__':
    app.run(debug=True)
