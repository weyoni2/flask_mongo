from app import app
from flask import render_template
from app.models import Todo
from flask.globals import request


@app.route('/')
def index():
    todos = Todo.objects.all()
    return render_template("to_dos.html", todos=todos)

@app.route('/add', methods=['POST', ])
def add():
    content = request.form.get("content")
    todo = Todo(content=content)
    todo.save()
    todos = Todo.objects.all()
    return render_template("to_dos.html", todos=todos)