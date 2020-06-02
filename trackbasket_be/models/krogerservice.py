from flask_restful import Resource, reqparse, request
from models.at_risk_user import AtRiskUser
import requests
import os
import json

class Krogerservice:

  @classmethod
  def return_token(cls):
    try:
      access_token
    except NameError:
      return Krogerservice.refresh_token()
    else:
      return access_token

  @classmethod
  def refresh_token(cls):
    client = os.environ.get("CLIENT")
    authorization = 'Basic {}'.format(client)
    data = { 'grant_type':'client_credentials', 'scope': 'product.compact' }
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': authorization}
    response = requests.post('https://api.kroger.com/v1/connect/oauth2/token', headers=headers, data=data).json()
    global access_token 
    access_token = response['access_token']
    return access_token
  
  @classmethod
  def closest_store(cls, zipcode):
    parameters = {'filter.zipCode.near': zipcode, 'filter.limit':1}
    headers = {'Authorization': 'Bearer {}'.format(Krogerservice.return_token())}  
    response = requests.get('https://api.kroger.com/v1/locations?', params=parameters, headers=headers)
#     parsed_response = response.json()
    return {'status code': response.status_code, 
            'response': response.text
           }

    if response.status_code != 200:
      headers = {'Authorization': 'Bearer {}'.format(Krogerservice.refresh_token())}  
      response = requests.get('https://api.kroger.com/v1/locations?', params=parameters, headers=headers)
      parsed_response = response.json()

    return  {
              'location_id': parsed_response['data'][0]['locationId'], 
              'name': parsed_response['data'][0]['chain'], 
              'address': parsed_response['data'][0]['address']['addressLine1'], 
              'city': parsed_response['data'][0]['address']['city'], 
              'state': parsed_response['data'][0]['address']['state'], 
              'zipcode': parsed_response['data'][0]['address']['zipCode'],
              'latitude': parsed_response['data'][0]['geolocation']['latitude'],
              'longitude': parsed_response['data'][0]['geolocation']['longitude']            
            }
  
  @classmethod
  def item_search(cls, term, at_risk_user_id):
    
    user = AtRiskUser.find_by_id(at_risk_user_id) 
    nearest_store = user.store[0]
    nearest_store_id = nearest_store.location_id
    parameters = {'filter.term': term, 'filter.locationId': nearest_store_id}
    headers = {'Authorization': 'Bearer {}'.format(Krogerservice.return_token())}
    response = requests.get('https://api.kroger.com/v1/products', params=parameters, headers=headers)

    json_items = response.json()['data']
    
    items = []   
      
    for item in json_items:
      data = {}
      
      data['name'] = item['description']
      data['productId'] = item['productId']
      data['upc'] = item['upc']
      data['aisle_number'] = int(item['aisleLocations'][0]['number']) 
      data['unit_price'] = item['items'][0]['price']['regular']
      for image in item['images']:
        if image['perspective'] == 'front': 
          for size in image['sizes']: 
            if size['size'] == 'medium':
              data['image'] = size['url']
              
      items.append(data)
      
    return { 'data': { 'id': 'items', 'attributes':  items } }
  
