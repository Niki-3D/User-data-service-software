from flask import Flask, Response, request
import json
from src.repositories import UserRepository
from src.repository_controllers import UserController
from src.status_codes import SUCCESS, BAD_REQUEST, CREATED, NOT_FOUND

app = Flask(__name__)

user_repository = UserRepository()
user_controller = UserController(user_repository)

@app.get('/ping')
def ping() -> str:
    return 'pong'

@app.get('/users')
def get_users() -> Response:
    users = user_controller.get_all()
    return Response(response=json.dumps(users), status=SUCCESS, mimetype='application/json')

@app.get('/users/<int:id>')
def get_user(id: int) -> Response:
    try:
        user = user_controller.get_by_id(id)
        return Response(response=json.dumps(user), status=SUCCESS, mimetype='application/json')
    except ValueError as error:
        return Response(response=str(error), status=BAD_REQUEST)

@app.post("/users")
def post_user() -> Response:
    data = request.get_json()
    try:
        user_controller.create(data)
        return Response(status=CREATED)
    except (ValueError, TypeError) as error:
        return Response(response=str(error), status=BAD_REQUEST)

@app.patch("/users/<int:id>")
def patch_user(id: int) -> Response:
    data = request.get_json()
    try:
        user_controller.update(id, data)
        return Response(status=NOT_FOUND)
    except (ValueError, TypeError) as error:
        return Response(response=str(error), status=BAD_REQUEST)

@app.delete("/users/<int:id>")
def delete_user(id: int) -> Response:
    try:
        user_controller.delete(id)
        return Response(status=NOT_FOUND)
    except ValueError as error:
        return Response(response=str(error), status=BAD_REQUEST)

if __name__ == "__main__":
    app.run("localhost", 8080)
