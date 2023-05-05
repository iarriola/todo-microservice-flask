import json
from flask import Flask, jsonify, request, make_response, redirect, render_template
from repositories.task_repository import TaskRepository

app = Flask(__name__)

repository = TaskRepository()

TASK_ROUTE = "/api/v1/tasks/:id"
TASKS_ROUTE = "/api/v1/tasks"


@app.route(TASK_ROUTE, methods=["GET"])
def get():
    return jsonify({"name": "alice", "email": "alice@outlook.com"})


@app.route(TASKS_ROUTE, methods=["GET"])
def get_all():
    result = repository.get_all()
    return jsonify(result), 200


@app.route(TASKS_ROUTE, methods=["POST"])
def post():
    return jsonify({"name": "alice", "email": "alice@outlook.com"})


@app.route(TASKS_ROUTE, methods=["PATCH"])
def patch():
    return jsonify({"name": "alice", "email": "alice@outlook.com"})


@app.route(TASK_ROUTE, methods=["DELETE"])
def delete():
    return jsonify({"name": "alice", "email": "alice@outlook.com"})
