from flask_restful import Resource, reqparse, request 
from ..models.at_risk_user import AtRiskUser
from ..models.basemodel import BaseModel,db 
from ..models.krogerservice import Krogerservice
from ..models.store import Store
from ..models.item import Item

class AtRiskUsers(Resource):
  
  def get(self, id): 
    at_risk_user = AtRiskUser.find_by_id(id)
    if at_risk_user:
      return at_risk_user.json(), 200
    return {'data': { 'id': 'at_risk_user', 'attributes': {'error': 'User not found'} } }, 400
  
  def post(self, id):
    data = request.json
    if AtRiskUser.find_by_id(id):
      return {'data': { 'id': 'at_risk_user', 'attributes': {'error': 'AtRiskUser already exists'} } }, 400
    at_risk_user = AtRiskUser(at_risk_user_id=id, **data)
    store_info = Krogerservice.closest_store(data['zipcode'])
    if store_info == {'error': 'no store found for this zipcode'}:
      return {'data': { 'id': 'at_risk_user', 'attributes': {'error': 'No Kroger store match AtRiskUser zipcode'} } }, 400
    at_risk_user.save(store_info)
    return at_risk_user.json(), 201

  def patch(self, id):
    data = request.json 
    at_risk_user = AtRiskUser.find_by_id(id)
    if at_risk_user is None:
      return {'data': { 'id': 'at_risk_user', 'attributes': {'error': 'User not found'} } }, 400
    at_risk_user.set_attrs(name = data['name'], address = data['address'], 
    city = data['city'], state = data['state'], zipcode = data['zipcode'], phone_number = data['phone_number'])
    db.session.commit()
    return at_risk_user.json(), 200
  
  def delete(self, id):
    at_risk_user = AtRiskUser.find_by_id(id)
    if at_risk_user is None:
      return {'data': { 'id': 'at_risk_user', 'attributes': {'error': 'at_risk_user does not exist'} } }, 400
    at_risk_user.delete_shoppinglists()
    at_risk_user.delete()
    return {'data': { 'id': 'at_risk_user', 'attributes': {'message': 'at_risk_user with id {} successfully deleted'.format(id)} } }, 200