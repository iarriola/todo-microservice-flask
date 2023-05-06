from flask import Blueprint
from .repository import TaskRepository

import json
from flask import Flask, jsonify, request, make_response, redirect, render_template

API_ROUTE_TASK = "/api/v1/tasks/:id"
API_ROUTE_TASKS = "/api/v1/tasks"

router = Blueprint("tasks_routes", __name__)
repo = TaskRepository()


@router.route(API_ROUTE_TASKS, methods=["GET"])
def get_all():
    return jsonify(repo.get_all())
