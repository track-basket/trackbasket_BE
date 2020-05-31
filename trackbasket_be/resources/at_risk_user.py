from flask_restful import Resource, reqparse, request 
from models.at_risk_user import AtRiskUser
from models.basemodel import BaseModel,db 
from models.krogerservice import Krogerservice
from models.store import Store

class AtRiskUsers(Resource):
  
  def get(self, id): 
    at_risk_user = AtRiskUser.find_by_id(id)
    if at_risk_user:
      return at_risk_user.json(), 200
    else: 
      return {'data': { 'id': 'at_risk_user', 'attributes': {'error': "User not found"} } }, 400
  
  def post(self, id):
    data = request.json
    at_risk_user = AtRiskUser(at_risk_user_id=id, **data)
    store_info = Krogerservice.closest_store(data['zipcode'])
    store = Store(**store_info, at_risk_user=at_risk_user)
    db.session.add(at_risk_user)
    db.session.add(store)
    db.session.commit()
    return at_risk_user.json(), 201

  def patch(self, id):
    data = request.json 
    at_risk_user = AtRiskUser.find_by_id(id)
    
    if at_risk_user:
      at_risk_user.name = data['name']
      at_risk_user.address = data['address']
      at_risk_user.city = data['city']
      at_risk_user.state = data['state']
      at_risk_user.zipcode = data['zipcode']
      at_risk_user.phone_number = data['phone_number']
    else: 
      return {'data': { 'id': 'at_risk_user', 'attributes': {'error': "User not found"} } }, 400
    db.session.commit()
    return at_risk_user.json(), 200
    