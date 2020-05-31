from models.basemodel import BaseModel, db
from models.item import Item
import datetime 

class ShoppingList(BaseModel, db.Model):
  __tablename__ = 'shopping_lists'
  id = db.Column(db.Integer, primary_key=True)
  status = db.Column(db.String)
  at_risk_user_id = db.Column(db.Integer, db.ForeignKey('at_risk_users.id'))
  created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  items = db.relationship('Item', backref='shopping_list')