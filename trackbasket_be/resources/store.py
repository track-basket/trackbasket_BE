from flask_restful import Resource, reqparse, request
from models.basemodel import BaseModel
from models.krogerservice import Krogerservice
import requests

class Stores(Resource):

  def get(self,id):
    request_data = request.json
    zipcode = request_data['zipcode']
    parameters = {'filter.zipCode.near': zipcode, 'filter.limit':1}
    headers = {'Authorization': 'Bearer {}'.format(Krogerservice.return_token())}  
    
    response = requests.get('https://api.kroger.com/v1/locations?', params=parameters, headers=headers)
    parsed_response = response.json()

    if response.status_code != 200:
      headers = {'Authorization': 'Bearer {}'.format(Krogerservice.refresh_token())}  
      response = requests.get('https://api.kroger.com/v1/locations?', params=parameters, headers=headers).json()
      parsed_response = response.json()

    return  {'data': 
              { 'id': 'store', 
                'attributes': 
                  { 'location_id': parsed_response['data'][0]['locationId'], 
                    'name': parsed_response['data'][0]['chain'], 
                    'address': parsed_response['data'][0]['address']['addressLine1'], 
                    'city': parsed_response['data'][0]['address']['city'], 
                    'state': parsed_response['data'][0]['address']['state'], 
                    'zipcode': parsed_response['data'][0]['address']['zipCode'],
                    'latitude': parsed_response['data'][0]['geolocation']['latitude'],
                    'longitude': parsed_response['data'][0]['geolocation']['longitude']
                  }
              }
    }