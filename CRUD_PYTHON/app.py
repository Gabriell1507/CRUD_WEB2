from flask import Flask, request, render_template, redirect, url_for

# Criação da aplicação Flask
app = Flask(__name__)

# Simulando um banco de dados em memória
tasks = []  # Lista para armazenar as tarefas
task_id_counter = 1  # Contador para atribuir IDs às tarefas

# Definição da classe Task para representar uma tarefa
class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Rota para adicionar uma nova tarefa
@app.route('/add', methods=['POST'])
def add_task():
    global task_id_counter
    title = request.form.get('title')
    description = request.form.get('description')
    task = Task(task_id_counter, title, description)  # Criação da nova tarefa
    tasks.append(task)  # Adiciona a tarefa à lista
    task_id_counter += 1  # Incrementa o contador de IDs
    return redirect(url_for('index'))  # Redireciona de volta para a página inicial

# Rota para editar uma tarefa existente
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((t for t in tasks if t.id == task_id), None)  # Procura a tarefa pelo ID
    if task is None:
        return "Task not found", 404

    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        return redirect(url_for('index'))

    return render_template('edit.html', task=task)

# Rota para deletar uma tarefa
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]  # Remove a tarefa com o ID fornecido
    return redirect(url_for('index'))

# Execução da aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor de desenvolvimento do Flask
git