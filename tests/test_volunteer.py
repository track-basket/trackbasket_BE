import unittest
import json
from trackbasket_be import create_app, db
from trackbasket_be.models.volunteer import Voluntter

class TestVolunteers(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.test_app = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

    def test_get_all_users(self):
        user = User(name='ian douglas')
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()
