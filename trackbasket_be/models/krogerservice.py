from flask_restful import Resource, reqparse, request
import requests
import os

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