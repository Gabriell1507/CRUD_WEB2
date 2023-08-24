from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Simulando um banco de dados em memória
tasks = []
task_id_counter = 1

class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global task_id_counter
    title = request.form.get('title')
    description = request.form.get('description')
    task = Task(task_id_counter, title, description)
    tasks.append(task)
    task_id_counter += 1
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((t for t in tasks if t.id == task_id), None)
    if task is None:
        return "Task not found", 404

    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        return redirect(url_for('index'))

    return render_template('edit.html', task=task)

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
