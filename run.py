from trackbasket_be import create_app
from flask_socketio import SocketIO, send
from flask_socketio import join_room, leave_room, emit
from flask import request
from trackbasket_be.models.at_risk_user import AtRiskUser
from trackbasket_be.models.conversation import Conversation
from trackbasket_be.models.message import Message
# from flask import Flask, render_template
# do this once you're ready for production, etc:
# config_name = os.getenv('APP_SETTINGS')
config_name = "development"

app = create_app(config_name)
# app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*', logger=True, engineio_logger=True)

@socketio.on('connect')
def on_connect():
  print('just connected')

@socketio.on('joinRoom')
def on_join(data):
    id = data['id']
    print('id: ' + data['id'])
    join_room(id)

@socketio.on('chat message')
def handle_message(data):
  room = data['id']
  at_risk_user = AtRiskUser.find_by_id(data['id'])
  conversation = Conversation.find_by_id(at_risk_user.id, data['volunteer_id'])
  if conversation is None:
    conversation = Conversation.create(at_risk_user.id, data['volunteer_id'])
  conversation.add_message(data['message']['text'], data['message']['author'], data['message']['timestamp'])
  emit('chat message', data['message']['text'], room=room)

@socketio.on('leaveRoom')
def on_leave(data):
  print('about to leave room {}'.format(data['id']))
  leave_room(id)

@socketio.on('statusChange')
def change_status(data):
  room = data["id"]
  print('changing status' + data["message"])
  emit('status change', data["message"], room=room)

if __name__ == '__main__':
  socketio.run(app)
  # app.run(port= 5000, debug= True)