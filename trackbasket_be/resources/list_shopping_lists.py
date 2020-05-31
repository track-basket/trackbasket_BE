from flask_restful import Resource, reqparse, request
from models.basemodel import BaseModel, db
from models.shopping_list import ShoppingList
from models.at_risk_user import AtRiskUser
from models.item import Item
from datetime import datetime
from sqlalchemy.sql import func
import requests

class ListShoppingLists(Resource):

  def get(self):
    lists = ShoppingList.query.filter_by(status="pending").all()

    lists_info = []

    for lst in lists:
      total = 0
      list_info = {}

      list_info['at_risk_user_id'] = lst.at_risk_user.at_risk_user_id
      for item in lst.items:
        total += item.quantity
      list_info['item_count'] = total
      list_info['lat_long'] = "{},{}".format(lst.at_risk_user.store[0].latitude, lst.at_risk_user.store[0].longitude)
      list_info['created_at'] = lst.created_date.strftime("%d/%m/%Y %H:%M:%S")
      lists_info.append(list_info)
      
    return {'data': { 'id': 'listshoppinglists', 'attributes': { 'lists': lists_info } } }, 200


    # return {'data': {  "id": "listshoppinglists","attributes":
    #         { "latLng": "{},{}".format(store.latitude, store.longitude), "status": shopping_list.status,
    #           "created_date": shopping_list.created_date.strftime("%d/%m/%Y %H:%M:%S"),
    #           "items": [item.json() for item in shopping_list.items] } } }
