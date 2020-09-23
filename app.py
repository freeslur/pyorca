from flask import Flask, session
from flask_cors import CORS
from flask_migrate import Migrate
from flask_socketio import SocketIO, emit

from config import Config
from serve.database import db
from serve.views.v_acceptance import acceptance_router
from serve.views.v_patient import patient_router

app = Flask(__name__)

CORS(app)

app.config.from_object(Config)

db.init_app(app)
Migrate(app, db)


app.register_blueprint(acceptance_router, url_prefix="/api")
app.register_blueprint(patient_router, url_prefix="/api")
socketio = SocketIO(app)


# @socketio.on("connect", namespace="/accsocket")
# def acc_connect():
#     emit("response", {"data": "Connected", "username": session["username"]})


# @socketio.on("disconnect", namespace="/accsocket")
# def acc_disconnect():
#     session.clear()
#     print("Disconnect")


@socketio.on("acc_new", namespace="/accsocket")
def acc_new(data, methods=["GET", "POST"]):
    emit("response", {"data": data["data"], "username": session["username"]})


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
