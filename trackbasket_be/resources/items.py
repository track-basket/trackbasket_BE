from flask_restful import Resource, reqparse, request
from ..models.basemodel import BaseModel
from ..models.krogerservice import Krogerservice
import requests 

class Items(Resource): 
  
  def get(self):
    params = request.args.to_dict()
    items = Krogerservice.item_search(params['product'], params['at_risk_user_id'])
    if items == 'error':
      return {'data': { 'id': 'items', 'attributes': {'error': 'Item not found'} } }, 400
    return items, 200
