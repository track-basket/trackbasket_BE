
from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from models.basemodel import db
from models.volunteer import Volunteer
from resources.volunteer import Volunteers
from resources.store import Stores
from models.at_risk_user import AtRiskUser
from resources.at_risk_user import AtRiskUsers
from resources.shopping_list import ShoppingLists
from models.store import Store

POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432',
}

app = Flask(__name__)
api = Api(app)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api.add_resource(Volunteers, '/volunteer/<string:id>')
api.add_resource(AtRiskUsers, '/atriskuser/<string:id>')
api.add_resource(Stores, '/store/<string:id>')
api.add_resource(ShoppingLists, '/shoppinglist/<string:id>')

if __name__ == '__main__':
    app.run(port= 5000, debug= True)
