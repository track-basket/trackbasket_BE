from .basemodel import BaseModel, db
from .item import Item
import datetime 


class ShoppingList(BaseModel, db.Model):
  __tablename__ = 'shopping_lists'
  id = db.Column(db.Integer, primary_key=True)
  status = db.Column(db.String)
  at_risk_user_id = db.Column(db.Integer, db.ForeignKey('at_risk_users.id'))
  created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  items = db.relationship('Item', backref='shopping_list')
  
  @classmethod
  def create_shopping_list(cls, at_risk_user_id, status, time):
    shopping_list = cls(at_risk_user_id=at_risk_user_id, status=status, created_date=time)
    db.session.add(shopping_list)
    db.session.commit()
    return shopping_list

  def add_items(self, data):
    for item in data:
      db.session.add(Item(shopping_list_id=self.id, **item)) 
      db.session.commit()
  
  def delete_existing_items(self):
    for item in self.items:
      db.session.delete(item)
      db.session.commit()
  
  def delete(self):
    self.delete_existing_items()
    db.session.delete(self)
    db.session.commit()

  def update_status(self, status):
    self.status = status
    db.session.commit()

  def update(self, data):
    self.update_status(data['status'])
    self.delete_existing_items()
    self.add_items(data["items"])
    db.session.commit()

  def json(self, store):
    return {'data': {  "id": "shoppinglist","attributes":
          { "name": store.name, "address": store.address, "city": store.city, "state": store.state, "zipcode": store.zipcode,
            "storeId": store.location_id, "latitude_longitude": [float(store.latitude), float(store.longitude)], "status": self.status,
            "created_date": self.created_date.strftime("%d/%m/%Y %H:%M:%S"),
            "items": [item.json() for item in self.items] } } }
