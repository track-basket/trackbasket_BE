from flask_restful import Resource, reqparse, request
from models.basemodel import BaseModel
from models.krogerservice import Krogerservice
import requests

class Stores(Resource):

  def get(self,id):
    request_data = request.json
    zipcode = request_data['zipcode']
    return Krogerservice.closest_store(zipcode)