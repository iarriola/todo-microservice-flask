import os
import psycopg2
from dotenv import load_dotenv

import json
from flask import Flask, jsonify, request, make_response, redirect, render_template

load_dotenv()

app = Flask(__name__)

DB_URL = os.getenv("DATABASE_URL")
CONNECION = psycopg2.connect(DB_URL)

TASK_ROUTE = "/api/v1/tasks/:id"
TASKS_ROUTE = "/api/v1/tasks"

# select id, uuid, title, description, created_at, completed_at, deleted_at from task;


@app.route(TASK_ROUTE, methods=["GET"])
def get():
    return jsonify({"name": "alice", "email": "alice@outlook.com"})


SELECT_ALL = "select uuid, title, description, created_at, completed_at, deleted_at from todo.task;"


@app.route(TASKS_ROUTE, methods=["GET"])
def get_all():
    with CONNECION.cursor() as cursor:
        cursor.execute(SELECT_ALL)
        tasks = cursor.fetchall()
        if tasks:
            result = []
            for task in tasks:
                result.append(
                    {
                        "id": task[0],
                        "title": task[1],
                        "description": task[2],
                        "createdAt": task[3],
                        "completedAt": task[4],
                        "deletedAt": task[5],
                    }
                )
            return result, 200
        else:
            return jsonify([]), 200


@app.route(TASKS_ROUTE, methods=["POST"])
def post():
    return jsonify({"name": "alice", "email": "alice@outlook.com"})


@app.route(TASKS_ROUTE, methods=["PATCH"])
def patch():
    return jsonify({"name": "alice", "email": "alice@outlook.com"})


@app.route(TASK_ROUTE, methods=["DELETE"])
def delete():
    return jsonify({"name": "alice", "email": "alice@outlook.com"})
