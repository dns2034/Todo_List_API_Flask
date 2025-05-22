from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []

# this route returns the list of current todos in JSON format
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# this route receives a new todo item via JSON in the request body and appends it to the 'todos' list
@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json.get('todo')
    if todo:
        todos.append(todo)
        return jsonify({"message": "Todo added successfully.", "todos": todos}), 201
    else:
        return jsonify({"error": "No todo provided."}), 400

if __name__ == '__main__':
    app.run(debug=True)