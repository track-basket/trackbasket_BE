from flask_restful import Resource, reqparse, request
from ..models.basemodel import BaseModel, db
from ..models.krogerservice import Krogerservice
from ..models.shopping_list import ShoppingList
from ..models.at_risk_user import AtRiskUser
from ..models.item import Item
from datetime import datetime
import requests

class ShoppingLists(Resource):

  def post(self,id):
    request_data = request.json
    at_risk_user = AtRiskUser.find_by_id(id)
    if at_risk_user is None:
      return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "At risk user #{} not found".format(id)} } }, 400
    store = at_risk_user.return_store()
    if request_data["items"] == []:
      return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "Shopping List can not be empty"} } }, 400
    shopping_list = ShoppingList.create_shopping_list(at_risk_user.id, request_data['status'], datetime.now())
    shopping_list.add_items(request_data["items"])
    return shopping_list.json(store), 200

  def get(self,id):
    at_risk_user = AtRiskUser.find_by_id(id)
    if at_risk_user is None:
      return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "At risk user not found"} } }, 400
    if at_risk_user.shopping_lists == []:
      return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "No shopping list associated with this user"} } }, 400
    shopping_list = at_risk_user.return_shopping_list()
    store = at_risk_user.return_store()
    if store is None:
      return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "No store associated with this user"} } }, 400
    return shopping_list.json(store), 200
    
  def patch(self,id):
    request_data = request.json
    at_risk_user = AtRiskUser.find_by_id(id)
    if at_risk_user is None:
      return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "At risk user #{} not found".format(id)} } }, 400
    store = at_risk_user.return_store()
    if at_risk_user.shopping_lists == []:
      return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "No shopping list associated with this user"} } }, 400
    shopping_list = at_risk_user.return_shopping_list()
    shopping_list.update(request_data)
    return shopping_list.json(store), 200
    
  def delete(self,id):
    at_risk_user = AtRiskUser.find_by_id(id)
    if at_risk_user is None:
      return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "At risk user #{} not found".format(id)} } }, 400
    if at_risk_user.shopping_lists == []:
      return {'data': { 'id': 'shoppinglist', 'attributes': {'error': "At risk user #{} does not have shopping lists".format(id)} } }, 400
    shopping_list = at_risk_user.return_shopping_list()
    shopping_list.delete()
    return {'data': { 'id': 'shoppinglist', 'attributes': {'message': "The shopping list was deleted"} } }, 200