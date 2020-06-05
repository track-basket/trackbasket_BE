import unittest
import json
from trackbasket_be.models.basemodel import db
from trackbasket_be.models.item import Item
from trackbasket_be.app import app

class TestItem(unittest.TestCase):

    def setUp(self):
      self.test_app = app.test_client()
      self.item = Item(description='a cool item', unit_price= 4.55, image='http://www.somelink.com/bread.jpg', upc='93850384', quantity=4, aisle_number=5)


    def test_volunteer(self):
      self.assertEqual(self.item.description, 'a cool item')
      self.assertEqual(self.item.unit_price, 4.55)
      self.assertEqual(self.item.image, 'http://www.somelink.com/bread.jpg')
      self.assertEqual(self.item.upc, '93850384')
      self.assertEqual(self.item.quantity, 4)
      self.assertEqual(self.item.aisle_number, 5)

    

if __name__ == '__main__':
    unittest.main()