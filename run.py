from trackbasket_be import create_app
from flask_socketio import SocketIO, send
# do this once you're ready for production, etc:
# config_name = os.getenv('APP_SETTINGS')
config_name = "development"

app = create_app(config_name)
socketio = SocketIO(app)

from flask_socketio import join_room, leave_room

@socketio.on('join')
def on_join(data):
    import ipdb; ipdb.set_trace()
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

if __name__ == '__main__':
  socketio.run(app)
  # app.run(port= 5000, debug= True)