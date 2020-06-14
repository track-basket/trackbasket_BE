import unittest
import json
from trackbasket_be.models.basemodel import db
from trackbasket_be.models.at_risk_user import AtRiskUser
from trackbasket_be import create_app, db

class TestAtRiskUser(unittest.TestCase):

  def setUp(self):
    self.app = create_app('testing')
    self.test_app = self.app.test_client()
    with self.app.app_context():
        db.create_all()
    self.at_risk_user = AtRiskUser(
        name= 'AtRiskUser1',
        at_risk_user_id= '12345',
        address= '729 East 10th Avenue',
        city= 'Denver',
        state= 'CO',
        zipcode= '80203',
        phone_number= '1234')

  def tearDown(self):
    with self.app.app_context():
      db.session.remove()
      db.drop_all()

  def test_create_at_risk_user(self):
    self.test_app.delete('/atriskuser/4321')
    response = self.test_app.post('/atriskuser/4321', json={ "name": "Alexis", "address": "125 ocean ave", "city": "Denver", "state": "ca", "zipcode": "91763", "phone_number": "123-456-7890"})
    payload = json.loads(response.data)
    self.assertEqual(response.status_code, 201)
    self.assertEqual(payload['data']['attributes']['name'], 'Alexis')
    self.assertEqual(payload['data']['attributes']['at_risk_user_id'], '4321')
    self.assertEqual(payload['data']['attributes']['address'], '125 ocean ave')
    self.assertEqual(payload['data']['attributes']['city'], 'Denver')
    self.assertEqual(payload['data']['attributes']['state'], 'ca')
    self.assertEqual(payload['data']['attributes']['zip code'], '91763')
    self.assertEqual(payload['data']['attributes']['phone number'], '123-456-7890')

    response = self.test_app.post('/atriskuser/4321', json={ "name": "Alexis", "address": "125 ocean ave", "city": "Denver", "state": "ca", "zipcode": "91763", "phone_number": "123-456-7890"})
    self.assertEqual(response.status_code, 400)
    payload = json.loads(response.data)
    self.assertEqual(payload['data']['attributes']['error'],"AtRiskUser already exists")

  def test_read_at_risk_user(self):
    self.test_app.delete('/atriskuser/4321')
    self.test_app.post('/atriskuser/4321', json={ "name": "Alexis", "address": "125 ocean ave", "city": "Denver", "state": "ca", "zipcode": "91763", "phone_number": "123-456-7890"})
    response = self.test_app.get('/atriskuser/4321')
    self.assertEqual(response.status_code, 200)
    payload = json.loads(response.data)
    self.assertEqual(payload['data']['attributes']['name'], 'Alexis')
    self.assertEqual(payload['data']['attributes']['at_risk_user_id'], '4321')
    self.assertEqual(payload['data']['attributes']['address'], '125 ocean ave')
    self.assertEqual(payload['data']['attributes']['city'], 'Denver')
    self.assertEqual(payload['data']['attributes']['state'], 'ca')
    self.assertEqual(payload['data']['attributes']['zip code'], '91763')
    self.assertEqual(payload['data']['attributes']['phone number'], '123-456-7890')
      
  def test_update_at_risk_user(self):
    self.test_app.delete('/atriskuser/4321')
    self.test_app.post('/atriskuser/4321', json={ "name": "Alexis", "address": "125 ocean ave", "city": "Denver", "state": "ca", "zipcode": "91763", "phone_number": "123-456-7890"})
      
    response = self.test_app.patch('/atriskuser/4321', json={ "name": "Mike", "address": "126 ocean ave", "city": "New York", "state": "NY", "zipcode": "84920", "phone_number": "124-456-7890"})

    self.assertEqual(response.status_code, 200)
    payload = json.loads(response.data)
    self.assertEqual(payload['data']['attributes']['name'], 'Mike')
    self.assertEqual(payload['data']['attributes']['at_risk_user_id'], '4321')
    self.assertEqual(payload['data']['attributes']['address'], '126 ocean ave')
    self.assertEqual(payload['data']['attributes']['city'], 'New York')
    self.assertEqual(payload['data']['attributes']['state'], 'NY')
    self.assertEqual(payload['data']['attributes']['zip code'], '84920')
    self.assertEqual(payload['data']['attributes']['phone number'], '124-456-7890')
    self.test_app.delete('/atriskuser/4321')
    response = self.test_app.patch('/atriskuser/55553', json={ "name": "Mike", "address": "126 ocean ave", "city": "New York", "state": "NY", "zipcode": "84920", "phone_number": "124-456-7890"})
    self.assertEqual(response.status_code, 400)
    payload = json.loads(response.data)
    self.assertEqual(payload['data']['attributes']['error'], 'User not found')

  def test_delete_at_risk_user(self):
    self.test_app.post('/atriskuser/4321', json={ "name": "Alexis", "address": "125 ocean ave", "city": "Denver", "state": "ca", "zipcode": "91763", "phone_number": "123-456-7890"})
    response = self.test_app.delete('/atriskuser/4321')
    self.assertEqual(response.status_code, 200)
    payload = json.loads(response.data)
    self.assertEqual(payload['data']['attributes']['message'], 'at_risk_user with id 4321 successfully deleted')

if __name__ == '__main__':
    unittest.main()