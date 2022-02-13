from flask_socketio import SocketIO, emit
from flask import Flask

app = Flask(__name__)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

@socketio.on('message')
def chatMessage(data):
    emit('message', data, broadcast=True)

socketio.run(app, host="0.0.0.0")
