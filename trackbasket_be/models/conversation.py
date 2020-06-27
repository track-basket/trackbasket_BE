from .basemodel import BaseModel, db
import datetime 
from .message import Message

class Conversation(BaseModel, db.Model):
  __tablename__ = 'conversations'
  id = db.Column(db.Integer, primary_key=True)
  at_risk_user_id = db.Column(db.String, db.ForeignKey('at_risk_users.id'))
  volunteer_id = db.Column(db.String)
  created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  messages = db.relationship('Message', backref='conversation')

  @classmethod 
  def find_by_id(cls, at_risk_user_id, volunteer_id):
    return cls.query.filter_by(at_risk_user_id=at_risk_user_id, volunteer_id=volunteer_id).first()

  @classmethod
  def create(cls, at_risk_user_id, volunteer_id):
    conversation = cls(volunteer_id=volunteer_id, at_risk_user_id=at_risk_user_id)
    db.session.add(conversation)
    db.session.commit()
    return conversation

  def add_message(self, text, author, timestamp):
    message = Message(text=text, conversation=self, author=author, created_date=timestamp)
    db.session.add(message)
    db.session.commit()

  def json(self):
    return {'data': {  "id": "conversation", "attributes":
          { "messages": [message.json() for message in self.messages] } } }


