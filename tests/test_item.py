import unittest
import json
from trackbasket_be.models.basemodel import db
from trackbasket_be.models.item import Item
from trackbasket_be import create_app, db

class TestItem(unittest.TestCase):

  def setUp(self):
    self.app = create_app('testing')
    self.test_app = self.app.test_client()
    with self.app.app_context():
      db.create_all()
    self.item = Item(description='a cool item', unit_price= 4.55, image='http://www.somelink.com/bread.jpg', upc='93850384', quantity=4, aisle_number=5)

  def tearDown(self):
    with self.app.app_context():
      db.session.remove()
      db.drop_all()

  def test_item(self):
    with self.app.app_context():
      db.session.add(self.item)
      db.session.commit()
      item = Item.query.filter_by(upc='93850384').first()
      
    self.assertEqual(item.description, 'a cool item')
    self.assertEqual(item.unit_price, 4.55)
    self.assertEqual(item.image, 'http://www.somelink.com/bread.jpg')
    self.assertEqual(item.upc, '93850384')
    self.assertEqual(item.quantity, 4)
    self.assertEqual(item.aisle_number, 5)

if __name__ == '__main__':
    unittest.main()