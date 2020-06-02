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
    if AtRiskUser.query.filter_by(at_risk_user_id=id).first() is None:
      at_risk_user = AtRiskUser(at_risk_user_id=id, **data)
      store_info = Krogerservice.closest_store(data['zipcode'])
      if store_info == {'error': 'no store found for this zipcode'}:
        return {'data': { 'id': 'at_risk_user', 'attributes': {'error': "No Kroger store match AtRiskUser zipcode"} } }, 400
      else:  
        store = Store(**store_info, at_risk_user=at_risk_user)
        db.session.add(at_risk_user)
        db.session.add(store)
        db.session.commit()
        return at_risk_user.json(), 201
    else:
      return {'data': { 'id': 'at_risk_user', 'attributes': {'error': "AtRiskUser already exists"} } }, 400

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
  
  def delete(self, id):
    at_risk_user = db.session.query(AtRiskUser).filter_by(at_risk_user_id=id).first()
    if at_risk_user:
      for lst in at_risk_user.shopping_lists:
        db.session.delete(lst) 
        db.session.commit()
      db.session.commit()
      db.session.delete(at_risk_user)
      db.session.commit()
      return {'data': { 'id': 'at_risk_user', 'attributes': {'message': "at_risk_user with id {} successfully deleted".format(id)} } }, 200
    else:
      return {'data': { 'id': 'at_risk_user', 'attributes': {'error': "at_risk_user does not exist"} } }, 400  
      
      
    
    
