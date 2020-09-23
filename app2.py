from flask import Flask, session
from flask_socketio import SocketIO, emit, join_room, leave_room

from temp.routes import main_b

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "mysecret"
socketio = SocketIO(app)


app.register_blueprint(main_b)


@socketio.on("joined", namespace="/chat")
def joined(message):
    room = session.get("room")
    join_room(room)
    emit("status", {"msg": session.get("name") + " has entered the room."}, room=room)


@socketio.on("text", namespace="/chat")
def text(message):
    room = session.get("room")
    emit("message", {"msg": session.get("name") + " : " + message["msg"]}, room=room)


@socketio.on("left", namespace="/chat")
def left(message):
    room = session.get("room")
    leave_room(room)
    emit("status", {"msg": session.get("name") + " has left the room."}, room=room)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
