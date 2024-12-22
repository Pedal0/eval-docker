import requests
from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from flaskr.controllers.task_controller import TaskController
from flaskr.schemas.schema import TaskSchema, UpdateTaskSchema

bp = Blueprint("tasks", __name__)

# Routes existantes
@bp.route("/tasks")
class Tasks(MethodView):
    @bp.arguments(TaskSchema)
    @bp.response(201)
    def post(self, data):
        return TaskController.create(data)

@bp.route("/tasks")
class TasksOnUser(MethodView):
    @bp.response(200, TaskSchema(many=True))
    def get(self):
        return TaskController.get_all()

@bp.route("/tasks/<task_id>")
class TaskById(MethodView):
    @bp.arguments(UpdateTaskSchema)
    @bp.response(200)
    def put(self, data, task_id):
        return TaskController.update(data, task_id)

    @bp.response(204)
    def delete(self, task_id):
        return TaskController.delete(task_id)

@bp.route("/predict")
class Predict(MethodView):
    def post(self):
        data = request.json
        try:
            response = requests.post("http://tensorflow-service:8501/v1/models/my_model:predict", json=data)
            response.raise_for_status()
            return jsonify(response.json())
        except requests.exceptions.RequestException as e:
            return jsonify({"error": str(e)}), 500
