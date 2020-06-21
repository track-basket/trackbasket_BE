from .basemodel import BaseModel, db
from .store import Store
from .shopping_list import ShoppingList
from .store import Store
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
import datetime 

class AtRiskUser(BaseModel, db.Model):
  __tablename__ = 'at_risk_users'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  at_risk_user_id = db.Column(db.String)
  address = db.Column(db.String)
  city = db.Column(db.String)
  state = db.Column(db.String)
  zipcode = db.Column(db.String)
  phone_number = db.Column(db.String)
  store = db.relationship('Store', backref=backref('at_risk_user', uselist=False))
  shopping_lists = db.relationship('ShoppingList', backref='at_risk_user')

  def json(self):
    return {'data': { 'id': 'at_risk_user', 'attributes': {'name': self.name, 'at_risk_user_id': self.at_risk_user_id, 'address': self.address, 'city': self.city, 'state': self.state, 'zip code': self.zipcode, 'phone number': self.phone_number} } }

  @classmethod 
  def find_by_id(cls, id):
    return cls.query.filter_by(at_risk_user_id=id).first()

  def save(self, store_info):
    store = Store(**store_info, at_risk_user=self)
    db.session.add(self)
    db.session.add(store)
    db.session.commit()    

  def set_attrs(self, **kwargs):
    for k,v in kwargs.items():
      setattr(self, k, v)

  def delete_shoppinglists(self):
    for lst in self.shopping_lists:
        if lst.items != None:
          for item in lst.items:
            db.session.delete(item) 
            db.session.commit()
        db.session.delete(lst) 
        db.session.commit()
  
  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  def return_store(self):
    return self.store[0]

  def return_shopping_list(self):
    return self.shopping_lists[-1]