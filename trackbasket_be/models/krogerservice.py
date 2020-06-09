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
    response = requests.post('https://api.kroger.com/v1/connect/oauth2/token', headers=headers, data=data)
    parsed_response = response.json()
    if response.status_code != 200:
      return  { 'error': 'could not refresh token' }
    access_token = parsed_response['access_token']
    return access_token

  @classmethod
  def closest_store(cls, zipcode):
    token = Krogerservice.refresh_token()
    number_results = 5
    parameters = {'filter.zipCode.near': zipcode, 'filter.limit':number_results}
    headers = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get('https://api.kroger.com/v1/locations?', params=parameters, headers=headers)
#     parsed_response = json.loads(response.text)
    
 #   parsed_response = response.json()

    if response.status_code != 200:
      return  { 'error': 'there was a problem with the API respnse' }
#       token = Krogerservice.refresh_token()
#       headers = {'Authorization': 'Bearer {}'.format(Krogerservice.refresh_token())}
#       response = requests.get('https://api.kroger.com/v1/locations?', params=parameters, headers=headers)
    return {'response': response.text, 'status_code': response.status_code, 'token': token, 'content_type': response.headers['Content-Type'] }  
#     parsed_response = response.json()

    if parsed_response['data'] == []:
      return  { 'error': 'no store found for this zipcode' }

    blacklist = ['shell company']
    i = 0
    while (parsed_response['data'][i]['name'].lower() in blacklist) and (i < number_results - 1):
      i += 1
    if (parsed_response['data'][i]['name'] in blacklist):
      return { 'error': 'no store found for this zipcode' }

    return  {
              'location_id': parsed_response['data'][i]['locationId'],
              'name': parsed_response['data'][ i]['chain'],
              'address': parsed_response['data'][i]['address']['addressLine1'],
              'city': parsed_response['data'][i]['address']['city'],
              'state': parsed_response['data'][i]['address']['state'],
              'zipcode': parsed_response['data'][i]['address']['zipCode'],
              'latitude': parsed_response['data'][i]['geolocation']['latitude'],
              'longitude': parsed_response['data'][i]['geolocation']['longitude']
            }

  @classmethod
  def item_search(cls, term, at_risk_user_id):

    user = AtRiskUser.find_by_id(at_risk_user_id)
    nearest_store = user.store[0]
    nearest_store_id = nearest_store.location_id
    parameters = {'filter.term': term, 'filter.locationId': nearest_store_id}
    if term == '':
      return 'error'

    headers = {'Authorization': 'Bearer {}'.format(Krogerservice.return_token())}
    response = requests.get('https://api.kroger.com/v1/products', params=parameters, headers=headers)

    if response.json()['data'] != []:
      json_items = response.json()['data']
      items = []
      for item in json_items:
        data = {}
        data['description'] = item['description'] if 'description' in item.keys() else ''
        data['upc'] = item['upc'] if 'upc' in item.keys() else ''
        if ('aisleLocations' in item.keys()) and (item['aisleLocations'] != []):
          data['aisle_number'] = int(item['aisleLocations'][0]['number'])
        if ('price' in item['items'][0].keys()):
          data['unit_price'] = item['items'][0]['price']['regular']

        if 'images' in item.keys():
          for image in item['images']:
            if ('perspective' in image.keys()):
              if image['perspective'] == 'front':
                for size in image['sizes']:
                  if size['size'] == 'medium':
                    data['image'] = size['url']

        items.append(data)
      return { 'data': { 'id': 'items', 'attributes':  items } }
    else:
      return 'error'
