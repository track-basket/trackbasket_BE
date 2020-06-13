from .basemodel import BaseModel
from trackbasket_be import db
# from models.basemodel import db
import datetime

class Volunteer(BaseModel, db.Model):
  __tablename__ = 'volunteers'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String)
  volunteer_id = db.Column(db.String)
  phone_number = db.Column(db.String)

  def __repr__(self):
    return 'Id: {}, name: {}'.format(self.id, self.name)
