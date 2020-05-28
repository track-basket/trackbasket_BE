from flask_restful import Resource, reqparse, request 
from models.at_risk_user import AtRiskUser, db 
from models.basemodel import BaseModel 

class AtRiskUsers(Resource):
  
  def get(self, id): 
    at_risk_user = AtRiskUser.find_by_id(id)
    
    return at_risk_user.json()
  
  def post(self, id):
    data = request.json 
    
    at_risk_user = AtRiskUser(name=data['name'], 
                              address=data['address'], 
                              city=data['city'], 
                              state=data['state'], 
                              phone_number=data['phone_number'], 
                              at_risk_user_id=id)
    at_risk_user.save_to_db()
    
    return at_risk_user.json(), 201

  def put(self, id):
    data = request.json 
    
    at_risk_user = AtRiskUser.find_by_id(id)
    at_risk_user.name = data['name']
    at_risk_user.address = data['address']
    at_risk_user.city = data['city']
    at_risk_user.state = data['state']
    at_risk_user.phone_number = data['phone_number']
    
    at_risk_user.save_to_db()
    
    return at_risk_user.json()
    