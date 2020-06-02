from flask_restful import Resource, reqparse, request
from models.basemodel import BaseModel, db
from models.krogerservice import Krogerservice
from models.shopping_list import ShoppingList
from models.at_risk_user import AtRiskUser
from models.item import Item
from datetime import datetime
import requests

class ShoppingLists(Resource):

  def post(self,id):
    request_data = request.json
    at_risk_user = AtRiskUser.query.filter_by(at_risk_user_id=id).first()
    store = at_risk_user.store[0]
    if at_risk_user is None:
      return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "At risk user #{} not found".format(id)} } }, 400
    else:
      shopping_list = ShoppingList(at_risk_user_id=at_risk_user.id, status=request_data['status'], created_date=datetime.now())
      db.session.add(shopping_list)
      db.session.commit()
      for item in request_data["items"]:
        db.session.add(Item(shopping_list_id=shopping_list.id, **item)) 
      db.session.commit()
      return {'data': {  "id": "shoppinglist","attributes":
            { "name": store.name, "address": store.address, "city": store.city, "state": store.state, "zipcode": store.zipcode,
              "storeId": store.location_id, "latitude_longitude": [float(store.latitude), float(store.longitude)], "status": shopping_list.status,
              "created_date": shopping_list.created_date.strftime("%d/%m/%Y %H:%M:%S"),
              "items": [item.json() for item in shopping_list.items] } } }, 200
      # return {'message': 'new shopping list created for user #{}'.format(id)}, 200

  def get(self,id):
    at_risk_user = AtRiskUser.query.filter_by(at_risk_user_id=id).first()
    if at_risk_user is None:
      return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "At risk user not found"} } }, 400
    else:
      if at_risk_user.shopping_lists == []:
        return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "No shopping list associated with this user"} } }, 400
      else:
        shopping_list = at_risk_user.shopping_lists[-1]
        store = at_risk_user.store[0]
        if store is None:
          return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "No store associated with this user"} } }, 400
        else:
          return {'data': {  "id": "shoppinglist","attributes":
              { "name": store.name, "address": store.address, "city": store.city, "state": store.state, "zipcode": store.zipcode,
                "storeId": store.location_id, "latitude_longitude": [float(store.latitude), float(store.longitude)], "status": shopping_list.status,
                "created_date": shopping_list.created_date.strftime("%d/%m/%Y %H:%M:%S"),
                "items": [item.json() for item in shopping_list.items] } } }, 200

  def patch(self,id):
    request_data = request.json
    at_risk_user = AtRiskUser.query.filter_by(at_risk_user_id=id).first()
    store = at_risk_user.store[0]
    if at_risk_user is None:
      return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "At risk user #{} not found".format(id)} } }, 400
    else:
      shopping_list = at_risk_user.shopping_lists[-1]
      
      shopping_list.status = request_data['status']
      db.session.commit()
      for item in shopping_list.items:
        db.session.delete(item)
      db.session.commit()
      for item in request_data["items"]:
        db.session.add(Item(shopping_list_id=shopping_list.id, **item)) 
      db.session.commit()
      
      return {'data': {  "id": "shoppinglist","attributes":
            { "name": store.name, "address": store.address, "city": store.city, "state": store.state, "zipcode": store.zipcode,
              "storeId": store.location_id, "latitude_longitude": [float(store.latitude), float(store.longitude)], "status": shopping_list.status,
              "created_date": shopping_list.created_date.strftime("%d/%m/%Y %H:%M:%S"),
              "items": [item.json() for item in shopping_list.items] } } }, 200
      

  def delete(self,id):
    at_risk_user = AtRiskUser.query.filter_by(at_risk_user_id=id).first()
    if at_risk_user is None:
      return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "At risk user #{} not found".format(id)} } }, 400
    elif len(at_risk_user.shopping_lists) == 0:
        return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "At risk user #{} does not have shopping lists".format(id)} } }, 400
    else:
      shopping_list = at_risk_user.shopping_lists[-1]
      for item in shopping_list.items:
        db.session.delete(item)
      db.session.commit()
      db.session.delete(shopping_list)
      db.session.commit()
      return {'data': { 'id': 'shoppinglist', 'attributes': {'message': "The shopping list was deleted"} } }, 200