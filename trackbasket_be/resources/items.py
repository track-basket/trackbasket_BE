from flask_restful import Resource, reqparse, request
from models.basemodel import BaseModel
from models.krogerservice import Krogerservice
import requests 

class Items(Resource): 
  
  def get(self, term):
    params = request.json
    at_risk_user_id = params['at_risk_user_id']
    items = Krogerservice.item_search(term, at_risk_user_id)
    if  items['data']['attributes'] == []:
       return {'data': { 'id': 'items', 'attributes': {'error': 'Item not found'} } }, 400
    else:
      return items, 200
