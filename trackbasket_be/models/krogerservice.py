from flask_restful import Resource, reqparse, request
from .at_risk_user import AtRiskUser
import requests, os, json

proxyDict = { "http"  : os.environ.get('FIXIE_URL', ''), "https" : os.environ.get('FIXIE_URL', '') }

class Krogerservice:

  @classmethod
  def closest_store(cls, zipcode):
    response  = cls.__store_api_request(zipcode)
    store = cls.__extract_kroger_store(response)
    if store is None:
      return { 'error': 'no store found for this zipcode' }
    return  { 'location_id': store['locationId'], 'name': store['chain'],'address': store['address']['addressLine1'],
            'city': store['address']['city'],'state': store['address']['state'], 'zipcode': store['address']['zipCode'],
            'latitude': store['geolocation']['latitude'],'longitude': store['geolocation']['longitude'] }
  
  @classmethod
  def item_search(cls, term, at_risk_user_id):
    nearest_store_id = cls.__get_store_id(at_risk_user_id)
    if term == '':
      return 'error'
    json_items = cls.__item_api_request(term, nearest_store_id)
    if json_items == []:
      return 'error'
    items = cls.__extract_items(json_items)
    return { 'data': { 'id': 'items', 'attributes':  items } }

  @classmethod
  def __return_token(cls):
    try:
      access_token
    except NameError:
      return cls.__refresh_token()
    else:
      return access_token

  @classmethod
  def __refresh_token(cls):
    global access_token  
    response = cls.__token_api_request()
    access_token = response.json()['access_token']
    return access_token

  @classmethod
  def __find_image(cls, item):
    if 'images' in item.keys():
      for image in item['images']:
        if (('perspective' in image.keys()) and image['perspective'] == 'front'):
          return next((size['url'] for size in image['sizes'] if size['size'] == 'medium'), None)
  
  @classmethod
  def __format_item(cls, item):
    data = {}
    data['description'] = item['description'] if 'description' in item.keys() else ''
    data['upc'] = item['upc'] if 'upc' in item.keys() else ''
    if ('aisleLocations' in item.keys()) and (item['aisleLocations'] != []):
      data['aisle_number'] = int(item['aisleLocations'][0]['number'])
    if ('price' in item['items'][0].keys()):
      data['unit_price'] = item['items'][0]['price']['regular']
    image = cls.__find_image(item)  
    if image is not None:
      data['image'] = image
    return data
  
  @classmethod
  def __extract_items(cls, json_items):
    items = []
    for item in json_items:
      formatted_item = cls.__format_item(item)  
      items.append(formatted_item)
    return items
  
  @classmethod
  def __store_api_request(cls, zipcode):
    token = cls.__return_token()
    number_results = 5 
    parameters = {'filter.zipCode.near': zipcode, 'filter.limit':number_results}
    headers = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get('https://api.kroger.com/v1/locations?', params=parameters, headers=headers, proxies=proxyDict)
    if response.status_code != 200:
      headers = {'Authorization': 'Bearer {}'.format(cls.__refresh_token())}
      response = requests.get('https://api.kroger.com/v1/locations?', params=parameters, headers=headers, proxies=proxyDict)
    return response

  @classmethod
  def __token_api_request(cls):
    authorization = 'Basic {}'.format(os.environ.get("CLIENT"))
    data = { 'grant_type':'client_credentials', 'scope': 'product.compact' }
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': authorization}
    return requests.post('https://api.kroger.com/v1/connect/oauth2/token', headers=headers, data=data)

  @classmethod
  def __item_api_request(cls, term, nearest_store_id):
    token = cls.__return_token()
    parameters = {'filter.term': term, 'filter.locationId': nearest_store_id}
    headers = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get('https://api.kroger.com/v1/products', params=parameters, headers=headers, proxies=proxyDict)
    if response.status_code != 200:
      headers = {'Authorization': 'Bearer {}'.format(cls.__refresh_token())}
      response = requests.get('https://api.kroger.com/v1/products', params=parameters, headers=headers, proxies=proxyDict)
    return response.json()['data']

  @classmethod
  def __extract_kroger_store(cls, response):
    parsed_response = response.json()
    if parsed_response['data'] == []:
      return  None
    blacklist = ['shell company']
    return next((store for store in parsed_response['data'] if store['name'].lower() not in blacklist), None)

  @classmethod
  def __get_store_id(cls, at_risk_user_id):
    user = AtRiskUser.find_by_id(at_risk_user_id)
    nearest_store = user.store[0]
    return nearest_store.location_id