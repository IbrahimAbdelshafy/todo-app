from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage (Phase 1 only)
todos = []

@app.route("/status", methods=["GET"])
def status():
    return "OK", 200

@app.route("/todos", methods=["GET"])
def list_todos():
    return jsonify(todos), 200

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()

    if not data or "title" not in data:
        return {"error": "title is required"}, 400

    todo = {
        "id": len(todos) + 1,
        "title": data["title"]
    }
    todos.append(todo)

    return todo, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

