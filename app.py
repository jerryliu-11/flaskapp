from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

todos = []

class Todo:
    """
    A simple Todo item class for managing task information.

    This class represents a single todo item with an auto-incremented ID,
    title, optional description, completion status, and creation timestamp.

    Attributes:
        id (int): Auto-generated unique identifier based on list length
        title (str): The title/name of the todo item
        description (str): Optional detailed description of the todo
        completed (bool): Flag indicating if the todo is completed
        created_at (datetime): Timestamp when the todo was created
    """

    def __init__(self, title, description=""):
        """
        Initialize a new Todo item.

        Creates a new todo with an auto-incremented ID based on the current
        length of the global todos list. Sets the initial completion status
        to False and records the creation timestamp.

        @param title: The title of the todo item
        @type title: str
        @param description: Optional description providing more details (default: "")
        @type description: str

        @example
        >>> todo = Todo("Buy groceries", "Milk, eggs, bread")
        >>> print(todo.title)
        'Buy groceries'
        >>> print(todo.completed)
        False
        """
        self.id = len(todos) + 1
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now()

@app.route('/')
def index():
    """
    Render the main index page with all todos.

    This route handler serves the home page of the application, displaying
    all todo items stored in the global todos list. It renders the index.html
    template and passes the todos list as context.

    @returns: Rendered HTML template with todos list
    @rtype: str

    @example
    # When user navigates to http://127.0.0.1:5000/
    # Returns the rendered index.html page with all current todos
    """
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    """
    Add a new todo item to the list.

    This route handler processes POST requests to create new todo items.
    It extracts the title and optional description from the form data,
    creates a new Todo object if the title is provided, and adds it to
    the global todos list. After processing, it redirects to the index page.

    @param title: Todo title from request.form (required)
    @type title: str
    @param description: Todo description from request.form (optional)
    @type description: str

    @returns: Redirect response to the index page
    @rtype: werkzeug.wrappers.Response

    @example
    # POST request with form data:
    # {'title': 'Write documentation', 'description': 'Add docstrings to all functions'}
    # Creates a new Todo and redirects to home page
    """
    title = request.form.get('title')
    description = request.form.get('description', '')
    if title:
        todo = Todo(title, description)
        todos.append(todo)
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    """
    Mark a specific todo item as completed.

    This route handler marks a todo as completed by setting its completed
    attribute to True. It searches through the todos list for a matching ID
    and updates the first match found. If no matching todo is found, no
    action is taken. After processing, it redirects to the index page.

    @param todo_id: The unique identifier of the todo to mark as complete
    @type todo_id: int

    @returns: Redirect response to the index page
    @rtype: werkzeug.wrappers.Response

    @example
    # GET request to /complete/3
    # Finds todo with id=3 and sets completed=True
    # Redirects to home page
    """
    for todo in todos:
        if todo.id == todo_id:
            todo.completed = True
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    """
    Delete a specific todo item from the list.

    This route handler removes a todo from the global todos list by filtering
    out any todo with a matching ID. It uses list comprehension to create a
    new list excluding the specified todo. After deletion, it redirects to
    the index page.

    @param todo_id: The unique identifier of the todo to delete
    @type todo_id: int

    @returns: Redirect response to the index page
    @rtype: werkzeug.wrappers.Response

    @example
    # GET request to /delete/3
    # Removes todo with id=3 from the todos list
    # Redirects to home page
    """
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)