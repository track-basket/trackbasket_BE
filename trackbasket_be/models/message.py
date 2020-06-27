from .basemodel import BaseModel, db
import datetime 

class Message(BaseModel, db.Model):
  __tablename__ = 'messages'
  id = db.Column(db.Integer, primary_key=True)
  conversation_id = db.Column(db.Integer, db.ForeignKey('conversations.id'))
  text = db.Column(db.String)
  author = db.Column(db.String)
  created_date = db.Column(db.String)
  # created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  
  def json(self):
    return {"text": self.text, "timestamp": self.created_date, "author": self.author}