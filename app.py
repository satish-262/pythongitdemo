from flask import Flask, render_template, request, jsonify
import json, os

app = Flask(__name__)
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE) as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    data = request.get_json()
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "text": data["text"], "done": False})
    save_tasks(tasks)
    return jsonify({"status": "ok"})

@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
    save_tasks(tasks)
    return jsonify({"status": "ok"})

@app.route("/delete/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
