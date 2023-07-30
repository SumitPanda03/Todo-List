from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/todos'
mongo = PyMongo(app)

todos = mongo.db.todos


@app.route('/')
def index():
    saved_todos = todos.find()
    # return dumps(saved_todos)
    return render_template('index.html', todos=saved_todos)


@app.route('/add', methods=['POST'])
def add_todo():
    new_todo = request.form.get('new-todo')
    todos.insert_one({'text': new_todo, 'complete': False})
    # return dumps(new_todo)
    return redirect(url_for('index'))


@app.route('/complete/<oid>')
def complete(oid):
    # todo_item = todos.find_one({'_id': ObjectId(oid)})
    # todo_item['complete'] = True
    todos.update_one({'_id': ObjectId(oid)}, {'$set': {'complete': True}})
    return redirect(url_for('index'))


@app.route('/delete_completed')
def delete_completed():
    todos.delete_many({'complete': True})
    return redirect(url_for('index'))


@app.route('/delete_all')
def delete_all():
    todos.delete_many({})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
