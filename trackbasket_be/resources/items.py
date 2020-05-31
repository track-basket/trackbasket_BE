from flask_restful import Resource, reqparse, request
from models.basemodel import BaseModel
from models.krogerservice import Krogerservice
import requests 

class Items(Resource): 
  
  def get(self, term):
    
    params = request.json
    at_risk_user_id = params['at_risk_user_id']
    items = Krogerservice.item_search(term, at_risk_user_id)
    if items:
      return items
    else:
       return {'data': { 'id': 'items', 'attributes': {'message': 'Item not found'} } }, 400
      
  
    
    