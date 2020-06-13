import unittest
import json
from trackbasket_be.models.store import Store
from trackbasket_be import create_app, db

class TestStore(unittest.TestCase):

  def setUp(self):
    self.app = create_app('testing')
    self.test_app = self.app.test_client()
    with self.app.app_context():
        db.create_all()
    self.store = Store(name='store1', location_id='9820340237', address= '12 Elm Street', city= 'Cambridge', state= 'MA', zipcode= '02139', latitude= '1234', longitude= '4321')
  
  def tearDown(self):
    with self.app.app_context():
      db.session.remove()
      db.drop_all()

  def test_new_store(self):
    self.assertEqual(self.store.name, 'store1')
    self.assertEqual(self.store.location_id, '9820340237')
    self.assertEqual(self.store.address, '12 Elm Street')
    self.assertEqual(self.store.city, 'Cambridge')
    self.assertEqual(self.store.state, 'MA')
    self.assertEqual(self.store.zipcode, '02139')
    self.assertEqual(self.store.latitude, '1234')
    self.assertEqual(self.store.longitude, '4321')

  # def test_read_store(self):
  #   response = self.test_app.get('/store/1234', json={'zipcode': '80012' })
  #   self.assertEqual(response.status_code, 200)
  #   payload = json.loads(response.data)
  #   self.assertEqual(payload['location_id'], '62000010')
  #   self.assertEqual(payload['name'], 'KINGSOOPERS')
  #   self.assertEqual(payload['address'], '15250 E Mississippi Ave')
  #   self.assertEqual(payload['city'], 'Aurora')
  #   self.assertEqual(payload['state'], 'CO')
  #   self.assertEqual(payload['zipcode'], '80012')
  #   self.assertEqual(payload['latitude'], 39.6951161)
  #   self.assertEqual(payload['longitude'], -104.8109163)

if __name__ == '__main__':
    unittest.main()