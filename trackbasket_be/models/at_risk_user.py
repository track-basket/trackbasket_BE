from models.basemodel import BaseModel, db
import datetime 

class AtRiskUser(BaseModel, db.Model):
  __tablename__ = 'at_risk_users'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  at_risk_user_id = db.Column(db.String)
  address = db.Column(db.String)
  city = db.Column(db.String)
  state = db.Column(db.String)
  phone_number = db.Column(db.String)

  def json(self):
    return {'name': self.name, 'at_risk_user_id': self.at_risk_user_id, 'address': self.address, 'city': self.city, 'state': self.state, 'phone_number': self.phone_number}

  @classmethod 
  def find_by_id(cls, id):
    return cls.query.filter_by(at_risk_user_id=id).first()
  
  def save_to_db(self):
    db.session.add(self)
    db.session.commit()