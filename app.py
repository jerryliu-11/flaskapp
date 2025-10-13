from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

todos = []

#ewfewtw4 


class Todo:
    def __init__(self, title, description=""):
        self.id = len(todos) + 1
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now()

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    description = request.form.get('description', '')
    if title:
        todo = Todo(title, description)
        todos.append(todo)
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    for todo in todos:
        if todo.id == todo_id:
            todo.completed = True
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)