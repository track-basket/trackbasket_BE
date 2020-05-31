from models.basemodel import BaseModel, db
import datetime 

class Item(BaseModel, db.Model):
  __tablename__ = 'items'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  description = db.Column(db.String)
  unit_price = db.Column(db.Float)
  image = db.Column(db.String)
  productId = db.Column(db.String)
  upc = db.Column(db.String)
  quantity = db.Column(db.Integer)
  aisle_number = db.Column(db.Integer)
  shopping_list_id = db.Column(db.Integer, db.ForeignKey('shopping_lists.id'))

  
  def json(self):
    return {
      'name': self.name, 
      'description': self.description, 
      'unit_price': self.unit_price, 
      'image': self.image, 
      'productId': self.productId, 
      'upc': self.upc, 
      'quantity': self.quantity,
      'aisle_number': self.aisle_number,
    }