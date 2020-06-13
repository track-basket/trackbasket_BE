import unittest
import json
from trackbasket_be.models.basemodel import db
from trackbasket_be.models.shopping_list import ShoppingList
from trackbasket_be.models.at_risk_user import AtRiskUser
from trackbasket_be.models.item import Item
from trackbasket_be.models.shopping_list import ShoppingList
from trackbasket_be.models.store import Store
from trackbasket_be import create_app, db
import datetime
from datetime import timezone

class TestShoppingList(unittest.TestCase):

    # def setUp(self):
    #   self.test_app = app.test_client()
    #   at_risk_user = AtRiskUser(name='Bob Doe',  at_risk_user_id = '2351647', address='12 Elm Street', city='Cambridge', state='MA', zipcode='02139', phone_number= '(234) 401-4329')
    #   with app.app_context():
    #     db.session.add(at_risk_user)
    #     db.session.commit()

    #   store = Store(name='store1', location_id='9820340237', address= '12 Elm Street', city= 'Cambridge', state= 'MA', zipcode= '02139', latitude= '1234', longitude= '4321', at_risk_user_id= at_risk_user.id)
    #   db.session.add(store)
    #   db.session.commit()
  
      
    def test_create_shopping_list(self):
      # import ipdb; ipdb.set_trace()
      # item1 = Item(description='bread', unit_price= 1.55, image='http://www.somelink.com/bread.jpg', upc='93850384', quantity=1, aisle_number=5)
      # item2 = Item(description='chocolate', unit_price= 2.39, image='http://www.somelink.com/chocolate.jpg', upc='03929849', quantity=4, aisle_number=4)
      
      # response = self.test_app.post('/shoppinglist/2351647', json={ "status": "pending", "items": [item1.json(), item2.json()] })
      
      # self.assertEqual(response.status_code, 201)
      pass

if __name__ == '__main__':
    unittest.main()