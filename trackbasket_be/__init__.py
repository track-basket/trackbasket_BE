import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(config_name):

  from flask import Flask, request
  from flask_restful import Resource, Api
  from trackbasket_be.config import app_config

  app = Flask(__name__)
  api = Api(app)
  app.config.from_object(app_config[config_name])
  # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
  # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
  # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  

  db.init_app(app)
  
  from flask_sqlalchemy import SQLAlchemy
  # from trackbasket_be.models.basemodel import db
  from trackbasket_be.models.volunteer import Volunteer
  from trackbasket_be.resources.volunteer import Volunteers
  from trackbasket_be.resources.store import Stores
  from trackbasket_be.models.at_risk_user import AtRiskUser
  from trackbasket_be.resources.at_risk_user import AtRiskUsers
  from trackbasket_be.resources.shopping_list import ShoppingLists
  from trackbasket_be.models.store import Store
  from trackbasket_be.resources.items import Items
  from trackbasket_be.resources.conversation import Conversations
  from trackbasket_be.resources.list_shopping_lists import ListShoppingLists
  import os
# POSTGRES = {
#     'user': 'postgres',
#     'pw': 'password',
#     'db': 'my_database',
#     'host': 'localhost',
#     'port': '5432',
# }

  
  api.add_resource(Volunteers, '/volunteer/<string:id>')
  api.add_resource(AtRiskUsers, '/atriskuser/<string:id>')
  api.add_resource(Stores, '/store/<string:id>')
  api.add_resource(Items, '/items')
  api.add_resource(Conversations, '/conversations')
  api.add_resource(ShoppingLists, '/shoppinglist/<string:id>')
  api.add_resource(ListShoppingLists, '/listshoppinglists/')
  
  return app