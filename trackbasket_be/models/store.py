from models.basemodel import BaseModel, db
import datetime

class Store(BaseModel, db.Model):
  __tablename__ = 'stores'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String)
  location_id = db.Column(db.String)
  address = db.Column(db.String)
  city = db.Column(db.String)
  state = db.Column(db.String)
  zipcode = db.Column(db.String)
  latitude = db.Column(db.String)
  longitude = db.Column(db.String)
  at_risk_user_id = db.Column(db.Integer, db.ForeignKey('at_risk_users.id'))

  def json(self):
    return {
      'name': self.name, 
      'location_id': self.location_id, 
      'address': self.address, 
      'city': self.city, 
      'state': self.state, 
      'zipcode': self.zipcode, 
      'latitude': self.latitude,
      'longitude': self.longitude
    }
