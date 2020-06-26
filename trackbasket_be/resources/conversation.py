from flask_restful import Resource, reqparse, request
from ..models.at_risk_user import AtRiskUser
from ..models.conversation import Conversation
from ..models.basemodel import BaseModel
import requests 

class Conversations(Resource): 
  
  def get(self):
    params = request.args.to_dict()
    at_risk_user = AtRiskUser.find_by_id(params['at_risk_user_id']) 
    conversation = Conversation.find_by_id(at_risk_user.id, params['volunteer_id'])
    if conversation is None:
      return {'data': { 'id': 'conversations', 'attributes': {'error': 'Conversation not found'} } }, 400
    return conversation.json(), 200
