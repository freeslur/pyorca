from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_socketio import SocketIO, emit

from config import Config
from serve.database import db
from serve.views.v_acceptance import acceptance_router, get_acc_datas
from serve.views.v_patient import patient_router

app = Flask(__name__)

CORS(app)

app.config.from_object(Config)

db.init_app(app)
Migrate(app, db)


app.register_blueprint(acceptance_router, url_prefix="/api")
app.register_blueprint(patient_router, url_prefix="/api")


socketio = SocketIO(app, cors_allowed_origins="*")

thread = None


def background_thread():
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        data = {"status": "push", "data": get_acc_datas()}
        socketio.emit(
            "accres",
            data,
            namespace="/accsocket",
        )


@socketio.on("connect", namespace="/accsocket")
def connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)
    emit("accres", {"status": "Connected", "data": []})


# @socketio.on("acc_new", namespace="/accsocket")
# def acc_new(data, methods=["GET", "POST"]):
#     print(data)
#     emit("accres", {"data": "data"})


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
